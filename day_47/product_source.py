from bs4 import BeautifulSoup
import requests
import urllib.parse
from product import Product
from requests_html import HTMLSession

HEADER_USER_AGENT = "Requests"
HEADER_ACCEPT_LANGUAGE = "id-ID"

TOKOPEDIA_URL = "https://www.tokopedia.com/search"
SHOPEE_URL = "https://shopee.co.id/search?keyword={keyword}"


def tokopedia(query: str, limit: int) -> list[Product]:
    param = {
        "q": urllib.parse.quote(query),
        "st": "product",
    }

    header = {
        'User-Agent': HEADER_USER_AGENT,
        "Accept-Language": HEADER_ACCEPT_LANGUAGE,
    }
    response = requests.get(TOKOPEDIA_URL, params=param, headers=header)
    response.raise_for_status()
    html_doc = response.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    products = soup.select("div[data-testid=divSRPContentProducts] .pcv3__info-content")

    results = []
    for product in products[:limit]:
        try:
            price = product.select("div[data-testid=spnSRPProdPrice]")[0].text
        except IndexError:
            continue

        price = price.replace("Rp", "").replace(".", "")
        results.append(
            Product(
                name=product['title'],
                link=product['href'],
                price=int(price),
            )
        )

    return results


def shopee(query: str, limit: int) -> list[Product]:

    param = {
        "keyword": urllib.parse.quote(query),
    }

    header = {
        "accept-encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "if-none-match": "55b03-1ae7d4aa7c47753a96c0ade3a9ea8b35",
        "origin": "https://shopee.co.id",
        "referer": "https://shopee.co.id/asusofficialshop",
        "x-api-source": "pc",
        "x-csrftoken": "8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "cookie": 'SPC_IA=-1; SPC_EC=-; SPC_F=QpolQhTSikpnxRXO6T4RjIW8ZGHNBmBn; REC_T_ID=ac80cdde-0e7d-11e9-a8c2-3c15fb3af585; SPC_T_ID="e4t1VmH0VKB0NajA1BrHaDQlFRwWjTZT7o83rrHW+p16sTf1NJK7ksWWDicCTPq8CVO/S8sxnw25gNR0DLQz3cv7U3EQle9Z9ereUnPityQ="; SPC_SI=k2en4gw50emawx5fjaawd3fnb5o5gu0w; SPC_U=-; SPC_T_IV="in3vKQSBLhXzeTaGwMInvg=="; _gcl_au=1.1.557205539.1546426854; csrftoken=8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO; welcomePkgShown=true; bannerShown=true; _ga=GA1.3.472488305.1546426857; _gid=GA1.3.1348013297.1546426857; _fbp=fb.2.1546436170115.11466858'
    }

    response = requests.get(SHOPEE_URL, params=param, headers=header)
    response.raise_for_status()
    html_doc = response.text
    print(html_doc)

    # try:
    #     session = HTMLSession()
    #     response = session.get(SHOPEE_URL.format(keyword=urllib.parse.quote(query)))
    #
    # except requests.exceptions.RequestException as e:
    #     print(e)
    #
    # response.html.render()
    # print(response.text)

    # soup = BeautifulSoup(html_doc, 'html.parser')
    # products = soup.select(".shopee-search-item-result__items")
    #
    # results = []
    # for product in products[:limit]:
    #     try:
    #         title = product.select("div[data-sqe=name] > div > div")[0].text
    #         link = product.select("div[data-sqe=link]")[0]['href']
    #     except IndexError:
    #         continue
    #
    #     price = product.find(class_="_24JoLh")
    #     price = price.replace("Rp", "").replace(".", "")
    #     results.append(
    #         Product(
    #             name=title,
    #             link=link,
    #             price=int(price),
    #         )
    #     )
    #
    # return results

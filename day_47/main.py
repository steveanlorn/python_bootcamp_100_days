import os
import smtplib

import requests
from bs4 import BeautifulSoup

EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
EMAIL_PASSWORD = os.environ.get("EMAIL_PWD")

BUY_PRICE = 7000000

PRODUCT_LINK = "https://www.tokopedia.com/philips-estore/philips-air-purifier-3000i-series-ac3033-10"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/14.0.3 Safari/605.1.15 "
}

response = requests.get(PRODUCT_LINK, headers=header)
response.raise_for_status()
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

title_tag = soup.find('h1')
price_tag = soup.find(class_='price')
stock_tag = soup.select('#pdpFloatingActions p[data-testid=stock-label] b')

if title_tag is not None and price_tag is not None and len(stock_tag) > 0:
    current_price = price_tag.text
    product_title = title_tag.text
    stock = stock_tag[0].text

    current_price = current_price.replace("Rp", "").replace(".", "")
    print("price: ", current_price)
    print("title: ", product_title)
    print("stock: ", stock)

    if BUY_PRICE <= int(current_price) and int(stock) > 0:
        print("Sending email to ", EMAIL_TO)
        message = f"{product_title} is now {price_tag.text}"

        email_connection = smtplib.SMTP("smtp.gmail.com")
        email_connection.starttls()
        email_connection.login(user=EMAIL_FROM, password=EMAIL_PASSWORD)

        email_connection.sendmail(
            from_addr=EMAIL_FROM,
            to_addrs=EMAIL_TO,
            msg=f"Subject:Tokopedia Price Alert!\n\n{message}\n{PRODUCT_LINK}"
        )

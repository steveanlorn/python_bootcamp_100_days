from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

SEARCH_TERM = input('Enter search term: ')

chrome_driver_path = ''

driver = webdriver.Chrome(chrome_driver_path)

products = {}

# TOKOPEDIA
driver.get(f"https://www.tokopedia.com/search?st=product&q={SEARCH_TERM}")
time.sleep(2)
try:
    tokopedia_product = driver.find_element_by_css_selector('div[data-ssr="contentProductsSRPSSR"] .unf-card')
    tokopedia_link = tokopedia_product.find_element_by_tag_name('a').get_attribute('href')
    tokopedia_name = tokopedia_product.find_element_by_css_selector('div[data-testid="spnSRPProdName"]').text
    tokopedia_price = tokopedia_product.find_element_by_css_selector('div[data-testid="spnSRPProdPrice"]').text
except NoSuchElementException:
    print("Product not found in Tokopedia")
else:
    products["tokopedia"] = {
        "name": tokopedia_name,
        "price": tokopedia_price,
        "link": tokopedia_link,
    }

# SHOPEE
driver.get(f"https://shopee.co.id/search?keyword={SEARCH_TERM}")
time.sleep(2)
try:
    shopee_product = driver.find_element_by_css_selector('.shopee-search-item-result__items .shopee-search-item-result__item')
    shopee_link = shopee_product.find_element_by_tag_name('a').get_attribute('href')
    shopee_name = shopee_product.find_element_by_css_selector('div[data-sqe="name"] > div > div').text
    shopee_price = shopee_product.find_element_by_css_selector('.WTFwws._1k2Ulw._5W0f35').text
except NoSuchElementException:
    print("Product not found in Shopee")
else:
    products["shopee"] = {
        "name": shopee_name,
        "price": shopee_price,
        "link": shopee_link,
    }

# LAZADA
driver.get(f"https://www.lazada.co.id/catalog/?q={SEARCH_TERM}")
time.sleep(2)
try:
    lazada_product = driver.find_element_by_css_selector('div[data-qa-locator="product-item"]')
    lazada_link = lazada_product.find_element_by_css_selector('.GridItem__title___8JShU a').get_attribute('href')
    lazada_name = lazada_product.find_element_by_css_selector('.GridItem__title___8JShU a').text
    lazada_price = lazada_product.find_element_by_css_selector('.GridItem__price___LY2Vk').text
except NoSuchElementException:
    print("Product not found in Lazada")
else:
    products["lazada"] = {
        "name": lazada_name,
        "price": lazada_price,
        "link": lazada_link,
    }

# # BLIBLI
# driver.get(f"https://www.blibli.com/cari/{SEARCH_TERM}")
# time.sleep(2)
# blibli_product = driver.find_element_by_css_selector('.product__item')
# blibli_link = blibli_product.find_element_by_tag_name('a').get_attribute('href')
# blibli_name = blibli_product.find_element_by_css_selector('.product__title').text
# blibli_price = blibli_product.find_element_by_css_selector('.product__body__price__display').text
#
# products["blibli"] = {
#     "name": blibli_name,
#     "price": blibli_price,
#     "link": blibli_link,
# }

driver.quit()

print("\nSearch Result:\n")
for shop, p in products.items():
    print(shop)
    print(p['name'])
    print(p['price'])
    print(p['link'])
    print('-------------------\n')


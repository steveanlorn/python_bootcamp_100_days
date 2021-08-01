""" --- CHALLENGE 4 ---
Cookie clicker game bot
https://orteil.dashnet.org/cookieclicker/
"""
import time

from selenium import webdriver

chrome_driver = ""

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url="https://orteil.dashnet.org/cookieclicker")

game_time = time.time() + 60 * 5

big_cookie = driver.find_element_by_id('bigCookie')

timeout = time.time() + 10

while time.time() < game_time:
    big_cookie.click()

    if time.time() > timeout:

        for i in range(10, 0, -1):
            try:
                driver.find_element_by_xpath(f'//*[@id="product{i}"]').click()
            except:
                pass

        timeout = time.time() + 10

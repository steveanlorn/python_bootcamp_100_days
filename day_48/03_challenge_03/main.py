""" --- CHALLENGE 3 ---
Fill in a form
and submit it
"""
import time

from selenium import webdriver

chrome_driver = ""

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url="https://steveanlorn.github.io/me")

email = "dummy.mail@mail.com"
name = "Steve Cool"
message = "This message generated from my code"

email_form = driver.find_element_by_id('exampleInputEmail1')
email_form.send_keys(email)

name_form = driver.find_element_by_id('name')
name_form.send_keys(name)

message_form = driver.find_element_by_id('exampleFormControlTextarea1')
message_form.send_keys(message)

time.sleep(2)

submit_button = driver.find_element_by_css_selector('.contact button[type="submit"]')
submit_button.submit()

time.sleep(3)
driver.quit()

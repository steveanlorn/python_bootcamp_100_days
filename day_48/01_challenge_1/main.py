""" --- CHALLENGE 1 ---
Get total article data from Wikipedia
and print it
"""

from selenium import webdriver

chrome_driver = ''

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

# article_count = driver.find_element_by_id('articlecount').find_element_by_tag_name('a')
article_count = driver.find_element_by_css_selector('#articlecount a[title="Special:Statistics"]').text

print(article_count)

driver.quit()

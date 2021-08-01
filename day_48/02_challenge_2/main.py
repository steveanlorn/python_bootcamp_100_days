""" --- CHALLENGE 2 ---
Scrap upcoming event data from https://www.python.org/
into dictionary with structure:
{
    0: {
        "date": "<event date>",
        "title": "<event title>",
    }
}
"""

from selenium import webdriver

chrome_driver = ""

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url="https://www.python.org/")

events_element = driver.find_elements_by_css_selector('.event-widget ul.menu li')

events = {}
for i, event in enumerate(events_element):
    date = event.find_element_by_tag_name('time').text
    title = event.find_element_by_tag_name('a').text

    events[i] = {
        'date': date,
        'title': title,
    }

print(events)

driver.quit()

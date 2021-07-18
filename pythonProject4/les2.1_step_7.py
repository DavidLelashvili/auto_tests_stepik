import math
from selenium import webdriver
import time

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    check = browser.find_element_by_id('robotCheckbox')
    check.click()
    radio = browser.find_element_by_css_selector('[value="robots"]')
    radio.click()
    button1 = browser.find_element_by_css_selector('[type="submit"]')
    button1.click()


finally:
    time.sleep(5)
    browser.quit()
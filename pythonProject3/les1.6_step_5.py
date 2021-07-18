import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
a = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    search_link = browser.find_element_by_link_text(a)
    search_link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("David")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Pasternak")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Saint-P")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.close()
    browser.quit()

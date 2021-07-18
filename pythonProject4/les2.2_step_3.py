import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    x = browser.find_element_by_id('num1')
    x = x.text
    x = int(x)
    y = browser.find_element_by_id('num2')
    y = y.text
    y = int(y)
    sum1 = x + y
    print(sum1)
    sum1 = str(sum1)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum1)
    time.sleep(2)
    button = browser.find_element_by_tag_name("button").click()


finally:
    time.sleep(5)
    browser.quit()

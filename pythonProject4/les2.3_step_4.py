from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button1.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)


finally:
    time.sleep(1)
    browser.quit()

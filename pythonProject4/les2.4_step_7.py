from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока значение цены не станет = 100. Селектор берется в скобки
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments [0].scrollIntoView(true);", x)
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
    browser.quit()

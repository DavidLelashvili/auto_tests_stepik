from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    fname = browser.find_element_by_name("firstname")
    fname.send_keys("David")
    lname = browser.find_element_by_name("lastname")
    lname.send_keys("Pasternak")
    email = browser.find_element_by_name("email")
    email.send_keys("мейл")

    file_btn = browser.find_element_by_css_selector('[type="file"]')
    file_btn.send_keys("C:\\Users\\user\\PycharmProjects\\pythonProject4\\les2.txt")
    # current_dir = os.path.abspath(os.path.dirname(__les2__))
    # file_path = os.path.join(current_dir, 'les2.txt')
    # element.send_keys(file_path)
    button1 = browser.find_element_by_css_selector('[type="submit"]')
    button1.click()


finally:
    time.sleep(5)
    browser.quit()
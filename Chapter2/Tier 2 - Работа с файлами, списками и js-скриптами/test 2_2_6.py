from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))

    answer_pole = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_pole)
    answer_pole.send_keys(y)
    
    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button_submit = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
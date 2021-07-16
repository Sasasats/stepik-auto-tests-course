from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  link = "http://suninjuly.github.io/math.html"
  browser = webdriver.Chrome()  
  browser.get(link)

  x_element = browser.find_element_by_id('input_value')
  x = x_element.text 
  y = calc(x)

  input_pole = browser.find_element_by_id('answer')
  input_pole.send_keys(y)

  robot_check_box = browser.find_element_by_id('robotCheckbox')
  robot_check_box.click()

  radiobutton = browser.find_element_by_id('robotsRule')
  radiobutton.click()

  button_submit = browser.find_element_by_css_selector('.btn')
  button_submit.click()

finally:
  time.sleep(10)
  browser.quit()
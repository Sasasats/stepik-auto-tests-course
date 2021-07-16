from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button_submit = browser.find_element_by_class_name('btn').click()

    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    input_answer = browser.find_element_by_id('answer').send_keys(y)

    button_submit = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(5)
    browser.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = 'http://suninjuly.github.io/selects1.html'

    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id('num1').text
    number2 = browser.find_element_by_id('num2').text
    summa = str(int(number1) + int(number2))

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(summa)

    button_submit = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()
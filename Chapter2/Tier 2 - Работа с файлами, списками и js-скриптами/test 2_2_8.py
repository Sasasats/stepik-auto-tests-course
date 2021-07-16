from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir, 'test.txt')

    input_first_name = browser.find_element_by_name('firstname').send_keys('Andrey')

    input_last_name = browser.find_element_by_name('lastname').send_keys('Sats')

    input_email = browser.find_element_by_name('email').send_keys('Email')

    button_add_file = browser.find_element_by_id('file').send_keys(file_path)

    button_submit = browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()
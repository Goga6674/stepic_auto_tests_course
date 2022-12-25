from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    # defintion function
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # open link
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find and klick button
    first_button = browser.find_element(By.TAG_NAME, "button")
    first_button.click()

    # accepting cofirm form
    alert = browser.switch_to.alert
    alert.accept()

    # find and rading variale x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    # input antswer calc
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # find and click button
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    #time to copyng cod in sec
    time.sleep(20)
    
    #colse browser
    browser.quit()

#free sting


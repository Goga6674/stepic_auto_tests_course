from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # open link
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # find and input name
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    # find and input last_name
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivanov")

    # find and input mail
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("exampl@mail.ru")

    # loading file 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "T118_D.py")
    element.send_keys(file_path)

    # scrol, find and click button
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    elements = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    #time to copyng cod in sec
    time.sleep(20)
    
    #colse browser
    browser.quit()

#free sting





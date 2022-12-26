from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# определение функции
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем значение переменной х
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    num_is = x_element.get_attribute("valuex")
    x = int(num_is)
    y = calc(x)

    # ищем и запоняем форму
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot".
    chek = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    chek.click()
    
    #Выбрать radiobutton "Robots rule!"
    radio_b = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_b.click()

    # Нажать на кнопку "Submit".
    submit = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

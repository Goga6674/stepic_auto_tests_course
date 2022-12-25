from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

# объявление функции расчёта
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# переход по ссылке

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# поиск значения х
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

# input calc
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

# скролим до конца страницы
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# поиск и постанова "галочки" checkbox
check_box = browser.find_element(By.ID, "robotCheckbox")
check_box.click()

# поиск и постанова "точки" radioButton
radio_b = browser.find_element(By.ID, "robotsRule")
radio_b.click()

# поиск и нажитие на кнопку отправки
button.click()

# Проверяем, что смогли зарегистрироваться
time.sleep(20)

# browser 0ff
browser.quit()

# free string


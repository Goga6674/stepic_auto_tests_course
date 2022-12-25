from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
browser = webdriver.Chrome()

# говорим WebDriver ждать все элементы в течение 12 секунд
# browser.implicitly_wait(12)

# объявление функции расчёта
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# open link
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# find and catch price == 100, clik "book" button

button = browser.find_element(By.CSS_SELECTOR, "#book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# поиск значения х
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

# input calc
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

# find and click button
submit = browser.find_element(By.CSS_SELECTOR, "#solve")
submit.click()

#time to copyng cod in sec
time.sleep(20)
 
#colse browser
browser.quit()

#free sting

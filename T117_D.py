from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# объявление функции расчёта
def calc(x, y):
    print(x, y)
    z = x + y
    return srt(z)

# поиск значения х
x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
x = x_element

# поиск значения y
y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
y = y_element

# find sum
sum1 = calc(x, y)

# поиск значения суммы в списке
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(sum1).click()

# поиск кнопки submit
x_element = browser.find_element(By.CSS_SELECTOR, ".btn")

# Проверяем, что смогли зарегистрироваться
time.sleep(20)

# browser 0ff
browser.quit()

# end line






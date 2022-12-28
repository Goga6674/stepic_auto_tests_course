from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Test_login_and_pass(unittest.TestCase):

    def test_login_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first ")
        input1.send_keys("First name")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Last name")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        input3.send_keys("mail@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
       
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'RegistrationFAILED_in_test1')
       
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_login_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first ")
        input1.send_keys("First name")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Last name")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        input3.send_keys("mail@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'RegistrationFAILED_in_test2')

        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()


# пустая строока

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class Test_h1_search(unittest.TestCase):
    def test_h1_search1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

        #Заполняем форму (только обязательные поля)
        input_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > input.first")
        input_name.send_keys("Ivan")
        input_lastname = browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > input.second")
        input_lastname.send_keys("Petrov")
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block > .third_class > input.third")
        input_email.send_keys("example@example.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Test_passed")

    def test_h1_search2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        #Заполняем форму (только обязательные поля)
        input_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > input.first")
        input_name.send_keys("Ivan")
        input_lastname = browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > input.second")
        input_lastname.send_keys("Petrov")
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block > .third_class > input.third")
        input_email.send_keys("example@example.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Test_passed") 

if __name__ == "__main__":
    unittest.main()

#Явное ожидание. Настройка ожидания задержки, пока элемент на сайте (цена) не станет равным элементу, который ищет (ждет) пользователь

import time
import math
#Математическая функция которая считает значение переменной и возвращает результат в строку
def calc(x):
        return math.log(abs(12*math.sin(int(x))))

from selenium import webdriver
from selenium.webdriver.common.by import By
#импортируем класс WebdriverWait
from selenium.webdriver.support.ui import WebDriverWait
#импортируем инструмент для работы с ожиданиями
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока сумма не уменьшится до 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))

    button1 = browser.find_element(By.CSS_SELECTOR, '#book')
    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, '#solve')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

import os
import time
from doctest import Example
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

"""Работа с куками"""
driver.get("https://www.freeconferencecall.com/en/us/login")

"""Добовление куки"""
driver.add_cookie({"name": "Example",
                   "value": "Kukushka"})

"""Получение куки"""
before = driver.get_cookie("Example")

"""Удаление куки"""
driver.delete_cookie("Exemple")

"""Получение всех куки"""
driver.get_cookies()

"""Удаление всех куки"""
driver.delete_all_cookies()

"""Логин ввод пароля логина и клик по кнопки"""
LOGIN_FIELD = ("xpath", "//input[@id='login_email")
PASSWORD_FIELD = ("xpath", "//input[@id='password")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit")

driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(*LOGIN_FIELD).send_keys("Dimasur@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()

"""что сохраняем, куда сохраняем, операция wb"""
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))

"""Использование сохраненый куки"""
driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

"""Всплывающее окно алертов"""
driver.get("https://demoqa.com/alerts")

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1))

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.accept()      """Принятие алерта"""

print(alert.text)       """Получение надписи Алерта"""

alert.dismiss()     """Отмена алерта"""

alert.send_keys("Hello World")      """Ввод текста в алерт"""

time.sleep(3)
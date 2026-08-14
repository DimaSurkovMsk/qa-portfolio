from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

ENABLE_IN_SECONDS = ("xpath", "//button[@id='enableAfter']")
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
REMOVE_BUTTON = ("xpath", "//button[@id='Remove']")

ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
TEXT_FIELD = ("xpath", "//input[@type='text']")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))


"""Кнопка которая появляется на сайте через определенное время"""
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

"""Кнопка которая станет кликаюельна через какое то время"""
wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS)).click()

"""кнопка которая исчезнет и мы ожидаем это"""
driver.find_element(*REMOVE_BUTTON)
wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""Переключение между окнами"""
#
# options = Options()
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(options=options)
#
# FOR_BUSINES_BUTTON_LOCATOR = ("xpath", "(//a[text()=' For Business '])")
# START_FREE_BUTTON_LOCATOR = ("xpath", "(//a[text()='Start for Free'])")
#
# driver.get("https://hyperskill.org/tracks")
# time.sleep(3)
#
# driver.find_element(*FOR_BUSINES_BUTTON_LOCATOR).click()
# time.sleep(3)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
# time.sleep(3)

"""Переключение между окнами"""
# options = Options()
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(options=options)
#
# # FOR_BUSINES_BUTTON_LOCATOR = ("xpath", "(//a[text()=' For Business '])")
# # START_FREE_BUTTON_LOCATOR = ("xpath", "(//a[text()='Start for Free'])")
#
# driver.get("https://hyperskill.org/tracks")
# time.sleep(5)
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# driver.get("https://ya.ru")
# time.sleep(5)

"""Переключение между окнами"""
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.switch_to.new_window("tab")
time.sleep(3)

driver.get("https://ya.ru")
time.sleep(3)


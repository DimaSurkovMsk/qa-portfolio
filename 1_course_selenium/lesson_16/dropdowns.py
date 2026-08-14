import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

"""Выбор выпадающих значений"""
# SELECT_LOCATOR = ("xpath", "(//select[@id='dropdown'])")
#
# driver.get("https://the-internet.herokuapp.com/dropdown")
#
# DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
# time.sleep(3)
# """Выбор по тексту"""
# DROPDOWN.select_by_visible_text("Option 1")
# """Выбор по значению"""
# DROPDOWN.select_by_value("2")
# """Выбор по индексу"""
# DROPDOWN.select_by_index(1)
# time.sleep(3)

"""Перебор выпадающий значений"""
SELECT_LOCATOR = ("xpath", "(//select[@id='dropdown'])")
driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

"""Перебор по тексту"""
# ALL_OPTIONS = DROPDOWN.options
#
# for option in ALL_OPTIONS:
#     time.sleep(1)
#     if "Option 2" in option.text:
#         print("Опция присутствует")
#    DROPDOWN.select_by_visible_text(option.text)

# """Перебор по индексу"""
# ALL_OPTIONS = DROPDOWN.options
#
# for option in ALL_OPTIONS:
#     time.sleep(1)
#     DROPDOWN.select_by_index(ALL_OPTIONS.index(option))

"""Перебор по value"""
ALL_OPTIONS = DROPDOWN.options

for option in ALL_OPTIONS:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))





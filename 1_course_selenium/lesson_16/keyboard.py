import time

from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
driver = webdriver.Chrome()

"""ВВод с клавиатуры выделение и удаление в строке"""
# KEYBOARD_INPUT = ("xpath", "//input[@id='target']")
# driver.get("https://the-internet.herokuapp.com/key_presses")
# time.sleep(3)
# driver.find_element(*KEYBOARD_INPUT).send_keys("AAAAAAAAAAA")
# time.sleep(3)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + "A")
# time.sleep(3)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
# time.sleep(3)

"""Выбор значение с выпадающего списка и выбор"""
# SELECT_LOCATOR_1 = ("xpath", "//input[@id='react-select-3-input']")
#
# driver.get("https://demoqa.com/select-menu")
#
# time.sleep(1)
#
# driver.find_element(*SELECT_LOCATOR_1).send_keys("Ms.")
# driver.find_element(*SELECT_LOCATOR_1).send_keys(Keys.ENTER)
#
# time.sleep(5)

"""Выбор значение с выпадающего списка и выбор 2 вариант"""
# SELECT_ONE = ("xpath", "//div[@id='selectOne']")
# PROF_OPTION = ("xpath", "//div[text()='Prof.']")
# driver.get("https://demoqa.com/select-menu")
#
# time.sleep(3)
#
# driver.find_element(*SELECT_ONE).click()
# time.sleep(3)
#
# driver.find_element(*PROF_OPTION).click()
#
# time.sleep(3)

"""Выбор  мульти-селекта + TAB Довершает слово"""
MULTY_SELECT = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")
time.sleep(3)

driver.find_element(*MULTY_SELECT).send_keys("Gre")
time.sleep(3)

driver.find_element(*MULTY_SELECT).send_keys(Keys.TAB)
time.sleep(3)

driver.find_element(*MULTY_SELECT).send_keys("Bla")
time.sleep(3)

driver.find_element(*MULTY_SELECT).send_keys(Keys.TAB)
time.sleep(3)


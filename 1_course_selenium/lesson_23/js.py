import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

"""Скролл страницы"""
driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get("https://seiyria.com/bootstrap-slider/")

EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
EX_2 = driver.find_element(*EX_2_LOCATOR)

scrolls.scroll_to_element(EX_2)

time.sleep(5)
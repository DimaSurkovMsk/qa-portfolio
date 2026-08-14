import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# """Перетягивания из зона в зону"""
# driver =webdriver.Chrome()
# action_1 = ActionChains(driver)
#
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# COLLUM_A = ("xpath", "//div[@id='column-a']")
# COLLUM_B = ("xpath", "//div[@id='column-b']")
#
# A = driver.find_element(*COLLUM_A)
# B = driver.find_element(*COLLUM_B)
#
# time.sleep(2)
#
# action_1.drag_and_drop(A, B).perform()
# time.sleep(2)
"""Перетягивания из зона в зону с удержанием итема и ожиданием появление окна"""
driver =webdriver.Chrome()
action_1 = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDE_BAR = ("xpath", "(//div[@class='drop-area__item'])[3]")

action_1.click_and_hold(driver.find_element(*ITEM))\
    .pause(1.5)\
    .move_to_element(driver.find_element(*SIDE_BAR))\
    .release()\
    .perform()
time.sleep(5)

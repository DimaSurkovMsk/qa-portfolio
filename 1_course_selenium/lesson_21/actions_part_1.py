import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_CLICK = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK = ("xpath", "//button[@id='rightClick']")
COLOR_BUTTON = ("xpath", "//button[@id='colorChangeOnHover']")
MENU_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
SUB_LIST_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")

""" Клик МЫШКОЙ"""
# driver.get("https://testkru.com/Elements/Buttons")
# #
# left_button = driver.find_element(*LEFT_CLICK)
# # time.sleep(3)
# #
# # action.click(left_button).perform()
# # time.sleep(3)
#
""" Двойной клик МЫШКОЙ"""
# # driver.get("https://testkru.com/Elements/Buttons")
# #
# double_button = driver.find_element(*DOUBLE_CLICK)
# # time.sleep(3)
# #
# # action.double_click(double_button).perform()
# # time.sleep(3)
#
""" Клик правой конпокй мышы"""
# # driver.get("https://testkru.com/Elements/Buttons")
# #
# right_button = driver.find_element(*RIGHT_CLICK)
# # time.sleep(3)
# #
# # action.context_click(right_button).perform()
# # time.sleep(3)
#
"""Очередь нажатий"""
# #driver.get("https://testkru.com/Elements/Buttons")
#
# time.sleep(3)
#
# action.click(left_button)\
# .pause(2)\
# .double_click(double_button)\
# .pause(2)\
# .context_click(right_button)\
# .perform()
# time.sleep(3)

# """Наведение на элемент"""
# driver.get("https://testkru.com/Elements/Buttons")
# #
# color_button = driver.find_element(*COLOR_BUTTON)
# time.sleep(3)
# #
# action.move_to_element(color_button).perform()
# time.sleep(3)

"""Открытие Шторки"""
driver.get("https://demoqa.com/menu")
#
menu_item_1 = driver.find_element(*MENU_LOCATOR)
sub_list = driver.find_element(*SUB_LIST_LOCATOR)
time.sleep(3)

action.move_to_element(menu_item_1)\
    .pause(2)\
    .move_to_element(sub_list)\
    .perform()
time.sleep(3)




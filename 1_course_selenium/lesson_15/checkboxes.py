import time

from selenium import webdriver


driver = webdriver.Chrome()

#CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")

"""Получение статуса и проставление чек бокса"""
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# time.sleep(3)
# print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# time.sleep(3)

"""Специальный метод для проставление и получение статуса"""
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# print(driver.find_element(*CHECKBOX_1).is_selected())
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).is_selected())
# time.sleep(3)

"""Перекрытый чекбокс"""
# CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']")
# CHECKBOX_HOME_ACTION = ("xpath", "//span[@class='rct-checkbox']")
#
# driver.get("https://demoqa.com/checkbox")
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
# driver.find_element(*CHECKBOX_HOME_ACTION).click()
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
# time.sleep(3)

""""""
# ELEMENT_ONE = ("xpath", "//li[text()='Cras justo odio']")
#
# driver.get("https://demoqa.com/selectable")
# before_1 = driver.find_element(*ELEMENT_ONE).get_attribute("class")
# print(before_1)
# driver.find_element(*ELEMENT_ONE).click()
# after = driver.find_element(*ELEMENT_ONE).get_attribute("class")
# assert "active" in after
#
# time.sleep(3)


"""Радио баттон"""
YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_ACTION = ("xpath", "//label[@for='yesRadio']")
NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO_ACTION = ("xpath", "//label[@for='noRadio']")

driver.get("https://demoqa.com/radio-button")
print(driver.find_element(*YES_RADIO_STATUS).is_selected())
driver.find_element(*YES_RADIO_ACTION).click()
print(driver.find_element(*YES_RADIO_STATUS).is_selected())

"""Запрос на взаимодействие"""
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
time.sleep(3)

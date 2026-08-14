import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""Переключение АЙФРЕЙМОВ и посик на странице айфреймов"""
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
# COPY_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")
# IFRAME_LOCATOR = ("xpath", "//iframe")
#
#
# driver.get("https://testautomationpractice.blogspot.com/")
# iframe = driver.find_element(*IFRAME_LOCATOR)
# driver.switch_to.frame(iframe)
#
# time.sleep(3)
# driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys("Dmitrii")
# time.sleep(3)
#
# driver.switch_to.default_content()
#
# driver.find_element(*COPY_TEXT_LOCATOR).click()
# time.sleep(3)
"""Переключение по айфремов"""
driver.get("https://demoqa.com/nestedframes")

driver.switch_to.frame("frame1")

print(driver.find_element("xpath", "//body").text)

driver.switch_to.frame(0)
print(driver.find_element("xpath", "//body").text)

driver.switch_to.parent_frame()
print(driver.find_element("xpath", "//body").text)

driver.switch_to.default_content()
import time

from selenium import webdriver
"""Запуск расширений"""
options = webdriver.ChromeOptions()
options.add_extension("""Названия файла который надо вставить """)

driver = webdriver.Chrome(options=options)
driver.get("https://ya.ru")
time.sleep(10)
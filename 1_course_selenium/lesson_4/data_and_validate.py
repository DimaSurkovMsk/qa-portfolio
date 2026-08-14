import time

from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url
print("URL Старницы:", url)
assert url == "https://www.wikipedia.org/", "Ошибка в URl, открыта не та страница"

current_titel = driver.title
print("Текущий заголовок:", current_titel)
assert current_titel == "Wikipedia", "Не корректный заголовок станицы"

print(driver.page_source)
time.sleep(3)
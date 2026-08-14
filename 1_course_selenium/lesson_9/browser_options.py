import time
from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager" # - только дом "normal" - загружает все
#chrome_options.add_argument("--headless")#тест не открывая браузер
chrome_options.add_argument("--incognito")# тест инкогнито
chrome_options.add_argument("--ignore-certificate-errors") #тест с просроченым сертификатом CCЛ
chrome_options.add_argument("--window-size=700,1080") #размер окна
chrome_options.add_argument("--disable-cache")# нет записи кэша
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()

driver.get("https://whatismyipaddress.com/")

end_time = time.time()
result = end_time - start_time
print(result)

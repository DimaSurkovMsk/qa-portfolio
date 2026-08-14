from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()

# 1. Открываем страницу задания
browser.get("https://suninjuly.github.io/redirect_accept.html")

# Запоминаем текущую вкладку
old_window = browser.current_window_handle

# 2. Нажимаем кнопку
browser.find_element(By.CSS_SELECTOR, "button").click()

# 3. Переключаемся на новую вкладку
time.sleep(1)

new_window = [window for window in browser.window_handles
              if window != old_window][0]

browser.switch_to.window(new_window)

# 4. Получаем x
x = int(browser.find_element(By.ID, "input_value").text)
print("x =", x)

# Решаем ln(abs(12 * sin(x)))
y = math.log(abs(12 * math.sin(x)))
print("y =", y)

# Вводим ответ
browser.find_element(By.ID, "answer").send_keys(str(y))

# Нажимаем кнопку
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)
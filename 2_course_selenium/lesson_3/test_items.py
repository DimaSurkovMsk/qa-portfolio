import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button_works(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )

    wait = WebDriverWait(browser, 30)

    # Ждём появления кнопки
    button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".btn-add-to-basket")
        )
    )

    # Прокручиваем к кнопке
    browser.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        button
    )

    # Нажимаем
    button.click()

    # Ждём изменения страницы после добавления
    time.sleep(2)

    print("Кнопка «Добавить в корзину» нажата")

    # Проверяем, что появилось сообщение об успешном добавлении
    success_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")
        )
    )

    print(f"Сообщение: {success_message.text}")

    assert success_message.is_displayed()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path=r"C:\Users\Win10_Game_OS\Desktop\selenium\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_firstname = browser.find_element(By.CLASS_NAME, 'form-control.first')
    input_firstname.send_keys('Ostap')

    input_secondname = browser.find_element(By.CLASS_NAME, 'form-control.second')
    input_secondname.send_keys('Zub')

    input_mail = browser.find_element(By.CLASS_NAME, 'form-control.third')
    input_mail.send_keys('mail@dot.com')

    #input_phone = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
    #input_phone.send_keys('888888888888')

    #input_address = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    #input_address.send_keys('Odesa')


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

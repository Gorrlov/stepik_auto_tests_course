from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/redirect_accept.html" 
    browser = webdriver.Chrome()
    browser.get(link)


    # нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()   

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(x)   

    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control:required")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click() 



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from  data import Account


class TestLogOutAccount:

    def test_Log_out_account_using_the_log_out_button_in_personal_account(self, driver): # выход по кнопке «Выйти» в личном кабинете
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Account.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Account.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text
        expected_texts = {'LOGIN_BUTTON': 'Войти'}
        assert text == expected_texts['LOGIN_BUTTON'] # кнопка Войти на форме авторизации после выхода из аккаунта

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from  data import Account


class TestlogInToYourAccount:

    def test_log_in_using_the_log_in_to_account_button(self, driver): # вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Account.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Account.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.PLACE_ORDER_BUTTON)).text
        expected_texts = {'PLACE_ORDER_BUTTON': 'Оформить заказ'}
        assert text == expected_texts['PLACE_ORDER_BUTTON'] # кнопка 'Оформить заказ' доступна только зарегистрированному пользователю

    def test_log_in_using_the_personal_account_button(self, driver): # вход через кнопку «Личный кабинет»
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Account.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Account.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.PLACE_ORDER_BUTTON)).text
        expected_texts = {'PLACE_ORDER_BUTTON': 'Оформить заказ'}
        assert text == expected_texts['PLACE_ORDER_BUTTON'] # кнопка 'Оформить заказ' доступна только зарегистрированному пользователю

    def test_log_in_via_the_button_in_the_registration_form(self, driver): # вход через кнопку в форме регистрации
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_SECTION))
        driver.find_element(*Locators.REGISTER_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.LOGIN_LINKS).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Account.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Account.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.PLACE_ORDER_BUTTON)).text
        expected_texts = {'PLACE_ORDER_BUTTON': 'Оформить заказ'}
        assert text == expected_texts['PLACE_ORDER_BUTTON'] # кнопка 'Оформить заказ' доступна только зарегистрированному пользователю

    def test_login_via_a_button_in_the_password_recovery_form(self, driver): # вход через кнопку в форме восстановления пароля
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_SECTION))
        driver.find_element(*Locators.RESTORE_PASSWORD_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_LINKS))
        driver.find_element(*Locators.LOGIN_LINKS).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Account.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Account.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.PLACE_ORDER_BUTTON)).text
        expected_texts = {'PLACE_ORDER_BUTTON': 'Оформить заказ'}
        assert text == expected_texts['PLACE_ORDER_BUTTON'] # кнопка 'Оформить заказ' доступна только зарегистрированному пользователю

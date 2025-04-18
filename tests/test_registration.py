from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data
from locators import Locators


class TestRegistrationWithNewData:

    def test_success_registration(self, driver):

        name, email, password = generate_registration_data()
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_SECTION))
        driver.find_element(*Locators.REGISTER_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_FIELD_AUTH).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                                         (Locators.PLACE_ORDER_BUTTON)).text
        assert text == 'Оформить заказ' # кнопка 'Оформить заказ' доступна только зарегистрированному пользователю

    def test_invalid_password_error(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_SECTION))
        driver.find_element(*Locators.REGISTER_SECTION).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('1')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.ERROR_PASSWORD)).text
        assert text == 'Некорректный пароль'
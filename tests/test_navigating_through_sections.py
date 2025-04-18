from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestNavigatingThroughSections:

    def test_click_through_to_the_personal_account(self, driver): # переход по клику на 'Личный кабинет'
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text
        expected_texts = {'LOGIN_BUTTON': 'Войти'}
        assert text == expected_texts['LOGIN_BUTTON'] # кнопка Войти на форме авторизации в разделе 'Личный кабинет'

    def test_click_through_to_the_constructor(self, driver): # переход из личного кабинета в Конструктор
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_SECTION))
        driver.find_element(*Locators.CONSTRUCTOR_SECTION).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.SAUCES_SECTION)).text
        expected_texts = {'SAUCES_SECTION': 'Соусы'}
        assert text == expected_texts['SAUCES_SECTION'] # подраздел Соусы в разделе Конструктор

    def test_click_on_the_stellar_burgers_logo(self, driver): # переход из личного кабинета в Конструктор по клику на логотип Stellar Burgers
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.STELLAR_BURGERS_LOGO))
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.SAUCES_SECTION)).text
        expected_texts = {'SAUCES_SECTION': 'Соусы'}
        assert text == expected_texts['SAUCES_SECTION']  # подраздел Соусы в разделе Конструктор

    def test_go_to_the_rolls_section(self, driver): # переход в раздел Булки
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.ROLLS_SECTION).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.ROLLS)).text
        expected_texts = {'ROLLS': 'Флюоресцентная булка R2-D3'}
        assert text == expected_texts['ROLLS'] # название булки доступной только в разделе Булки

    def test_go_to_the_sauces_section(self, driver): # переход в раздел Соусы
        driver.find_element(*Locators.SAUCES_SECTION).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.SAUCES)).text
        expected_texts = {'SAUCES': 'Соус с шипами Антарианского плоскоходца'}
        assert text == expected_texts['SAUCES']  # название соуса доступного только в разделе Соусы

    def test_go_to_the_filling_section(self, driver): # переход в раздел Начинки
        driver.find_element(*Locators.FILLING_SECTION).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.FILLING)).text
        expected_texts = {'FILLING': 'Филе Люминесцентного тетраодонтимформа'}
        assert text == expected_texts['FILLING']  # название начинки доступной только в разделе Начинки
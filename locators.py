from selenium.webdriver.common.by import By


class Locators:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" # кнопка 'Личный кабинет'
    SIGN_ACCOUNT_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]' # кнопка 'Войти в аккаунт'
    REGISTER_BUTTON = By.XPATH, '//button[text()="Зарегистрироваться"]' # кнопка 'Зарегистрироваться'
    RESTORE_BUTTON = By.XPATH, "//button[text()='Восстановить']" # кнопка 'Восстановить'
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]' # кнопка 'Войти'
    NAME_FIELD = By.XPATH, '//div[label[contains(text(),"Имя")]]//input' # поле 'имя'
    EMAIL_FIELD = By.XPATH, '//div[label[contains(text(),"Email")]]//input' # поле 'email'
    PASSWORD_FIELD = By.XPATH, '//input[@name="Пароль"]' # поле 'пароль'
    REGISTER_SECTION = By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Зарегистрироваться"]' # раздел 'зарегистрироваться'
    RESTORE_PASSWORD_SECTION = By.XPATH, '//a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]' # раздел 'восстановить пароль'
    CONSTRUCTOR_SECTION = By.XPATH, '//p[text()="Конструктор"]' # раздел 'Конструктор'
    STELLAR_BURGERS_LOGO = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a' # переход по логотипу 'Stellar Burgers'
    ROLLS_SECTION = By.XPATH, '//span[text()="Булки"]' # раздел 'Булки'
    SAUCES_SECTION = By.XPATH, '//span[text()="Соусы"]' # раздел 'Соусы'
    FILLING_SECTION = By.XPATH, '//span[text()="Начинки"]' # раздел 'Начинки'
    EXIT_BUTTON = By.XPATH, '// button[text() = "Выход"]' # кнопка 'Выход' из личного кабинета
    ERROR_PASSWORD = By.XPATH, '// p[@class ="input__error text_type_main-default"]' # ошибка 'Некорректный пароль'
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]' # кнопка 'Сохранить' в личном кабинете
    PLACE_ORDER_BUTTON = By.XPATH, '// button[text() = "Оформить заказ"]' # кнопка 'Оформить заказ'
    LOGIN_LINKS = By.XPATH, '//a[@class ="Auth_link__1fOlj"]' # ссылка 'Войти'
    ROLLS = By.XPATH, '//p[text() = "Флюоресцентная булка R2-D3"]' # булка доступная в разделе Булки
    SAUCES = By.XPATH, '//p[text() = "Соус с шипами Антарианского плоскоходца"]' # соус доступный в разделе Соусы
    FILLING = By.XPATH, '//p[text() = "Филе Люминесцентного тетраодонтимформа"]' # начинка доступная в разделе Начинки

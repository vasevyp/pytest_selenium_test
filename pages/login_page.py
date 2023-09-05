from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class MyLogin(Base):
    url = 'https://doma-hleb.ru/'
    login_test = 'vasevyp@yandex.ru'
    password_test = 'mytestshop'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Auth Locators

    authorization = '//*[@id="header_wrap"]/div[1]/div/div[2]/ul/li[5]/a/span'

    my_login = '//input[@id="login_email"]'
    my_password = '//input[@id="login_pass"]'

    commit_button = '//button[@id="btn_login"]'

    # Getters

    def get_auth(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.authorization)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.my_login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.my_password)))

    def get_commit(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.commit_button)))

    def get_x_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.x_button)))

    # Actions

    def click_mylogin(self):
        self.get_auth().click()
        print('Click Open click_Authorization')

    def input_login(self, login):
        self.get_login().send_keys(login)
        print('Input Login')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input Password')

    def click_commit(self):
        self.get_commit().click()
        print('Click Commit Button')

    def click_x_button(self):
        self.get_x_button().click()
        print('Click x_button Button')

    # Methods

    def my_authorization(self):
        # метод, который открывает url
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        # методы авторизации, вход в личный кабинет
        self.click_mylogin()
        self.input_login(self.login_test)
        self.input_password(self.password_test)
        self.click_commit()
        self.get_current_url()
        time.sleep(2)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
import time


class MyCompleat(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Finish Locators

    account = '//*[@id="header_wrap"]/div[1]/div/div[2]/ul/li[5]/a/span'
    cart = '//*[@id="header_wrap"]/div[3]/div/nav/ul/li[6]/div/div/a'
    clear_cart = '//*[@id="checkout_left"]/div/a/span'
    a = '//*[@id="header_wrap"]/div[2]/div/a'
    exit_account = '//*[@id="header_wrap"]/div[1]/div/div[2]/ul/li[6]/a/span'
    thanks_word = '//*[@id="all_page"]/div/div[2]/div/div/div/div'

    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_account(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.account)))

    def get_clear_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.clear_cart)))

    def get_a(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.a)))

    def get_exit(self):
        return WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, self.exit_account)))

    def get_thanks_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.thanks_word)))

    # Actions

    def click_cart(self):
        self.get_cart().click()
        print('Click Cart')

    def click_account(self):
        self.get_account().click()
        print('Click Account')

    def click_clear_cart(self):
        self.get_clear_cart().click()
        print('Click clear Cart')

    def click_a(self):
        self.get_a().click()
        print('Click clear')

    def click_exit(self):
        self.get_exit().click()
        print('Click Exit Account')

     # Methods

    def select_compleat(self):

        self.click_account()
        self.click_cart()
        # time.sleep(1)
        self.click_clear_cart()
        time.sleep(1)
        # Прокручиваем страницу вверх на 500 пикселей
        self.driver.execute_script("window.scrollTo(0, -500);")
        self.click_exit()
        self.assert_word(self.get_thanks_word(),
                         'Спасибо, что посетили наш магазин!')
        # try:
        # ....
        # except TimeoutException as e:
        #     print('click_exite  - Not done!!!\n', e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time


class MyCompleat(Base):

    # Finish Locators

    account = '//*[@id="header_wrap"]/div[1]/div/div[2]/ul/li[5]/a/span'

    cart = '//*[@id="header_wrap"]/div[3]/div/nav/ul/li[6]/div/div/a'
    clear_cart = '//*[@id="checkout_left"]/div/a/span'

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

    def click_exit(self):
        self.get_exit().click()
        print('Click Exit Account')

     # Methods

    def select_compleat(self):
        self.click_account()
        self.click_cart()
        self.click_clear_cart()
        time.sleep(1)
        # Прокручиваем страницу вверх на 500 пикселей
        self.driver.execute_script("window.scrollTo(0, -500);")
        self.click_exit()
        self.assert_word(self.get_thanks_word(),
                         'Спасибо, что посетили наш магазин!')
        self.assert_url('https://doma-hleb.ru/logoff.php?logout=1')

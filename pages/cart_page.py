from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
import time


class MyCart(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Cart Locators

    cart = '//*[@id="header_wrap"]/div[3]/div/nav/ul/li[6]/div/div/a'
    cart_word = '//*[@id="cart_page_ajax"]/h1'
    checkout = '//*[@id="checkout_right"]/div/a'

    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_checkout(self):
        return WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout)))

    # Actions

    def click_cart(self):
        self.get_cart().click()
        print('Click Cart')

    def click_checkout(self):
        self.get_checkout().click()
        print('Click Checkout Cart')

     # Methods

    def select_cart(self):

        self.click_cart()
        self.assert_word(self.get_cart_word(), 'В корзине 3 товара')
        self.do_screenshot()
        self.click_checkout()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
import time


class MyOrder(Base):
    comment_text = 'Я выполняю тестовое задание по тестированию бизнес пути покупки товаров на этом сайте.'

    # Order Locators
    # Почта России, радио кнопка
    post = '//*[@id="shipping_options"]/div[3]/label'
    comment = '//textarea[@id="comments"]'
    order = '//*[@id="checkout_right"]/div/button'

    # Getters

    def get_order(self):
        return WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, self.order)))

    def get_post(self):
        return WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, self.post)))

    def get_comment(self):
        return WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, self.comment)))

    # Actions

    def click_order(self):
        self.get_order().click()
        print('Click Order')

    def click_post(self):
        self.get_post().click()
        print('Click PochtaRossii radio button')

    def input_comment(self, text):
        self.get_comment().send_keys(text)
        print('Input Comment')

     # Methods

    def send_order(self):
        self.click_post()
        self.input_comment(self.comment_text)
        time.sleep(3)
        self.click_order()
        self.get_current_url()

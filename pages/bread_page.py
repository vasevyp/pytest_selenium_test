from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.base_class import Base
import time


class MyGoods(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Goodss Locators
    catalog = '//*[@id="header_wrap"]/div[3]/div/nav/ul/li[2]/a'
    first_word = '//*[@id="all_page"]/div/div[2]/div/div/h1'
    baking_mixes = '//*[@id="all_page"]/div/div[2]/div/div/div/div/ul/li[2]/div/a/span'
    baking_mixes_product = '//*[@id="ajax_content_catalog"]/div[2]/div[1]/div/div[5]/a/span'
    droggy = '//*[@id="all_page"]/div/div[2]/div/div/div/div/ul/li[3]/div/a/span'
    droggy_product = '//*[@id="ajax_content_catalog"]/div[2]/div[1]/div/div[5]/a/span'
    flour = '//*[@id="all_page"]/div/div[2]/div/div/div/div/ul/li[1]/div/a/span'
    # Мука амарантовая "Масляный Король"  300г
    flour_product = '//*[@id="ajax_content_catalog"]/div[2]/div[1]/div/div[5]/a/span'
    addto_cart = '//button[@id="add_to_cart"]'

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_first_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_word)))

    def get_flour_list(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.flour)))

    def get_baking_mixes_list(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.baking_mixes)))

    def get_droggy_list(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.droggy)))

    def get_flour_product(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.flour_product)))

    def get_baking_mixes_product(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.baking_mixes_product)))

    def get_droggy_product(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.droggy_product)))

    def get_addto_cart(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.addto_cart)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print('Click Open Catalog')

    def click_flour_list(self):
        self.get_flour_list().click()
        print('Click Open flour list')

    def click_baking_mixes_list(self):
        self.get_baking_mixes_list().click()
        print('Click Open baking_mixes list')

    def click_droggy_list(self):
        self.get_droggy_list().click()
        print('Click Open droggy list')

    def click_flour_product(self):
        self.get_flour_product().click()
        print('Click Flour_product')

    def click_baking_mixes_product(self):
        self.get_baking_mixes_product().click()
        print('Click Baking mixes product')

    def click_droggy_product(self):
        self.get_droggy_product().click()
        print('Click Droggy product')

    def click_addto_cart(self):
        self.get_addto_cart().click()
        print('Click Button add to cart')

     # Methods

    def select_goods(self):
        self.click_catalog()
        self.get_current_url()
        self.assert_word(self.get_first_word(), 'Каталог товаров')
        self.click_baking_mixes_list()
        self.click_baking_mixes_product()
        self.click_addto_cart()
        time.sleep(3)
        self.click_catalog()
        self.click_droggy_list()
        self.click_droggy_product()
        self.click_addto_cart()
        time.sleep(3)
        self.click_catalog()
        self.click_flour_list()
        time.sleep(3)
        self.click_flour_product()
        self.click_addto_cart()
        time.sleep(3)

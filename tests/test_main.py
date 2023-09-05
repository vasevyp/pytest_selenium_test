from pages.login_page import MyLogin
from pages.bread_page import MyGoods
from pages.cart_page import MyCart
from pages.order_page import MyOrder
from pages.finish_page import MyCompleat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_choice_goods():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    # driver = webdriver.Firefox(
    #     service=FirefoxService(GeckoDriverManager().install()))

    print('Start AutoTest')

    auth = MyLogin(driver)
    auth.my_authorization()

    goods = MyGoods(driver)
    goods.select_goods()

    cart = MyCart(driver)
    cart.select_cart()

    order = MyOrder(driver)
    order.send_order()

    compleat = MyCompleat(driver)
    compleat.select_compleat()

    print('Test Success!!')

    # time.sleep(20)
    # driver.quit()

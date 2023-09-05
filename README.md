# Тестовый проект по тестированию сайта https://doma-hleb.ru/ с использованием pytest.

## 1. Структура проекта

    PYTEST_TEST/
        /base/
            base_class.py
        /pages/
            bread_page.py
            cart_page.py
            finish_page.py
            login_page.py
            order_page.py
        /scrinshots/
        /tests/
            test_main.py

## 2. Порядок выполнения теста

1. Авторизация на сайте: ввести логин и пароль.

2. Открыть в меню "Каталог товаров".
   2.1 Выбрать подменю "Смеси для выпечки"
   2.2 Выбрать товар ""Чиабатта" пекарная смесь 500г".
   2.3 добавить товар ""Чиабатта" пекарная смесь 500г" в корзину.

3. Открыть в меню "Каталог товаров".
   3.1 Выбрать подменю "Дрожжи"
   3.2 Выбрать товар "Дрожжи "Saf-Instant" 500г".
   3.3 Добавить товар "Дрожжи "Saf-Instant" 500г" в корзину.

4. Открыть в меню "Каталог товаров".
   4.1 Выбрать подменю "Мука, отруби"
   4.2 Выбрать товар "Мука амарантовая "Масляный Король" 300г".
   4.3 добавить товар "Мука амарантовая "Масляный Король" 300гг" в корзину.

5. Переход в корзину покупателя
   5.1 Проверка текста "В корзине 3 товара"
   5.2 Выполнение скриншота в папку screenshots
   5.3 Нажимаем кнопку "Перейти к оформлению ->"

6. Переход на страницу заказа
   6.1 Выберите способ доставки: Почта России (радио кнопка)
   6.2 Комментарии к Вашему заказу: "Я выполняю тестовое задание по тестированию бизнес пути покупки товаров на этом сайте." (заносим комментарий в поле ввода комментария)
   6.3 Нажимаем кнопку "Оформить заказ"

7. Переход на страницу Подтверждение (заказа)
   7.1 На странице вся информация о заказе с кнопкой "Подтвердить Заказ" (не нажимаем)
   7.2 Кликаем на "Мой аккаунт", выходим со страницы подтверждения в свой Личный кабинет

8. Завершение тестирования
   8.1 Кликаем на кнопку "Корзина", заходим в корзину покупателя
   8.2 Кликаем на "Очистить корзину"
   8.2 Прокручиваем экран вниз, чтобы была доступна надпись "Выход"
   8.3 Кликаем на "Выход"
   8.4 Делаем проверку текста "Спасибо, что посетили наш магазин!", который появляется после выхода из аккаунта.

## 3. Результат тестирования

_tests/test_main.py::test_choice_goods Start AutoTest_

Current_url: https://doma-hleb.ru/

Click Open click_Authorization

Input Login

Input Password

Click Commit Button

Current_url: https://doma-hleb.ru/

Click Open Catalog

Current_url: https://doma-hleb.ru/catalog

Value word "Каталог товаров"- OK!

Click Open baking_mixes list

Click Baking mixes product

Click Button add to cart

Click Open Catalog

Click Open droggy list

Click Droggy product

Click Button add to cart

Click Open Catalog

Click Open flour list

Click Flour_product

Click Button add to cart

Click Cart

Value word "В корзине 3 товара"- OK!

Current_url: https://doma-hleb.ru/shopping_cart.php

Screenshot OK!

Click Checkout Cart

Click PochtaRossii radio button

Input Comment

Click Order

Current_url: https://doma-hleb.ru/sc_checkout_confirmation.php

Click Account

Click Cart

Click clear Cart

Click Exit Account

Value word "Спасибо, что посетили наш магазин!"- OK!

Test Success!!

PASSED

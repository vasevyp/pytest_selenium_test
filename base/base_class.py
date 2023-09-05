
'''Создаем базовый класс, в котором храним наш драйвер.
Далее можно создать здесь универсальные медоты, которые можно вызывать в каждом тесте.
Например, медоты возвращающие url, делающие скриншот, скроллинг и т.д.'''
import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current_url: {get_url} ')

    '''Method assert word'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f'Value word "{value_word}"- OK!')

    '''Method assert URL'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL value - OK!')

    '''Method create page screenshot '''

    def do_screenshot(self):
        now_time = datetime.datetime.now().strftime("%y-%m-%d_%H:%M:%S")
        name_screenshot = str(self.get_current_url()) + str(now_time) + '.png'
        self.driver.save_screenshot('screenshots/' + name_screenshot)
        print('Screenshot OK!')

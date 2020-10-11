import time
import unittest
from selenium import webdriver
from pages.page_home import PageHome
from pages.page_items import PageItems


class TestMessageError(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/gabriela/PycharmProjects/automation_proyect/driver/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        self.pageHome = PageHome(self.driver)
        self.pageItem = PageItems(self.driver)

    def test_message_error(self):
        self.pageHome.search('hola')
        time.sleep(4)

        assert self.pageItem.get_text_error_message() == 'No results were found for your search "hola"'

    def test_valid_dress(self):
        self.pageHome.search('dress')
        time.sleep(4)

        assert self.pageItem.get_text_valid_message() == '"DRESS"'

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

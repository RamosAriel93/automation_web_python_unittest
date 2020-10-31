import unittest
from selenium import webdriver
from pages.page_home import PageHome
from pages.page_items import PageItems
from pages.page_sing_in import PageSingIn


class TestMessageError(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            r'C:\Users\Gabriela\PycharmProjects\test\automation_web_python_unittest\driver\chromedriverwin.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        self.pageHome = PageHome(self.driver)
        self.pageItem = PageItems(self.driver)
        self.pageSingIn = PageSingIn(self.driver)

    def test_message_error(self):
        self.pageHome.search('hola')

        assert self.pageItem.get_text_error_message() == 'No results were found for your search "hola"'

    def test_valid_dress(self):
        self.pageHome.search('dress')

        assert self.pageItem.get_text_valid_message() == '"DRESS"'

    def test_no_valid_sing_in(self):
        self.pageHome.click_sing_in()
        self.pageSingIn.send_email_and_password('123456', 'test123@test.com')
        self.pageSingIn.click_sing_in()

        assert self.pageSingIn.get_text_error() == 'Authentication failed.'

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

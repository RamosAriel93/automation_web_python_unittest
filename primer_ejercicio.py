import time
import unittest
from selenium import webdriver


class TestError(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/gabriela/PycharmProjects/automation_proyect/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')

    def test_message_error(self):
        self.driver.find_element_by_id('search_query_top').send_keys('hola')
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(4)
        self.error = self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text

        assert self.error == 'No results were found for your search "hola"'

    def test_valid_dress(self):
        self.driver.find_element_by_id('search_query_top').send_keys('dress')
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(4)
        self.valid_message = self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text

        assert self.valid_message == '"DRESS"'

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

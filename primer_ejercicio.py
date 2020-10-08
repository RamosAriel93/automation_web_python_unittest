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

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

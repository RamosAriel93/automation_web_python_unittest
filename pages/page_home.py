from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageHome:
    def __init__(self, my_driver):
        self.input = 'search_query_top'
        self.search_button = 'submit_search'
        self.driver = my_driver

    def search(self, item):
        self.driver.find_element_by_id(self.input).send_keys(item)
        self.driver.find_element_by_name(self.search_button).click()

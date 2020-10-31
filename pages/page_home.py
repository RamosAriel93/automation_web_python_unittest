from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageHome:
    def __init__(self, my_driver):
        self.input = (By.ID, 'search_query_top')
        self.search_button = (By.NAME, 'submit_search')
        self.sing_in = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        self.driver = my_driver

    def search(self, item):
        try:
            box_search = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.input))
            box_search.send_keys(item)

            button_search = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.search_button))
            button_search.click()

        except:
            print("No se encuentra el elemento")

    def click_sing_in(self):
        try:
            button_sing_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sing_in))
            button_sing_in.click()

        except:
            print("No se encuentra el elemento")
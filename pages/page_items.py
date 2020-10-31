from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageItems:
    def __init__(self, my_driver):
        self.error_message = (By.XPATH, '//*[@id="center_column"]/p')
        self.valid_message = (By.XPATH, '//*[@id="center_column"]/h1/span[1]')
        self.driver = my_driver

    def get_text_error_message(self):
        message_error = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.error_message))
        return message_error.text

    def get_text_valid_message(self):
        message_valid = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.valid_message))
        return message_valid.text

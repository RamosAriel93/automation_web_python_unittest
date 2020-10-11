class PageItems:
    def __init__(self, my_driver):
        self.error_message = '//*[@id="center_column"]/p'
        self.valid_message = '//*[@id="center_column"]/h1/span[1]'
        self.driver = my_driver

    def get_text_error_message(self):
        return self.driver.find_element_by_xpath(self.error_message).text

    def get_text_valid_message(self):
        return self.driver.find_element_by_xpath(self.valid_message).text




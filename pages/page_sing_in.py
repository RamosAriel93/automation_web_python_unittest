from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageSingIn:
    def __init__(self, my_driver):
        self.email = (By.ID, "email")
        self.password = (By.ID, "passwd")
        self.button_sing_in = (By.XPATH, '//*[@id="SubmitLogin"]/span/i')
        self.text_error = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')
        self.driver = my_driver

    def send_email_and_password(self, password, email):
        box_email = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.email))
        box_email.send_keys(email)
        box_password = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password))
        box_password.send_keys(password)

    def click_sing_in(self):
        sing_in = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.button_sing_in))
        sing_in.click()

    def get_text_error(self):
        error_text = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.text_error))
        return error_text.text

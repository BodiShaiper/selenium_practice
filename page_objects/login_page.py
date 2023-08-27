from selenium.webdriver.common.by import By
from page_objects.main_page import MainPage
from utilities.ui_utilities.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.CSS_SELECTOR, '#j_username')
    __user_password_input = (By.CSS_SELECTOR, '#j_password')
    __login_button = (By.XPATH, "//button[@class='mb-4 button button--primary']/span/span[text()]")

    def set_email(self, email_value):
        self._send_keys(self.__email_input, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self.__user_password_input, password_value)
        return self

    def click_log_in_button(self):
        self._click(self.__login_button)
        return MainPage(self.driver)

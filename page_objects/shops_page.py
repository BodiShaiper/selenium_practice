from selenium.webdriver.common.by import By
from utilities.ui_utilities.base_page import BasePage


class ShopsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __shops_body = (By.XPATH, "//div[@id='app']")
    __all_stores_button = (By.XPATH, '//a[@qaid="store-locator__all-locations"]')
    __store_finder = (By.XPATH, '//*[@id="content"]/main/div[1]/div/h3')
    __geo_prompt_warning = (By.XPATH, '//div[@id="geoPromptModal"]')
    __close_geo_warning = (By.XPATH, '//i[@class="md-24"]')
    __italy_stores = (By.XPATH, '//a[@id="all-retailer-link-IT"]')
    __appiano_store = (By.XPATH, '//a[@id="retailer-link-390708"]')
    __appiano_check = (By.XPATH, '//span[@class="text-weak"][text()="APPIANO"]')

    def check_if_shops_is_loaded(self):
        return self._is_element_visible(self.__shops_body)

    def check_if_all_stores_is_visible(self):
        return self._is_element_visible(self.__store_finder)

    def geo_warning_check(self):
        if self._is_displayed(self.__geo_prompt_warning):
            self._click(self.__close_geo_warning)
            return self
        else:
            return self

    def click_open_all_stores(self):
        self._click(self.__all_stores_button)
        return self

    def open_italy_retailers(self):
        self._click(self.__italy_stores)
        return self

    def open_appiano_service_center(self):
        self._click(self.__appiano_store)
        return self

    def check_if_appiano_store_is_loaded(self):
        return self._is_element_visible(self.__appiano_check)

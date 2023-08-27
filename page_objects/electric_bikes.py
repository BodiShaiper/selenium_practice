from selenium.webdriver.common.by import By
from utilities.ui_utilities.base_page import BasePage


class ElectricBikesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __electric_bikes_title = (By.XPATH, '//h1[text()="Electric bikes"]')
    __category_el_mountain_bikes = (By.XPATH, '//em[text()="Electric mountain bikes"]')
    __category_el_hybrid_bikes = (By.XPATH, '//em[text()="Electric hybrid bikes"]')
    __category_electra_e_bikes = (By.XPATH, '//em[text()="Electra e-bikes"]')
    __category_electric_road_bikes = (By.XPATH, '//em[text()="Electric road bikes"]')
    __el_mnt_bike_title = (By.XPATH, '//h1[text()="Electric mountain bikes"]')
    __el_rd_bike_title = (By.XPATH, '//h1[text()="Electric road bikes"]')
    __el_e_bike_title = (By.XPATH, '//h1[text()="GO! E-BIKES"]')
    __el_hb_bike_title = (By.XPATH, '//h1[text()="Electric city bikes"]')
    __first_bike_in_list = (
        By.XPATH, '//div[@class="searchresultslistcomponent"]/ul/li[1]/div')
    __close_geo_warning = (By.XPATH, '//i[@class="md-24"]')
    __accept_cookie_button = (By.XPATH, '//a[@id="CybotCookiebotDialogBodyButtonAccept"]')
    __biggest_bike_size = (By.XPATH, '//div[@class="mb-1"]/div/div/button[last()]')
    __add_to_cart_button = (By.XPATH, '//button[@id="addToCartButton"]')

    def geo_popup_check(self):
        if self._is_displayed(self.__close_geo_warning):
            self._click_via_js(self.__close_geo_warning)
            return self
        else:
            return self

    def accept_cookie(self):
        if self._is_displayed(self.__accept_cookie_button):
            self._click_via_js(self.__accept_cookie_button)
            return self
        else:
            return self

    def check_electric_bikes_page(self):
        return self._is_element_visible(self.__electric_bikes_title)

    def open_category_electric_mountain_bikes(self):
        self._click(self.__category_el_mountain_bikes)
        return self

    def open_category_electric_hybrid_bikes(self):
        self._click(self.__category_el_hybrid_bikes)
        return self

    def open_category_electra_e_bikes(self):
        self._click(self.__category_electra_e_bikes)
        return self

    def open_category_electric_road_bikes(self):
        self._click(self.__category_electric_road_bikes)
        return self

    def check_el_mnt_bike_page(self):
        return self._is_element_visible(self.__el_mnt_bike_title)

    def check_el_rd_bike_page(self):
        return self._is_element_visible(self.__el_rd_bike_title)

    def check_el_e_bike_page(self):
        return self._is_element_visible(self.__el_e_bike_title)

    def check_el_hb_bike_page(self):
        return self._is_element_visible(self.__el_hb_bike_title)

    def open_first_bike_in_list(self):
        self.geo_popup_check()
        self._click(self.__first_bike_in_list)
        return self

    def select_biggest_bike(self):
        self._click(self.__biggest_bike_size)
        return self

    def add_bike_to_cart(self):
        self._click(self.__add_to_cart_button)
        return self

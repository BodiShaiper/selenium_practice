from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __log_out_button = (By.XPATH, '//a[@class="sub-dd__item"][@title="Log out"]')
    __person_icon_button = (By.XPATH, '//*[@id="my-profile-login"]/i')
    __log_in_button = (By.XPATH, '//a[@class="sub-dd__item"]')
    __mountain_bikes_menu_button = (By.CSS_SELECTOR, '#expandMountainBikesMainMenu-large')
    __mountain_bikes_block = (By.XPATH, '//*[@id="expandMountainBikesMenuNode-large"]')
    __road_bikes_menu_button = (By.CSS_SELECTOR, '#expandRoadBikesMainMenu-large')
    __road_bikes_block = (By.XPATH, '//*[@id="expandRoadBikesMenuNode-large"]')
    __gravel_bikes_menu_button = (By.CSS_SELECTOR, '#expandGravelBikesMainMenu-large')
    __gravel_bikes_block = (By.XPATH, '//*[@id="expandGravelBikesMenuNode-large"]')
    __shops_retailer_locator = (By.XPATH, '//a[@qaid="nav-categories-link-viewRetailerLocator-large"]')
    __sale_locator = (By.XPATH, '//a[@qaid="nav-categories-link-viewSalePage-large"]')
    __region_logo = (By.XPATH, '//div[@class="nav-utility-bar-b2c-container__b2c-utilities"]/div[2]')
    __netherlands_region = (By.XPATH, '//a[@href="/nl/nl_NL/?clear=true"]')
    __netherlands_logo_check = (
        By.XPATH, '//div[@class="nav-utility-bar-b2c-container__b2c-utilities"]/div[2]/a[@href="/nl/nl_NL/regions/"]')
    __electric_bikes = (By.XPATH, '//a[@id="electricBikesFooterLink"]')
    __close_geo_warning = (By.XPATH, '//div[@id="geoPromptModal"]/div/button')
    __accept_cookie_button = (By.XPATH, '//a[@id="CybotCookiebotDialogBodyButtonAccept"]')

    def click_person_icon_button(self):
        self._click(self.__person_icon_button)
        return self

    def click_log_in_button(self):
        from page_objects.login_page import LoginPage
        self._click(self.__log_in_button)
        return LoginPage(self.driver)

    def if_user_is_logged_in(self):
        self._is_displayed(self.__log_out_button)

    def check_mountain_bikes_block(self):
        self._click(self.__mountain_bikes_menu_button)
        return self._is_displayed(self.__mountain_bikes_block)

    def check_road_bikes_block(self):
        self._click(self.__road_bikes_menu_button)
        return self._is_displayed(self.__road_bikes_block)

    def check_gravel_bikes_block(self):
        self._click(self.__gravel_bikes_menu_button)
        return self._is_displayed(self.__gravel_bikes_block)

    def click_shops_button(self):
        from page_objects.shops_page import ShopsPage
        self._click(self.__shops_retailer_locator)
        return ShopsPage(self.driver)

    def click_sale_button(self):
        from page_objects.sale_page import SalePage
        self._click(self.__sale_locator)
        return SalePage(self.driver)

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

    def open_electric_bikes(self):
        from page_objects.electric_bikes import ElectricBikesPage
        self._click_via_js(self.__electric_bikes)
        return ElectricBikesPage(self.driver)

    def open_region_selection_page(self):
        self._click(self.__region_logo)
        return self

    def select_netherlands_region(self):
        self._click(self.__netherlands_region)
        return self

    def check_if_netherlands_region_is_applied(self):
        return self._is_element_visible(self.__netherlands_logo_check)

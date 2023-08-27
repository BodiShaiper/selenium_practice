from selenium.webdriver.common.by import By
from utilities.ui_utilities.base_page import BasePage


class SalePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __shop_all_sale_bikes = (By.XPATH, '//a[@qaid="link_SaleClearance2023_AllBikesMarquee"]')
    __shop_all_sale_equipment = (By.XPATH, '//a[@id="link_SaleClearance2023_AllGearAccessories"]')
    __shop_all_sale_apparel = (By.XPATH, '//a[@id="link_SaleClearance2023_AllApparel"]')
    __cycling_equipment_title = (By.XPATH, '//h1[text()="Cycling equipment"]')
    __bike_clothing_title = (By.XPATH, '//h1[text()="Bike clothing"]')
    __bikes_title = (By.XPATH, '//h1[text()="Bikes"]')
    __filter_sale_true = (By.XPATH, '//li[@id="filter-Sale-true"]')
    __sale_and_clearance_block = (By.XPATH, '//section[@id="marquee_SaleClearance2023_Editorial"]')
    __clearance_centers = (By.XPATH, '//a[@id="link_SaleClearance2023_EditorialMarquee4"]')
    __clearance_centers_title = (By.XPATH, '//h1[text()="Trek Clearance Centers are open now"]')

    def open_all_sale_bikes(self):
        self._click(self.__shop_all_sale_bikes)
        return self

    def open_all_sale_equipment(self):
        self._click(self.__shop_all_sale_equipment)

    def open_all_sale_apparel(self):
        self._click(self.__shop_all_sale_apparel)

    def open_track_clearance_centers(self):
        self._click(self.__clearance_centers)

    def check_if_sales_page_is_opened(self):
        return self._is_element_visible(self.__sale_and_clearance_block)

    def check_if_sales_filter_is_on(self):
        return self._is_element_visible(self.__filter_sale_true)

    def check_if_bikes_sales_is_opened(self):
        return self._is_element_visible(self.__bikes_title)

    def check_if_all_sale_equipment_is_opened(self):
        return self._is_element_visible(self.__cycling_equipment_title)

    def check_if_all_sale_apparel_is_opened(self):
        return self._is_element_visible(self.__bike_clothing_title)

    def check_if_clearance_centers_opened(self):
        return self._is_element_visible(self.__clearance_centers_title)

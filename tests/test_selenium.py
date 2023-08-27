from page_objects.electric_bikes import ElectricBikesPage
from page_objects.main_page import MainPage
from page_objects.shops_page import ShopsPage
from page_objects.sale_page import SalePage
from utilities.config_reader import ReadConfig
from selenium.webdriver.support.ui import Select
import pytest


@pytest.mark.smoke
def test_title(create_driver):
    driver = create_driver
    actual_title = driver.title
    assert actual_title == "Trek Bikes - The world's best bikes and cycling gear"


@pytest.mark.smoke
@pytest.mark.regression
def test_login(create_driver):
    user_name, password = ReadConfig.get_user_creds()
    driver = create_driver
    MainPage(driver).click_person_icon_button().click_log_in_button().set_email(user_name).set_password(
        password).click_log_in_button()


@pytest.mark.smoke
def test_selection_region(create_driver):
    driver = create_driver
    main_page = MainPage(driver).open_region_selection_page().select_netherlands_region()
    assert main_page.check_if_netherlands_region_is_applied(), 'Smth is wrong, Netherlands regions is not applied'


@pytest.mark.regression
@pytest.mark.parametrize("navigation_button", ["mountain", "road", "gravel", "shops", "sale", "electric_bikes"])
def test_redirect_to_navigation_blocks(create_driver, navigation_button):
    driver = create_driver
    main_page = MainPage(driver)

    if navigation_button == "mountain":
        main_page.check_mountain_bikes_block()
    elif navigation_button == "road":
        main_page.check_road_bikes_block()
    elif navigation_button == "gravel":
        main_page.check_gravel_bikes_block()
    elif navigation_button == "shops":
        main_page.click_shops_button()
        assert ShopsPage(driver).check_if_shops_is_loaded(), "shop page is not displayed normally"
    elif navigation_button == "sale":
        main_page.click_sale_button()
        assert SalePage(driver).check_if_sales_page_is_opened(), "sale page is not displayed properly"
    elif navigation_button == "electric_bikes":
        main_page.open_electric_bikes()
        assert ElectricBikesPage(driver).check_electric_bikes_page(), "electric bikes page is not opened properly"


@pytest.mark.smoke
def test_view_all_stores(create_driver):
    driver = create_driver
    MainPage(driver).click_shops_button().geo_warning_check().click_open_all_stores()
    assert ShopsPage.check_if_all_stores_is_visible, "Stores are failed to load"


@pytest.mark.regression
def test_open_store_in_appiano(create_driver):
    driver = create_driver
    MainPage(driver).click_shops_button().geo_warning_check().click_open_all_stores().open_italy_retailers(). \
        open_appiano_service_center()
    assert ShopsPage.check_if_appiano_store_is_loaded, "Store in Appiano is failed to load"


@pytest.mark.smoke
@pytest.mark.parametrize("sale_item", ["bikes", "equipments", "apparel", "clearance_centers"])
def test_open_all_sale_items(create_driver, sale_item):
    driver = create_driver
    sale_page = MainPage(driver).click_sale_button()

    if sale_item == 'bikes':
        sale_page.open_all_sale_bikes()
        assert sale_page.check_if_bikes_sales_is_opened(), 'not a page with bikes is opened, smth is wrong'
        assert sale_page.check_if_sales_filter_is_on(), 'sale filter is not ok'
    elif sale_item == 'equipments':
        sale_page.open_all_sale_equipment()
        assert sale_page.check_if_all_sale_equipment_is_opened(), 'not a page with sale equipments is opened'
        assert sale_page.check_if_sales_filter_is_on(), 'sale filter is broken'
    elif sale_item == 'apparel':
        sale_page.open_all_sale_apparel()
        assert sale_page.check_if_all_sale_apparel_is_opened(), 'not a page with bike cloth is opened'
        assert sale_page.check_if_sales_filter_is_on(), 'sale filter is set improperly'
    elif sale_item == 'clearance_centers':
        sale_page.open_track_clearance_centers()
        assert sale_page.check_if_clearance_centers_opened()


@pytest.mark.regression
@pytest.mark.parametrize("e_bike_category", ["mountain", "road", "electra", "hybrid"])
def test_e_bike_category_selection(create_driver, e_bike_category):
    driver = create_driver
    e_bike_page = MainPage(driver).geo_popup_check().accept_cookie().open_electric_bikes()

    if e_bike_category == 'mountain':
        e_bike_page.open_category_electric_mountain_bikes().geo_popup_check().accept_cookie()
        assert e_bike_page.check_el_mnt_bike_page()
    elif e_bike_category == 'road':
        e_bike_page.open_category_electric_road_bikes()
        assert e_bike_page.check_el_rd_bike_page()
    elif e_bike_category == 'electra':
        e_bike_page.open_category_electra_e_bikes()
        assert e_bike_page.check_el_e_bike_page()
    elif e_bike_category == 'hybrid':
        e_bike_page.open_category_electric_hybrid_bikes()
        assert e_bike_page.check_el_hb_bike_page()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("e_bike_category, sorting_by", [("mountain", "price-desc"),
                                                         ("mountain", "price-asc"),
                                                         ("road", "price-desc"),
                                                         ("road", "price-asc"),
                                                         ("electra", "price-desc"),
                                                         ("electra", "price-asc"),
                                                         ("hybrid", "price-desc"),
                                                         ("hybrid", "price-asc")
                                                         ])
def test_open_the_most_expensive_or_cheapest_e_bike(create_driver, e_bike_category, sorting_by):
    driver = create_driver
    e_bike_page = MainPage(driver).geo_popup_check().accept_cookie().open_electric_bikes()

    if e_bike_category == 'mountain':
        e_bike_page.open_category_electric_mountain_bikes().geo_popup_check()
        Select(driver.find_element(by='id', value='sortOptions1')).select_by_value(sorting_by)
        ElectricBikesPage(driver).open_first_bike_in_list().select_biggest_bike().add_bike_to_cart()
    elif e_bike_category == 'road':
        e_bike_page.open_category_electric_road_bikes().geo_popup_check()
        Select(driver.find_element(by='id', value='sortOptions1')).select_by_value(sorting_by)
        ElectricBikesPage(driver).open_first_bike_in_list().select_biggest_bike().add_bike_to_cart()
    elif e_bike_category == 'electra':
        e_bike_page.open_category_electra_e_bikes().geo_popup_check()
        Select(driver.find_element(by='id', value='sortOptions1')).select_by_value(sorting_by)
        ElectricBikesPage(driver).open_first_bike_in_list().select_biggest_bike().add_bike_to_cart()
    elif e_bike_category == 'hybrid':
        e_bike_page.open_category_electric_hybrid_bikes().geo_popup_check()
        Select(driver.find_element(by='id', value='sortOptions1')).select_by_value(sorting_by)
        ElectricBikesPage(driver).open_first_bike_in_list().select_biggest_bike().add_bike_to_cart()

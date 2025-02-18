import time

from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")


def test_two_monitors(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_monitors()
    time.sleep(2)
    home_page.check_many_monitors(2)

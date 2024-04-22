import pytest

from selenium import webdriver
from pages.create_acc_page import CreateAccPage
from pages.collections_page import CollectionPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def create_acc(driver):
    return CreateAccPage(driver)


@pytest.fixture()
def collection_page(driver):
    return CollectionPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

from pages.base_page import BasePage
from locators import collections_page_locs as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac


class CollectionPage(BasePage):
    rel_url = 'collections/eco-friendly.html'
    category_text = 'Eco Friendly'
    category_title = 'Eco Friendly'
    product_name = 'Ana Running Short'

    def check_category_text(self):
        category_text = self.find(loc.category).text
        assert category_text == self.category_text

    def check_category_title(self):
        category_title = self.driver.title
        assert category_title == self.category_title

    def add_to_cart(self):
        size_btn = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(loc.short_28_size))
        ac(self.driver).move_to_element(size_btn).perform()
        size_btn.click()
        self.find(loc.short_28_color).click()
        add_btn = self.find(loc.short_add_to_cart)
        ac(self.driver).move_to_element(add_btn).perform()
        add_btn.click()
        added_text = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(loc.added_to_cart_alert)).text
        assert self.product_name in added_text
        cart_num = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(loc.cart_counter)).text
        assert cart_num == '1'

from pages.base_page import BasePage
from locators import sale_page_locs as loc


class SalePage(BasePage):
    rel_url = 'sale.html'
    category_text = 'Sale'

    def check_sale_blocks(self):
        sale_blocks = self.find_all(loc.sale_block)
        assert len(sale_blocks) == 6

    def check_top_menu(self):
        top_menu = self.find_all(loc.top_menu)
        assert len(top_menu) == 6

    def check_side_menu(self):
        side_menu = self.find(loc.side_menu)
        assert side_menu.is_displayed()

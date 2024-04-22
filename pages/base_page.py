from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    base_url = 'https://magento.softwaretestingboard.com/'
    rel_url = None

    def visit_page(self):
        if self.rel_url:
            self.driver.get(f'{self.base_url}{self.rel_url}')
        else:
            raise Exception('No rel_url given')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

from selenium.webdriver.common.by import By

page_title = (By.TAG_NAME, 'title')
category = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
cart = (By.XPATH, '//a[@class="action showcart"]')
cart_counter = (By.XPATH, '//span[@class="counter-number"]')
added_to_cart_alert = (By.XPATH, '//div[contains(text(), "You added")]')
short_28_size = (By.ID, 'option-label-size-143-item-171')
short_28_color = (By.ID, 'option-label-color-93-item-56')
short_add_to_cart = (By.XPATH, '//button[@class="action tocart primary"]')
short_text = (By.XPATH, '//a[@class="product-item-link"]')

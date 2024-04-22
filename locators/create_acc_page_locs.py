from selenium.webdriver.common.by import By

first_name = (By.ID, 'firstname')
last_name = (By.ID, 'lastname')
email = (By.ID, 'email_address')
password = (By.ID, 'password')
pass_confirm = (By.ID, 'password-confirmation')
submit = (By.XPATH, '//button[@class="action submit primary"]')
email_error = (By.ID, 'email_address-error')
first_name_error = (By.ID, 'firstname-error')
password_error = (By.ID, 'password-error')

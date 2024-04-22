from pages.base_page import BasePage
from locators import create_acc_page_locs as loc


class CreateAccPage(BasePage):
    rel_url = 'customer/account/create/'
    fname = 'Alex'
    lname = 'Xela'
    email = 'alex@xela.com'
    password = 'A1exxela'
    required_field_error = 'This is a required field.'
    invalid_email_error = 'Please enter a valid email address (Ex: johndoe@domain.com).'
    password_3_classes_error = (
        'Minimum of different classes of characters in password is 3. Classes of characters: ' +
        'Lower Case, Upper Case, Digits, Special Characters.'
    )

    def no_first_name_given(self):
        self.find(loc.last_name).send_keys(self.lname)
        self.find(loc.email).send_keys(self.email)
        self.find(loc.password).send_keys(self.password)
        self.find(loc.pass_confirm).send_keys(self.password)
        self.find(loc.submit).click()
        error_text = self.find(loc.first_name_error).text
        assert error_text == self.required_field_error

    def invalid_email(self):
        self.find(loc.first_name).send_keys(self.fname)
        self.find(loc.last_name).send_keys(self.lname)
        self.find(loc.email).send_keys(self.email[:4])
        self.find(loc.password).send_keys(self.password)
        self.find(loc.pass_confirm).send_keys(self.password)
        self.find(loc.submit).click()
        error_text = self.find(loc.email_error).text
        assert error_text == self.invalid_email_error

    def invalid_password(self):
        self.find(loc.first_name).send_keys(self.fname)
        self.find(loc.last_name).send_keys(self.lname)
        self.find(loc.email).send_keys(self.email)
        self.find(loc.password).send_keys('123456789')
        self.find(loc.pass_confirm).send_keys('123456789')
        self.find(loc.submit).click()
        password_error = self.find(loc.password_error).text
        assert password_error == self.password_3_classes_error

import pytest


@pytest.mark.smoke
def test_no_email(create_acc):
    create_acc.visit_page()
    create_acc.no_first_name_given()


@pytest.mark.smoke
def test_invalid_email(create_acc):
    create_acc.visit_page()
    create_acc.invalid_email()


@pytest.mark.smoke
def test_invalid_password(create_acc):
    create_acc.visit_page()
    create_acc.invalid_password()

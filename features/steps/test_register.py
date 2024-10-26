"""This module has the steps from this project"""
from pytest_bdd import given, then, when, scenario
import allure
from pages.actions.register_actions import RegisterActions


@scenario("register.feature", "Register User")
@allure.suite("Landing Page")
@allure.title("Registration from user")
def test_register_page():
    pass


@given('The user access to the Website')
def open_web(browser, props)-> None:
    register_page = RegisterActions(browser)
    register_page.load_web(f"{props('baseUrl')}")


@when('The user enter with the credentials')
def step_register_user(browser, props)-> None:
    register_page = RegisterActions(browser)
    register_page.type_user(f"{props('user')}")
    register_page.type_email(f"{props('email')}")
    register_page.type_age("80")
    register_page.click_to_register()


@then('The user is registered successfully')
def step_registered_user_successfully(browser) -> None:
    register_page = RegisterActions(browser)
    assert register_page.user_is_logged(), "The user is not logged in successfully."
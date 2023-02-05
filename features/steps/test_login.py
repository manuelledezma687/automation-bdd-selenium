"""This module has the steps from this project"""
from pytest_bdd import given, then, when, scenario
import allure
from pages.actions.login_actions import LoginActions


@scenario("login.feature", "Login User")
@allure.suite("Landing Page")
@allure.title("Login from user")
def test_login_page():
    pass


@given('The user access to the Website')
def open_web(browser, props):
    login_page = LoginActions(browser)
    login_page.load_web(f"{props('baseUrl')}")


@when('The user enter with the credentials')
def step_login_user(browser, props):
    login_page = LoginActions(browser)
    login_page.click_login_section()
    login_page.type_user(f"{props('user')}")
    login_page.type_password(f"{props('password')}")
    login_page.click_to_login()


@then('The user access successfully')
def step_login_user_successfully(browser):
    login_page = LoginActions(browser)
    login_page.user_is_logged()

from actions.LoginActions import LoginActions
from configurations.config import testData
from behave import given, when, then

@given(u'The user access to the Website')
def step_enter_to_url(context):
    login_page = LoginActions(context)
    login_page.load_web(testData.BASE_URI)


@when('The user enter with the credentials')
def step_login_user(browser):
    # login_page = LoginActions(browser)
    # login_page.clickToLoginSection()
    # login_page.typeUser(USER)
    # login_page.typePassword(PASSWORD)
    # login_page.clickToLogin()
    pass
    
@then('The user access successfully')
def step_login_user_successfully(browser):
    # login_page = LoginActions(browser)
    # login_page.UserIsLogged()
    pass
  
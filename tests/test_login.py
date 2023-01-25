from actions.LoginActions import LoginActions
from configurations.config import testData


def test_login_user(browser):
  login_page = LoginActions(browser)
  login_page.load_web(testData.BASE_URI)
  login_page.click_login_section()
  login_page.type_user(testData.USER)
  login_page.type_password(testData.PASSWORD)
  login_page.click_to_login()
  login_page.user_is_logged()

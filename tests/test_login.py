from actions.login_actions import LoginActions as login_entry
from configurations.config import BASE_URI, USER, PASSWORD


def test_login_user(browser):
    login_page = login_entry(browser)
    login_page.load_web(BASE_URI)
    login_page.click_login_section()
    login_page.type_user(USER)
    login_page.type_password(PASSWORD)
    login_page.click_to_login()
    login_page.user_is_logged()

from actions.LoginActions import LoginActions
from configurations.Config import BASE_URI, USER, PASSWORD

def test_login_user(browser):
  login_page = LoginActions(browser)
  login_page.loadSite(BASE_URI)
  login_page.clickToLoginSection()
  login_page.typeUser(USER)
  login_page.typePassword(PASSWORD)
  login_page.clickToLogin()
  #login_page.UserIsLogged()
  
  ##First commit wait others commits

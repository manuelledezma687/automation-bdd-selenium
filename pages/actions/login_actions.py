from pages.pages_objects.login import Login
from pages.pages_objects.home import Home
from pages.actions.base_actions import BaseActions

class LoginActions(BaseActions):

    def __init__(self, browser):
        self._browser = browser
        super().__init__(browser)

    def load_web(self, url):
        self.load(url)

    def click_login_section(self):
        self.element_click(Home.loginSection)

    def type_user(self,user):
        self.type_info(Login.userInput,user)

    def type_password(self,password):
        self.type_info(Login.passwordInput,password)

    def click_to_login(self):
        self.element_click(Login.loginButton)

    def user_is_logged(self):
        self.is_displayed(Login.userLogged)

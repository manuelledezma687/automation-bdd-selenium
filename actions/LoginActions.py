from pages.Login import userInput, passwordInput,loginButton, userLogged
from pages.Home import loginSection
from actions.BaseActions import BaseActions

class LoginActions(BaseActions):
    
    def __init__(self, browser):
        super().__init__(browser)

    def load_web(self, url):
        self.load(url)
        
    def click_login_section(self):
        self.element_click(loginSection)

    def type_user(self,user):
        self.type_info(userInput,user)
        
    def type_password(self,password):
        self.type_info(passwordInput,password)
        
    def click_to_login(self):
        self.element_click(loginButton)

    def user_is_logged(self):
        self.is_displayed(userLogged)
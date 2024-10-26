from pages.pages_objects.register import Register
from pages.actions.base_actions import BaseActions

class RegisterActions(BaseActions):

    def __init__(self, browser):
        self._browser = browser
        super().__init__(browser)

    def load_web(self, url):
        self.load(url)

    def type_user(self,user: str):
        self.type_info(Register.userInput,user)

    def type_email(self,email: str):
        self.type_info(Register.emailInput,email)

    def type_age(self,age: str):
        self.type_info(Register.ageInput,age)

    def click_to_register(self):
        self.element_click(Register.registerButton)
    
    def user_is_logged(self) -> bool:
        return self.is_displayed(Register.userRegisteredMessage)

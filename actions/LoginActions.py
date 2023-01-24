from pages.Login import userInput, passwordInput,loginButton, userLogged
from pages.Home import loginSection
from configurations.BaseActions import load,typeInfo,elementClick,isDisplayed


class LoginActions:

    loadUrl = load
    type = typeInfo
    elementClick = elementClick
    isDisplayed = isDisplayed
    
    def __init__(self, browser):
        self.browser = browser

    def loadSite(self, url):
        self.loadUrl(url)
        
    def clickToLoginSection(self):
        self.elementClick(*loginSection)

    def typeUser(self,user):
        self.type(*userInput,user)
        
    def typePassword(self,password):
        self.type(*passwordInput,password)
        
    def clickToLogin(self):
        self.elementClick(*loginButton)

    def UserIsLogged(self):
        self.isDisplayed(*userLogged)

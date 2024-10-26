from selenium.webdriver.common.by import By

class Login:
    userInput = (By.XPATH, "//input[@id='username']")
    passwordInput = (By.XPATH, "//input[@id='password']")
    loginButton = (By.XPATH, "//button[@class='academy-btn academy-btn--bg-purple']")
    userLogged = (By.XPATH, "//*[@class='academy-logged-in-message']")

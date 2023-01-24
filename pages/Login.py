from selenium.webdriver.common.by import By


userInput = (By.XPATH, "//input[@id='loginusername']")
passwordInput = (By.XPATH, "//input[@id='loginpassword']")
loginButton = (By.XPATH, "//button[text()='Log in']")
closeButton = (By.XPATH, "//button[text()='Close']")
userLogged = (By.XPATH, "//a[@id='nameofuser']")

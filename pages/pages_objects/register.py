from selenium.webdriver.common.by import By

class Register:
    userInput = (By.XPATH, "//input[@id='name']")
    emailInput = (By.XPATH, "//input[@id='email']")
    ageInput = (By.XPATH, "//input[@id='ageSlider']")
    registerButton = (By.XPATH, "//input[@type='submit']")
    userRegisteredMessage = (By.XPATH, "//*[@id='formMessage']")

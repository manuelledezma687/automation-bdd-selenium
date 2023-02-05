from selenium.webdriver.common.by import By

class Contact:
    contactEmail = (By.XPATH, "//input[@id='recipient-email']")
    contactName = (By.XPATH, "//input[text()='Contact Name:']")
    contactMessage = (By.XPATH, "//textarea[@id='message-text']")
    contactButton = (By.XPATH, "//button[text()='Send message']")
    closeButton = (By.XPATH, "//button[text()='Close']")

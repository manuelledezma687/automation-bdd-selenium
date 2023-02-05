from selenium.webdriver.common.by import By

class Home:
    imgLogo = (By.XPATH, "//a[@id='nava']")
    homeSection = (By.XPATH, "//a[text()='Home ']")
    contactSection = (By.XPATH, "//a[text()='Contact']")
    AboutUsSection = (By.XPATH, "//a[text()='About us']")
    cartSection = (By.XPATH, "//a[text()='Cart']")
    loginSection = (By.XPATH, "//a[text()='Log in']")
    logOutSection = (By.XPATH, "//a[text()='Log out']")
    signUpSection = (By.XPATH, "//a[text()='Sign up']")
    phonesSection = (By.XPATH, "//a[text()='Phones']")
    laptopsSection = (By.XPATH, "//a[text()='Laptops']")
    monitorsSection = (By.XPATH, "//a[text()='Monitors']")

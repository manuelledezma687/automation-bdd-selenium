from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def __init__(self, browser):
      self.browser = browser

def load(self,url):
      self.browser.get(url)

def elementClick(self,xpath,locator):
      user = self.browser.find_element(xpath,locator)
      user.click()
      
def typeInfo(self,xpath,locator,info):
      user = self.browser.find_element(xpath,locator)
      user.send_keys(info)
      
def isDisplayed(self,xpath, locator):
      # user = self.browser.find_element(xpath,locator)
      # WebDriverWait(self,timeout=10).until(EC.presence_of_element_located((user)))
      pass
      
def isEnabled(self,locator,element):
      pass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack

class Framework():

    def __init__(self,driver):
        self.driver=driver

    def LocateForTheLocator(self, locator):
            locator=locator.lower()
            if locator == 'id':
                return By.ID
            elif locator == 'class':
                return By.CLASS_NAME
            elif locator == 'css':
                return By.CSS_SELECTOR
            elif locator == 'xpath':
                return By.XPATH
            elif locator == 'name':
                return By.NAME
            elif locator == 'link':
                return By.PARTIAL_LINK_TEXT
            elif locator == 'partial link':
                return By.LINK_TEXT
            else:
                print ('!!! didnt get the ' + locator)
            return False

    def LocateFor(self,element,locator):
        path = None
        try:
            locator=locator.lower()
            returnLocator=self.LocateForTheLocator(locator)
            path = self.driver.find_element(returnLocator,element)
            print ('### I found the Locator: ' + locator + ' with element: ' + element)
        except:
            print ('!!! impossible to get the Locator: ' + locator + ' with element '  + element)
        return path

    def Click(self,element,locator):
        try:
            path=self.LocateFor(element,locator)
            path.click()
            print ('### I clicked on the element: ' + element + ' with Locator: ' + locator)
        except:
            print ("!!! I didn't click the element: " + element + ' with Locator: ' + locator)
        return path
    def SendKeys(self,element,locator,data):
        try:
            path=self.Click(element,locator)
            # path= self.LocateFor(element,locator)
            path.send_keys(data)
            print ('### I sent the data: ' + data)
        except:
            print ("!!! I didn't sent the data: " + data)

    def IsElementPresent(self,element,locator):
        try:
            present = self.LocateFor(element, locator)
            if present:
                print ('### The element is present')

            else:
                print ('!!! The element is NOT present')
        except:
            print('!!! EXCEPTION: Element not present')


    def IsEnabled(self, element, locator):
        try:
            enabled = self.LocateFor(element , locator)
            if enabled.is_enabled():
                print ('### The element is enabled')
            else:
                print ('!!! The element is disabled')
        except:
            print('!!! EXCEPTION: Element not enabled/disabled')


    def WaitForElement(self, element, locator, timeout = 10,
                       pollFrequency = 0.5):
        path = None
        try:
            byLocator = self.LocateForTheLocator(locator)
            print ('!!! Waiting for maximum: ' + str(timeout) +
                   ' seconds for element to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency= 0.5,
                                ignored_exceptions= [NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            path = wait.until(EC.element_to_be_clickable((byLocator,element))
            print ("### Element appeared on time")
        except:
            print("!!! Element appeared on time")
            print_stack()
        return path
















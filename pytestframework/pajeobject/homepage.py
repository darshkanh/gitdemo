
from selenium.webdriver.common.by import By
from pajeobject.checkoutpage import Checkoutpage





class Homepage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    check = (By.ID, "exampleCheck1")
    email = (By.NAME,"email")
    gender = (By.ID,"exampleFormControlSelect1")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    submit = (By.XPATH, "//input[@value='Submit']")
    submit2 =(By.CSS_SELECTOR,"[type=submit]")
    checkbox =(By.XPATH,"//div[@class='checkbox checkbox-primary']")

    def shopitems(self):
        return self.driver.find_element(*Homepage.shop).click()
        checkOutPage = Checkoutpage(self.driver)
        return checkOutPage

    def Name(self):
        return self.driver.find_element(*Homepage.name)

    def getcheckbox(self):
        return self.driver.find_element(*Homepage.check)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getgender(self):
        return self.driver.find_element(*Homepage.gender)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)


    def getsubmit(self):
        return self.driver.find_element(*Homepage.submit)

    def clicksubmit(self):
        return self.driver.find_element(*Homepage.submit2)

    def clickcheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)






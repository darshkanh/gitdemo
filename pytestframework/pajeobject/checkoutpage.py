from selenium.webdriver.common.by import By
from pajeobject.confirmpage import ConfirmPage


class Checkoutpage:


    checkout = (By.XPATH, "//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    prodbutton = (By.CSS_SELECTOR, ".card-footer button")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*Checkoutpage.cardTitle)

    def prodselect(self):
        return self.driver.find_elements(*Checkoutpage.prodbutton)

    def check(self):
        return self.driver.find_element(*Checkoutpage.checkout).click()
        confirm = ConfirmPage(self.driver)
        return confirm
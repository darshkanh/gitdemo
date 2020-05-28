import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pajeobject.homepage import Homepage
from pajeobject.checkoutpage import Checkoutpage

from utility.baseclass import BaseClass


class Testone(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homepage = Homepage(self.driver)
        checkpage = homepage.shopitems()
        # //div[@class"card h-100"]
        # //div[@class"card h-100"]/div/h4/a
        log.info("get all card titles")
        log.error("get all card titles")

        checking =Checkoutpage(self.driver)
        cards = checking.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            product = card.text
            log.info(product)
            if product == "Blackberry":
                checkpage.prodselect()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmpage = checkpage.check()
        log.info("entering the country in India")
        self.driver.find_element_by_id("country").send_keys("IND")

        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        homepage.clicksubmit().click()
        # print(driver.find_element_by_class_name("alert-success").text)
        successtext = self.driver.find_element_by_class_name("alert-success").text
        log.info("text received from application" +successtext)
        assert ("Success! Thank you!" in successtext)
        self.driver.get_screenshot_as_file("screen.png")


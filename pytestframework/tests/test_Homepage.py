import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.Homepagedata import Homepagedata
from pajeobject.homepage import Homepage
from utility.baseclass import BaseClass



class TestHomepage(BaseClass):

    def test_formsubmission(self, getdata):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        log.info("firstname is :"+getdata["firstname"])
        homepage.Name().send_keys(getdata["firstname"])
        homepage.getcheckbox().click()
        homepage.getEmail().send_keys(getdata["lastname"])
        self.selectOptionByText(homepage.getgender(), getdata["gender"])
        homepage.getsubmit().click()
        alertText = homepage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=Homepagedata.getTestdata('Testcase2'))
    def getdata(self, request):
        return request.param




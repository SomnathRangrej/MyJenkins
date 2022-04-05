import pytest
from selenium import webdriver

class TestLogin:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_HomeTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin12")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.find_element_by_xpath("//*[@id ='menu_admin_viewAdminModule']/b").is_enabled() == True

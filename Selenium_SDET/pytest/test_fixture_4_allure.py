import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure

@allure.severity(allure.severity_level.NORMAL)
class TestLogin:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="D:\MyGitHub\MyGitHub\MySeleniumScripts\drivers\chromedriver_win32\chromedriver.exe")
        yield
        self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_HomeTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        if self.driver.title == "OrangeHRM123":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_HomeTitle.png", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.find_element_by_xpath("//*[@id ='menu_admin_viewAdminModule']/b").is_enabled() == True


'''
# Note:
    - Allure supports decorator concept, i.e. using difference severity levels for each class/method
    - we can attach screenshots in report itself
'''
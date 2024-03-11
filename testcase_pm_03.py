from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestAdminPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_admin_page_headers(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        username_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input"))
        )
        username_field.send_keys("Admin")

        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input--active"))
        )
        password_field.send_keys("admin123")

        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]'))
        )
        login_button.click()

        admin = WebDriverWait(self.driver, 120).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a'))
        )
        admin.click()

        # Click on "PIM"
        PIM = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a'))
        )
        PIM.click()

        # Click on "Leave"
        Leave = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(3) > a'))
        )
        Leave.click()

        # Click on "Time"
        Time = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(4) > a'))
        )
        Time.click()

        # Click on "Recruitment"
        Recruitment = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a'))
        )
        Recruitment.click()

        # Click on "My Info"
        Info = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a'))
        )
        Info.click()

        # Click on "Performance"
        Performance = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(7) > a'))
        )
        Performance.click()

        # Click on "Dashboard"
        Dashboard = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a'))
        )
        Dashboard.click()

        # Click on "Directory"
        Directory = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(9) > a'))
        )
        Directory.click()

        # Click on "Maintenance"
        Maintenance = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(10) > a'))
        )
        Maintenance.click()

        administrator_access_link = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/form/h6'))
        )
        administrator_access_link.click()
        password_input = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[3]/div/div[2]/input'))
        )
        password_input.send_keys("admin123")

        confirm_button = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/form/div[4]/button[2]'))
        )
        confirm_button.click()

        # Click on "Claim"
        Claim = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(11) > a'))
        )
        Claim.click()

        # Click on "Buzz"
        Buzz = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'))
        )
        Buzz.click()

        def tearDown(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
















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

        username_field = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input"))
        )
        username_field.send_keys("Admin")

        password_field = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input--active"))
        )
        password_field.send_keys("admin123")

        login_button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]'))
        )
        login_button.click()

        admin_page_link = WebDriverWait(self.driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
        )
        admin_page_link.click()

        # Click on "User Management"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span[contains(text(), "User Management")]'))
        )
        element.click()

        # Click on "Job"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span[contains(text(), "Job")]'))
        )
        element.click()

        # Click on "Organization"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span[contains(text(), "Organization")]'))
        )
        element.click()

        # Click on "Qualification"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span[contains(text(), "Qualifications")]'))
        )
        element.click()

        # Click on "Nationalities"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a[contains(text(), "Nationalities")]'))
        )
        element.click()

        # Click on "Corporate Banking"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a[contains(text(), "Corporate Branding")]'))
        )
        element.click()

        # Click on "Configuration"
        element = WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span[contains(text(), "Configuration")]'))
        )
        element.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()







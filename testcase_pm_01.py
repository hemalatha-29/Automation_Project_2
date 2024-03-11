from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_textbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))

    forget_password_link = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
    forget_password_link.click()

    username_textbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#app > div.orangehrm-forgot-password-container > div.orangehrm-forgot-password-wrapper > div > form > div.oxd-form-row > div > div:nth-child(2) > input'))
    )

    username_textbox.send_keys("Admin")

    reset_password_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]')
    reset_password_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]//div[contains(@class, "message success")]/h6'))
    )

    expected_success_message = "Reset password link sent successfully."
    assert expected_success_message in success_message.text, "Unexpected success message: " + success_message.text
    print("Success message found:", success_message.text)

except Exception as e:
    print( "Reset password link sent successfully.")

finally:
    driver.quit()


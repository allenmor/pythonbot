from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# Navigate to a website
driver.get("https://www.linkedin.com")

email_login = driver.find_element(By.NAME, 'session_key')
email_login.send_keys("blah@gmail.com")
email_pass = driver.find_element(By.NAME, 'session_password')
email_pass.send_keys("blah")
submit = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
submit.click()
search_input = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
search_input.send_keys('React')
search_input.send_keys(Keys.RETURN)
try:
    wait = WebDriverWait(driver, 10)
    jobs_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button')))
    jobs_button.click()
except TimeoutError:
    print("Timed out waiting for the element to be clickable.")
try:
    wait = WebDriverWait(driver, 10)
    easy_apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button')))
    easy_apply_btn.click()
except TimeoutError:
    print("Timed out waiting for the element to be clickable.")














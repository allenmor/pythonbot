from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException




chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# Navigate to a website
driver.get("https://orteil.dashnet.org/cookieclicker/")
wait = WebDriverWait(driver, 10)

# Wait for the element to be present and visible on the page
english = wait.until(EC.visibility_of_element_located((By.ID, "langSelect-EN")))

english.click()

cookie = driver.find_element(By.ID, 'bigCookie')


# button0 = driver.find_element(By.ID, "product0")
# button1 = driver.find_element(By.ID, "product1")


while cookie.is_enabled():
    cookie.click()
    button0 = driver.find_element(By.ID, "product0")
    button1 = driver.find_element(By.ID, "product1")
    if driver.find_element(By.ID, "product2"):
        button2 = driver.find_element(By.ID, "product2")
    if driver.find_element(By.ID, "product3"):
        button3 = driver.find_element(By.ID, "product3")
    if driver.find_element(By.ID, "product4"):
        button4 = driver.find_element(By.ID, "product4")
    if driver.find_element(By.ID, "product5"):
        button5 = driver.find_element(By.ID, "product5")
    if driver.find_element(By.ID, "product6"):
        button6 = driver.find_element(By.ID, "product6")
    try:
        upgrade0 = driver.find_element(By.ID, "upgrade0")
        if "crate upgrade enabled" in upgrade0.get_attribute("class"):
            upgrade0.click()
    except NoSuchElementException:
        pass
    if "product unlocked enabled" in button6.get_attribute("class"):
        button6.click()
    if "product unlocked enabled" in button5.get_attribute("class"):
        button5.click()
    if "product unlocked enabled" in button4.get_attribute("class"):
        button4.click()
    if "product unlocked enabled" in button3.get_attribute("class"):
        button3.click()
    if "product unlocked enabled" in button2.get_attribute("class"):
        button2.click()
    if "product unlocked enabled" in button1.get_attribute("class"):
        button1.click()
    if "product unlocked enabled" in button0.get_attribute("class"):
        button0.click()

    





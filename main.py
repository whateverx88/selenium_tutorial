from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
driver = webdriver.Firefox(
    service=Service("/usr/local/bin/geckodriver"),
    options=options
)

driver.get("https://automationpractice.techwithjatin.com/")
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in_a.click()
print(type(sign_in_a))
driver.maximize_window()
sleep(2)
driver.quit()
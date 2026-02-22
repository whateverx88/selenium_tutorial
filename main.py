from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

class Gender:
    MALE = 0
    FEMALE = 1

DATA_EMAIL = "test@test.pl"
DATA_GENDER = Gender.FEMALE

options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
driver = webdriver.Firefox(
    service=Service("/usr/local/bin/geckodriver"),
    options=options
)

driver.get("https://automationpractice.techwithjatin.com/")
driver.maximize_window()
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in_a.click()
driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)
driver.find_element(By.ID, "SubmitCreate").click()
sleep(2)
if DATA_GENDER == Gender.FEMALE:
    driver.find_element(By.XPATH, "//label[@for='id_gender2']").click()
else:
    driver.find_element(By.XPATH, "//label[@for='id_gender1']").click()
#driver.quit()
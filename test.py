from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile

options = Options()
options.binary_location = "/snap/bin/chromium"

# CRITICAL for SNAP Chromium
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# CRITICAL: SNAP needs its own writable profile
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"),
    options=options
)

driver.get("https://google.com")

input("Press Enter to close...")
driver.quit()
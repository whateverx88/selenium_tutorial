from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile

options = Options()

# SNAP Chromium binary
options.binary_location = "/snap/bin/chromium"

# REQUIRED flags for SNAP
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# CRITICAL: unique profile directory
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"),
    options=options
)

driver.get("https://google.com")

input("Press Enter to close...")
driver.quit()
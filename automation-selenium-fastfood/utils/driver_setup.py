from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def init_driver():
    options = Options()
    options.add_argument("--start-maximized") #full screen

    # ⚡ Tạo profile riêng (chỉ cần tạo 1 lần duy nhất)
    profile_path = os.path.join(os.getcwd(), "selenium-profile")
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    # Prefs để tắt password manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver
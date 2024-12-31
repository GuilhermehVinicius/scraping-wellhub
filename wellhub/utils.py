from selenium import webdriver

def configure_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)

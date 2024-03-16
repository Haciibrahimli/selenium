from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time



options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://turbo.az")
time.sleep(5)
x = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-price')))
for i in range(len(x)):
    print(x[i].text)
driver.close()
# product-price




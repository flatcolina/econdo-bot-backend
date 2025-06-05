from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def criar_liberacao_econdo(nome, data_checkin, data_checkout):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    try:
        driver.get('https://app.econdos.com.br/')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-username-input']").send_keys('tiagoddantas@me.com')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-password-input']").send_keys('W3b12345')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-sign-in-button']").click()
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-occurrence-gate-button']").c

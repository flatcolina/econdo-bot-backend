import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def criar_liberacao_econdo(nome, data_checkin, data_checkout):
    print("Iniciando configuração do Chrome headless...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--single-process')

    print("Instalando e iniciando o ChromeDriver...")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    try:
        print("Acessando https://app.econdos.com.br/")
        driver.get('https://app.econdos.com.br/')
        time.sleep(1)

        print("Preenchendo usuário...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-username-input']").send_keys('tiagoddantas@me.com')
        print("Preenchendo senha...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-password-input']").send_keys('W3b12345')
        print("Clicando em Entrar...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-sign-in-button']").click()
        time.sleep(2)

        print("Clicando em Portaria...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-occurrence-gate-button']").click()
        time.sleep(1)

        print("Clicando em Criar liberação...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-open-liberation-modal-button']").click()
        time.sleep(1)

        print("Preenchendo nome...")
        driver.find_element(By.CSS_SELECTOR, ".form-control[placeholder='Ex: Diarista, personal trainer, churrasco, etc']").send_keys(nome)
        print("Preenchendo data inicial...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-start-date-input']").send_keys(data_checkin)
        print("Preenchendo data final...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-end-date-input']").send_keys(data_checkout)

        print("Clicando em Salvar...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-submit-button']").click()
        time.sleep(3)

        print("Buscando link de liberação...")
        link_elem = driver.find_element(By.CSS_SELECTOR, "[data-testid='share-link-target-link']")
        link = link_elem.text.strip()
        print("Link capturado:", link)
        return link
    except Exception as e:
        print("Erro no Selenium:", e)
        return None
    finally:
        print("Finalizando e fechando navegador.")
       

        driver.quit()

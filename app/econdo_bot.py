import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




def criar_liberacao_econdo(nome, data_checkin, data_checkout):
    print("Iniciando o processo de liberação no eCondo...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')

    # Caminho padrão do Chromium no Render. Se rodar local e der erro, comente essa linha.
    chrome_options.binary_location = "/usr/bin/chromium"

    print("Configurando driver do Chrome...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("Acessando o site eCondo...")
        driver.get('https://app.econdos.com.br/')
        time.sleep(2)

        print("Preenchendo login...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-username-input']").send_keys('tiagoddantas@me.com')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-password-input']").send_keys('W3b12345')
        driver.find_element(By.CSS_SELECTOR, "[data-testid='login-sign-in-button']").click()
        time.sleep(4)

        print("Acessando menu de portaria...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-occurrence-gate-button']").click()
        time.sleep(1)

        print("Abrindo modal de liberação...")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='feed-open-liberation-modal-button']").click()
        time.sleep(1)

        print("Preenchendo dados do hóspede...")
        driver.find_element(By.CSS_SELECTOR, ".form-control[placeholder='Ex: Diarista, personal trainer, churrasco, etc']").send_keys(nome)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-start-date-input']").send_keys(data_checkin)
        driver.find_element(By.CSS_SELECTOR, "[data-testid='create-authorized-person-end-date-input']").send_keys(data_checkout)

        print("Enviando cadastro...")
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
        driver.quit()

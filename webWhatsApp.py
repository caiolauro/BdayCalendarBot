from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

# object for chrome driver
class chromeDriver:
    PATH =  r"C:\Program Files (x86)\Google\chromedriver\chromedriver.exe"
    options = webdriver.ChromeOptions().add_argument(r"user-data-dir=C:\Program Files\Google\Chrome\Application")
    driver = webdriver.Chrome(PATH, options=options)

driver = chromeDriver.driver


def send_whatsapp_message(message:str,destiny_name:str="Notificado de Eventos"):

    # incializa google chrome abrindo página do WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    wait = WebDriverWait(driver, 300)

    # nome do contato ou grupo destinatário
    target = '"{}"'.format(destiny_name)
    try:
    # clicar no contato de destino
        x_arg = '//span[contains(@title,' + target + ')]'
        dst_title = wait.until(EC.presence_of_element_located(( 
        By.XPATH, x_arg))) 
        dst_title.click() 

    except ElementClickInterceptedException:
    # aciona JavaScript para scrollar até o início da página e evitar Interceptação
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # caminho XPATH para botão de envio de mensagem
    sendMessageXpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

    inputBox = wait.until(EC.presence_of_element_located((By.XPATH, sendMessageXpath)))
    inputBox.send_keys(message + Keys.ENTER) 
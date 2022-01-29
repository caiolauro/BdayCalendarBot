from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

from list_events import get_today_events
# object for chrome driver
class chromeDriver:
    PATH =  r"C:\Program Files (x86)\Google\chromedriver\chromedriver.exe"
    options = webdriver.ChromeOptions().add_argument(r"user-data-dir=C:\Program Files (x86)\Google\chromedriver")
    driver = webdriver.Chrome(PATH, options=options)

driver = chromeDriver.driver


def send_whatsapp_message(message:str,destiny_name:str="Notificado de Eventos"):

    # incializa google chrome abrindo página do WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    time.sleep(5)
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
    sendMessageXpath = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
    textBox = driver.find_element_by_css_selector(r"#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
    msgList = message.split('<scape>')
    
    for msg in msgList:
        
        textBox.send_keys(msg)
        textBox.send_keys(Keys.SHIFT, Keys.ENTER)

    time.sleep(1)

    inputBox = wait.until(EC.presence_of_element_located((By.XPATH, sendMessageXpath)))
    inputBox.send_keys(Keys.ENTER) 
    #driver.quit()
    print("Message sent")

send_whatsapp_message(get_today_events(),'Elis Cotosky')
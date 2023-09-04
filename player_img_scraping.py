from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import json

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)

acao = ActionChains(navegador)

navegador.get('https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1')

aceitar_cookies = navegador.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
aceitar_cookies.click()
sleep(2)
seletor = navegador.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select')
seletor.click()
acao.send_keys('a' + Keys.ENTER).perform()

lista = []
jogador = {}
total = 1

while True:
    if total > 539:
        break        
    nome = navegador.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr[{total}]/td[2]/a')
    url = nome.get_attribute('href')
    url = url.replace('https://www.nba.com/stats/player/', '')
    url = url.replace('/', '')
    img_url = f'https://cdn.nba.com/headshots/nba/latest/1040x760/{url}.png'
    jogador = {"id": total, "PName": nome.text, "img_url": img_url}
    print(f'{total} - {jogador["img_url"]}')
    lista.append(jogador.copy())
    total +=1

j = json.dumps(lista)

#creating a json file in the desired path
with open ("derised_path\\Players_List.json", "w") as f:
     f.write(j)

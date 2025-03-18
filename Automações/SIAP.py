import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Parâmetros import URL_SIAP, ID_SIAP, Senha_SIAP, xpaths_SIAP
from Funções import clicar_xpath, digitar_por_xpath, esperar_pagina_carregar
from time import sleep

navegador = webdriver.Chrome()

navegador.get(URL_SIAP)
navegador.maximize_window()

esperar_pagina_carregar(navegador=navegador)
digitar_por_xpath(navegador=navegador, xpath=xpaths_SIAP['campo login'], texto=ID_SIAP)
digitar_por_xpath(navegador=navegador, xpath=xpaths_SIAP['campo senha'], texto=Senha_SIAP)

tentativas = 0
while tentativas < 3:  # Limite de 3 tentativas para evitar loop infinito
    tentativas += 1

    # Captura o CAPTCHA
    captcha = navegador.find_element(By.XPATH, xpaths_SIAP['captcha'])
    digitar_por_xpath(navegador=navegador, xpath=xpaths_SIAP['captcha input'], texto=captcha.text)

    clicar_xpath(navegador=navegador, xpath=xpaths_SIAP['botão login'])

    # Aguarda até 3 segundos para verificar se a mensagem de erro aparece
    try:
        WebDriverWait(navegador, 3).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[3]/div/div/div/div[2]/div[2]/span[1]"))
        )
        print("Captcha incorreto, tentando novamente...")
        sleep(2)  # Aguarde um tempo antes de tentar de novo
    except:
        print("Login bem-sucedido ou outro erro ocorreu.")
        break  # Sai do loop se não houver mensagem de erro

esperar_pagina_carregar(navegador)
clicar_xpath(navegador=navegador, xpath=xpaths_SIAP['menu sistema'])
clicar_xpath(navegador=navegador, xpath=xpaths_SIAP['menu/freq'])

xpaths_turmas = [xpaths_SIAP[chave] for chave in ['6A', '6B', '7A', '7B', '8A', '8B', '9A', '6C']]

for turma in xpaths_turmas:
    clicar_xpath(navegador=navegador, xpath=turma)
    esperar_pagina_carregar(navegador)
    clicar_xpath(navegador, xpaths_SIAP['salvar e próximo'])

print('Presença lançada para TODOS os alunos.')
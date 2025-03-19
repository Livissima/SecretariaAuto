import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Automações.Parâmetros import path_base_faltas
from Parâmetros import URL_SIAP, ID_SIAP, Senha_SIAP, xpaths_SIAP, xpaths_turmas, path_database
from Funções import clicar_xpath, digitar_por_xpath, esperar_pagina_carregar
from time import sleep
import pandas as pd

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

base_estudantes = pd.read_excel(path_database)
base_estudantes = base_estudantes[['Matrícula', 'Estudante', 'Turma']]
df_faltas = pd.read_excel(path_base_faltas, sheet_name='Visão Faltas')
df_faltas = df_faltas[['Turma', 'Estudante', 'Data Falta', 'Lançado']]
df_faltas = df_faltas[df_faltas['Lançado'] == 'Lançado']

map_matrícula = base_estudantes.set_index('Estudante')['Matrícula']
df_faltas['Matrícula'] = df_faltas['Estudante'].map(map_matrícula)
print(df_faltas)



def localizar_clicar(navegador, turma):
    """
    Localiza e clica nos elementos de falta com base na turma e matrícula.
    """
    # Filtrar apenas as matrículas da turma atual
    matriculas_turma = df_faltas[df_faltas['Turma'] == turma]['Matrícula'].astype(str).tolist()

    # Aguardar a carga da lista de presença
    WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "itens")))

    # Localizar todos os "pontinhos" de presença/falta
    pontinhos = navegador.find_elements(By.CSS_SELECTOR, "div.itens div.item")

    if not pontinhos:
        print(f"⚠ Nenhum elemento encontrado para a turma {turma}")
        return

    total_cliques = 0

    for ponto in pontinhos:
        matricula = ponto.get_attribute("data-matricula")  # Capturar a matrícula

        if matricula in matriculas_turma:
            try:
                # Força o clique com JavaScript caso o Selenium não consiga
                navegador.execute_script("arguments[0].click();", ponto)
                sleep(0.5)  # Delay para evitar cliques muito rápidos
                total_cliques += 1
            except Exception as e:
                print(f"Erro ao clicar na matrícula {matricula}: {e}")

    print(f"✔ {total_cliques} faltas lançadas para a turma {turma}.")





for turma in xpaths_turmas:
    clicar_xpath(navegador=navegador, xpath=turma)  # Muda para a turma
    esperar_pagina_carregar(navegador=navegador)  # Aguarda carregamento

    localizar_clicar(navegador=navegador, turma=turma)  # Lança as faltas para a turma

    clicar_xpath(navegador=navegador, xpath=xpaths_SIAP['salvar e próximo'])  # Passa para a próxima turma

    sleep(5)

sleep(60*10)
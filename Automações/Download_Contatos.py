from time import sleep

import pyautogui
from pyautogui import click, moveTo
from pyautogui import hotkey as atalho
from Automação.Parâmetros import path_contatos
from Parâmetros import ID_SIGE, Senha_SIGE, URL_SIGE, path_fichas, chrome_options, start_time, data_completa, Turmas, Series, turmas_por_serie

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from keyboard import write as escrever
from pyautogui import press as tecla
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Funções
from Funções import voltar, selecionar_turma, selecionar_série, Sessão_downloads_fichas, menu_de_contatos

print(f'\nAutomação contatos iniciada em {data_completa}.')

# Iniciar o navegador com as opções configuradas
# navegador = webdriver.Chrome(options=chrome_options)


#######################################################################################################
#
# navegador.find_element('id', 'txtCPF').send_keys(ID_SIGE)
# navegador.find_element('id', 'txtSenha').send_keys(Senha_SIGE)
#
# navegador.find_element('id', 'cmdOK').click()
# print('Login realizado com sucesso.', end='\r')
# time.sleep(2)
#
# navegador.find_element('xpath', '//*[@id="mensagensSIGE"]/a').click()
#
#
# def select_option(dropdown_id, option_value=None, option_text=None):
#     # Espera até que o dropdown esteja presente
#     select_element = WebDriverWait(navegador, 10).until(
#         EC.presence_of_element_located((By.ID, dropdown_id))
#     )
#     select = Select(select_element)
#
#     if option_value:
#         select.select_by_value(option_value)
#     elif option_text:
#         select.select_by_visible_text(option_text)
#     else:
#         raise ValueError("You must provide either option_value or option_text.")

voltar()





menu_de_contatos()



for serie in Series:
    selecionar_série(serie)
    turmas_correspondentes = turmas_por_serie[serie]

    for turma in turmas_correspondentes:
        Sessão_downloads_fichas(turma, primeira_execucao)
        primeira_execucao = False


####################################################################################



print('Automação concluída.')
end_time1 = time.time()
print(f'    Tempo de execução do código: {end_time1 - start_time:.2f} segundos')


time.sleep(600)

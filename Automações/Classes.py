from time import sleep

import pyautogui
from pyautogui import click, moveTo


from Parâmetros import ID_SIGE, Senha_SIGE, URL_SIGE, path_fichas_casa, chrome_options, start_time, data_completa, path_contatos_casa
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from keyboard import write as escrever
from pyautogui import press as tecla


# Iniciar o navegador com as opções configuradas
print(f'\nAutomação iniciada em {data_completa}.')
navegador = webdriver.Chrome(options=chrome_options)
navegador.get(URL_SIGE)
navegador.maximize_window()
navegador.find_element('id', 'txtCPF').send_keys(ID_SIGE)
navegador.find_element('id', 'txtSenha').send_keys(Senha_SIGE)
navegador.find_element('id', 'cmdOK').click()

print('Login realizado com sucesso.', end='\r')

navegador.find_element('xpath', '//*[@id="mensagensSIGE"]/a').click()
sleep(2000)


def select_option(dropdown_id, option_value=None, option_text=None):
    # Espera até que o dropdown esteja presente
    select_element = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, dropdown_id))
    )
    select = Select(select_element)

    if option_value:
        select.select_by_value(option_value)
    elif option_text:
        select.select_by_visible_text(option_text)
    else:
        raise ValueError("You must provide either option_value or option_text.")



def clicar_marcar_todos():
    navegador.find_element('xpath', '/html/body/div[8]/form/table/tbody/tr[9]/td/table/tbody/tr[1]/td[1]/input').click()

def clicar_gerar():
    navegador.find_element('id', 'gerarRel').click()

def voltar():
    navegador.find_element('xpath', '/html/body/div[2]/img[1]').click()

def selecionar_série(série):
    select_option('cmbComposicao', option_value='199')
    select_option('cmbSerie', option_text=f'{série}º Ano')  # Corrigido de 'cmgSerie' para 'cmbSerie'
    select_option('cmbTurno', option_value='1')


def selecionar_turma(turma):
    select_option('cmbComposicao', option_value='199')
    select_option('cmbTurno', option_value='1')
    select_option('cmbTurma', option_text=turma)


def Sessão_downloads_fichas(turma, primeira_execucao):
    selecionar_turma(turma)
    clicar_marcar_todos()
    clicar_gerar()
    sleep(0.3)

    Imprimir()
    sleep(1.3)
    if primeira_execucao:
        # moveTo(x=1398, y=351, duration=0.3)
        # click(x=1398, y=351)
        # sleep(0.3)
        # tecla('p')
        # sleep(0.2)
        # tecla('tab', presses=3, interval=0.1)
        print('Seleciona layout de paisagem agora!!')
        sleep(10)
    else:
        pass

    tecla('enter')
    sleep(3)
    escrever(f'{turma}.pdf')

    sleep(0.5)
    clicar_no_endereço()
    escrever(path_fichas_casa)


    sleep(0.5)
    clicar_salvar()
    print(f'{turma}', end=' ')
    sleep(1.3)
    voltar()
    sleep(1.2)

def Sessão_downloads_contatos(turma, primeira_execucao):
    selecionar_turma(turma)
    clicar_gerar()
    sleep(0.3)

    Imprimir()

    if primeira_execucao:
        print('Selecione paisagem agora!!!!!!!')
        sleep(10)
    else:
        pass

    sleep(1.3)
    tecla('enter')
    sleep(2.5)
    escrever(f'{turma}.pdf')
    sleep(0.3)


    clicar_no_endereço()
    sleep(0.2)
    escrever(path_contatos_casa)

    sleep(0.3)
    clicar_salvar()
    print(f'{turma}', end=' ')
    sleep(1.3)
    voltar()
    sleep(1.2)


def clicar_no_endereço():
    pyautogui.hotkey('alt', 'e')

def clicar_salvar():
    ''''
    Executa hotkey(Alt + L) para clicar em Salvar,
    então 0,5s para executar hotkey (Alt + S) para confirmar.
    '''
    pyautogui.hotkey('alt', 'l')
    time.sleep(0.3)
    pyautogui.hotkey('alt', 's')
    time.sleep(0.9)

def Impressão():
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.moveTo(x=1398, y=351, duration=0.3)
    pyautogui.click(x=1398, y=351)
    time.sleep(0.3)
    pyautogui.hotkey('p')
    pyautogui.hotkey('tab', presses=3, interval=0.1)
    pyautogui.hotkey('enter')

def menu_de_fichas():
    pyautogui.moveTo(x=792, y=281, duration=0.2)
    pyautogui.moveTo(x=793, y=372, duration=0.2)
    pyautogui.moveTo(x=995, y=367, duration=0.2)
    pyautogui.moveTo(x=1175, y=372, duration=0.2)
    pyautogui.moveTo(x=1166, y=404, duration=0.2)
    pyautogui.click(x=1166, y=404)
    print('• PDFs de Fichas salvos:')

def menu_de_contatos():
    pyautogui.moveTo(x=792, y=281, duration=0.2)
    pyautogui.moveTo(x=793, y=372, duration=0.2)
    pyautogui.moveTo(x=995, y=367, duration=0.2)
    pyautogui.moveTo(x=1199, y=375, duration=0.2)
    pyautogui.moveTo(x=1124, y=535, duration=0.2)
    pyautogui.click(x=1124, y=535)
    time.sleep(1.5)
    print('Relatórios de Contatos:')


def Imprimir():
    pyautogui.hotkey('ctrl', 'p')

def clicar_marcar_todos():
    navegador.find_element('xpath', '/html/body/div[8]/form/table/tbody/tr[9]/td/table/tbody/tr[1]/td[1]/input').click()

def clicar_gerar():
    navegador.find_element('id', 'gerarRel').click()

def voltar():
    navegador.find_element('xpath', '/html/body/div[2]/img[1]').click()


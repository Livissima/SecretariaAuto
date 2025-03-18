from Parâmetros import pasta_generos, pasta_fichas, pasta_situações, pasta_contatos
from Parâmetros import ID_SIGE, Senha_SIGE, URL_SIGE, chrome_options, data_completa, xpaths_SIGE, hoje

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from keyboard import write as escrever
from pyautogui import press as tecla
from typing import Literal
from time import sleep
import pyautogui
from pyautogui import click, moveTo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import StaleElementReferenceException






#-----------------------------------------------------
#-----------------------------------------------------
# Funções --------------------------------------------





# Configuração básica do logging
logging.basicConfig(level=logging.WARNING)  # Mude para INFO se quiser ver mensagens de info

def clicar_xpath(navegador, xpath: str):
    """Função para localizar e clicar num elemento a partir do xpath, aguardando até que o elemento esteja clicável."""
    try:
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        # logging.info(f"Clicou no elemento: {xpath}")  # Use logging em vez de print
    except Exception as e:
        logging.error(f"Erro ao clicar no elemento: {xpath}. Erro: {e}")  # Registra erros



def clicar_id(navegador, ID: str):
    """Função para localizar e clicar num elemento a partir do ID HTML, aguardando até que o elemento esteja clicável."""
    try:
        # Aguarda até que o elemento esteja presente e clicável
        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, ID)))
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.ID, ID)))
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, ID))).click()
    except Exception as e:
        print(f"Erro ao clicar no elemento com ID: {ID}. Erro: {e}")  # Você pode manter esta linha para capturar erros


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from time import sleep

def digitar_por_xpath(navegador, xpath: str, texto: str):
    """Função para localizar um campo por XPath e enviar texto, aguardando até que o campo esteja clicável."""
    for _ in range(3):  # Tenta até 3 vezes
        try:
            # Aguarda até que o elemento esteja presente, visível e habilitado
            element = WebDriverWait(navegador, 10).until(
                lambda driver: driver.find_element(By.XPATH, xpath) if driver.find_element(By.XPATH, xpath).is_enabled() else None
            )

            element.clear()  # Limpa o campo antes de digitar (se necessário)
            element.send_keys(texto)  # Envia o texto

            break  # Sai do loop se a operação for bem-sucedida
        except StaleElementReferenceException:
            print(f"Elemento stale, tentando novamente: {xpath}")
            sleep(1)  # Espera um pouco antes de tentar novamente
        except TimeoutException:
            print(f"Tempo limite excedido para encontrar o elemento: {xpath}")
            break
        except Exception as e:
            print(f"Erro ao digitar no campo com XPath: {xpath}. Erro: {e}")
            break  # Sai do loop em caso de erro diferente




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
    """Função Selenium. Clica na checkbox de marcar todos.
    Localiza elemento por xpath.
    """
    clicar_xpath(xpath=xpaths_SIGE['caixa de marcar todos'])

def clicar_gerar():
    """Função Selenium. Clica no botão de gerar relatório e esperar para printar. Localiza elemento por ID. """
    clicar_id('gerarRel')
    sleep(1)


def selecionar_série(série):
    """"
    Sequência de funções Selenium.
    Seleciona as opções de Série nos campos de dropdown.
    """
    select_option('cmbComposicao', option_value='199')
    select_option('cmbSerie', option_text=f'{série}º Ano')  # Corrigido de 'cmgSerie' para 'cmbSerie'
    select_option('cmbTurno', option_value='1')


def selecionar_turma(turma):
    """"
    Sequência de funções Selenium.
    Seleciona as opções de Turma nos campos de dropdown.
    """
    select_option('cmbComposicao', option_value='199')
    select_option('cmbTurno', option_value='1')
    select_option('cmbTurma', option_text=turma)

def definir_layout_por_click():
    """Função pyautogui para clicar em Layout e pressionar 'P' e apertar tab 3x para posicionar sobre SALVAR"""
    moveTo(x=1398, y=351, duration=0.3)
    click(x=1398, y=351)
    sleep(0.3)
    tecla('p')
    sleep(0.2)
    tecla('tab', presses=3, interval=0.1)


def clicar_no_endereço():
    """Função de atalho (Alt + E) para clicar na barra de endereço."""
    pyautogui.hotkey('alt', 'e')


def clicar_salvar():
    """
    Executa hotkey(Alt + L) para clicar em Salvar,
    então 0,5s para executar hotkey (Alt + S) para confirmar a substituição.
    """
    pyautogui.hotkey('alt', 'l')
    time.sleep(0.3)
    pyautogui.hotkey('alt', 's')
    time.sleep(1)


def menu_de_fichas():
    """Função pyautogui para chegar na tela de gerar relatórios de fichas cadastrais."""
    clicar_xpath(xpath=xpaths_SIGE['lápis documentos'])
    clicar_xpath(xpath=xpaths_SIGE['doc/relatórios'])
    clicar_xpath(xpath=xpaths_SIGE['rel/dados cadastrais'])
    clicar_xpath(xpath=xpaths_SIGE['dad/fichas do aluno'])
    print('• PDFs de Fichas salvos:')


def menu_de_contatos():
    """Função pyautogui para chegar na tela de gerar relatórios de fichas cadastrais."""
    clicar_xpath(xpath=xpaths_SIGE['lápis documentos'])
    clicar_xpath(xpath=xpaths_SIGE['doc/relatórios'])
    clicar_xpath(xpath=xpaths_SIGE['rel/dados cadastrais'])
    clicar_xpath(xpath=xpaths_SIGE['dad/contatos'])
    print('Relatórios de Contatos:')

def menu_de_situações():
    clicar_xpath(xpath=xpaths_SIGE['lápis documentos'])
    clicar_xpath(xpath=xpaths_SIGE['doc/relatórios'])
    clicar_xpath(xpath=xpaths_SIGE['rel/alunos'])
    clicar_xpath(xpath=xpaths_SIGE['alu/situação'])

def menu_de_gêneros():
    clicar_xpath(xpath=xpaths_SIGE['lápis documentos'])
    clicar_xpath(xpath=xpaths_SIGE['doc/relatórios'])
    clicar_xpath(xpath=xpaths_SIGE['rel/acomp pedagógico'])
    clicar_xpath(xpath=xpaths_SIGE['aco/alunos por idade'])


def esperar_pagina_carregar(navegador):
    """Aguarda até que a página esteja completamente carregada."""
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))  # Aguarda o corpo da página estar presente
    WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))  # Aguarda o corpo da página estar visível

def Imprimir():
    """Atalho simples (Ctrl + P)"""
    esperar_pagina_carregar()  # Aguarda a página carregar completamente
    pyautogui.hotkey('ctrl', 'p')  # Executa o atalho de impressão

def voltar(tipo_de_relatório: Literal['Fichas', 'Contatos', 'Gênero', 'Situações']):
    """
    Função Selenium. Clica no botão de voltar.
    Localiza elemento por xpath.
    """
    if tipo_de_relatório == 'Fichas' or tipo_de_relatório == 'Contatos':
        clicar_xpath(xpath=xpaths_SIGE['botão voltar F, C'])
    elif tipo_de_relatório == 'Situações' or tipo_de_relatório == 'Gênero':
        clicar_xpath(xpath=xpaths_SIGE['botão voltar S, G'])


def salvar_printar(turma):
    """Função simples para agrupar sequência de comandos de salvar, confirmar, printar nome do último arquivo e
    então clicar em Voltar."""
    clicar_salvar()
    print(f'{turma}', end=' ')
    sleep(0.3)

def preencher_path(tipo_de_relatório: Literal['Fichas', 'Contatos', 'Gênero', 'Situações']):
    """Função Pyautogui e Keyboard.
    Atalho simples de (Ctrl + E) para clicar na barra de endereço e preencher com o path do respectivo relatório."""
    clicar_no_endereço()
    sleep(0.2)
    caminhos = {
        'Fichas': pasta_fichas,
        'Situações': pasta_situações,
        'Gênero': pasta_generos,
        'Contatos': pasta_contatos
    }
    path_pasta = caminhos.get(tipo_de_relatório)
    escrever(path_pasta)
    sleep(0.3)

def preencher_nome(turma):
    """sleep por 3 segundos, preenche o nome e sleep again"""
    sleep(3)
    escrever(f'{turma}.pdf')
    sleep(0.5)


def Sessão_downloads_fichas(turma, primeira_execucao):
    """
    Sequência de ações automatizadas por Selenium e Pyautogui.
    Execução em loop, quando na tela de gerar relatórios de fichas cadastrais.
    Seleciona as turmas disponíveis na lista dada, marca todos os estudantes, solicita impressão,
    confirma impressão, nomeia o arquivo e conclui o armazenamento do PDF.
    Na primeira execução, o layout é definido para paisagem com pyautogui.
    """
    selecionar_turma(turma)
    clicar_marcar_todos()
    clicar_gerar()

    Imprimir()
    sleep(1.3)

    if primeira_execucao:
        definir_layout_por_click()

    tecla('enter')
    preencher_nome(turma=turma)

    if primeira_execucao:
        preencher_path('Fichas')

    salvar_printar(turma=turma)
    voltar('Fichas')


def Sessão_downloads_contatos(turma, primeira_execucao):
    """
    Sequência de ações automatizadas por Selenium e Pyautogui.
    Execução em loop, quando na tela de gerar relatórios contatos.
    Seleciona as turmas disponíveis na lista dada, marca todos os estudantes, solicita impressão,
    confirma impressão, nomeia o arquivo e conclui o armazenamento do PDF.
    Na primeira execução, o layout é definido para paisagem com pyautogui.
    """
    selecionar_turma(turma)
    clicar_gerar()

    Imprimir()

    if primeira_execucao:
        definir_layout_por_click()


        #Alternativa para ajuste manual --------------
        # print('Selecione paisagem agora!!!!!!!')
        # sleep(10)

    sleep(1.3)
    tecla('enter')
    preencher_nome(turma=turma)

    if primeira_execucao:
        preencher_path('Contatos')
    salvar_printar(turma=turma)
    voltar('Contatos')


def Sessão_downloads_situações(turma, primeira_execucao):
    """
    Sequência de ações automatizadas por Selenium e Pyautogui.
    Execução em loop, quando na tela de gerar relatórios de situações.
    Seleciona as turmas disponíveis na lista dada, solicita impressão,
    confirma impressão, nomeia o arquivo e conclui o armazenamento do PDF.
    Na primeira execução, o layout é definido para paisagem com pyautogui.
    """
    selecionar_turma(turma)
    clicar_gerar()

    Imprimir()

    if primeira_execucao:
        definir_layout_por_click()

    sleep(1.3)
    tecla('enter')

    preencher_nome(turma=turma)

    if primeira_execucao:
        preencher_path('Situações')
    salvar_printar(turma=turma)
    voltar('Situações')

def Sessão_downloads_gêneros(turma, primeira_execucao):
    """
    Sequência de ações automatizadas por Selenium e Pyautogui.
    Execução em loop, quando na tela de gerar relatórios de gênero.
    Seleciona as turmas disponíveis na lista dada, solicita impressão,
    confirma impressão, nomeia o arquivo e conclui o armazenamento do PDF.
    Na primeira execução, o layout é definido para paisagem com pyautogui.
    """
    selecionar_turma(turma)
    digitar_por_xpath(xpath=xpaths_SIGE['api/data ref'], texto=hoje)
    clicar_gerar()

    Imprimir()

    if primeira_execucao:
        definir_layout_por_click()

    sleep(1.3)
    tecla('enter')

    preencher_nome(turma=turma)

    if primeira_execucao:
        preencher_path('Gênero')
    salvar_printar(turma=turma)
    voltar('Gênero')



#---------------------------------------------
# Inicialização.
if __name__ == "__main__":
    print(f'\nAutomação iniciada em {data_completa}.')
    navegador = webdriver.Chrome(options=chrome_options)
    navegador.get(URL_SIGE)
    navegador.maximize_window()
    navegador.find_element('id', 'txtCPF').send_keys(ID_SIGE)
    navegador.find_element('id', 'txtSenha').send_keys(Senha_SIGE)
    navegador.find_element('id', 'cmdOK').click()

    print('Login realizado com sucesso.', end='\r')
    clicar_xpath(xpaths_SIGE['janela de alertas'])
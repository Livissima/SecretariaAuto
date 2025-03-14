import time
start_time = time.time()
import pyautogui
from selenium.webdriver.chrome.options import Options
import json
from datetime import datetime



data_completa                 = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")
hoje                          = datetime.now().strftime('%d/%m/%Y')

data_completa_nome_de_arquivo = datetime.now().strftime("%H_%M_%S, %d_%m_%Y")

Turmas = ['6A', '6B', '6C', '7A', '7B', '8A', '8B', '9A']
Series = ['6', '7', '8', '9']


turmas_por_serie = {
    '6': ['6A', '6B', '6C'],
    '7': ['7A', '7B'],
    '8': ['8A', '8B'],
    '9': ['9A']
}

xpaths = {
    'janela de alertas'    : '//*[@id="mensagensSIGE"]/a',
    'caixa de marcar todos': '/html/body/div[8]/form/table/tbody/tr[9]/td/table/tbody/tr[1]/td[1]/input',
    'botão voltar F, C'    : '/html/body/div[2]/img[1]',
    'botão voltar S, G'    : '/html/body/div[1]/img[1]',
    'lápis documentos'     : '/html/body/div[7]/ul/li[4]/h4/a',
    'doc/relatórios'       : '/html/body/div[7]/ul/li[4]/ul/li[2]/a',
    'rel/dados cadastrais' : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[1]/a',
    'rel/acomp pedagógico' : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[3]/a',
    'rel/alunos'           : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[2]/a',
    'alu/situação'         : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[2]/ul/li[2]/a',
    'aco/alunos por idade' : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[3]/ul/li[6]/a',
    'dad/fichas do aluno'  : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[2]/a',
    'dad/contatos'         : '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[6]/a',
    'api/data ref'         : '/html/body/div[8]/form/table/tbody/tr[6]/td[2]/input'
}




#####################################################SIAP
ID_SIAP = ''
Senha_SIAP = ''
URL_SIAP = r'https://siap.educacao.go.gov.br/FrequenciaDiaria.aspx'

#####################################SIGE
ID_SIGE    = '802.930.181-20'
Senha_SIGE = '23112006'
path_fichas = r'C:\Users\meren\OneDrive - Secretaria de Estado da Educação\Secretaria\2025\Dados\Estudantes\Base de dados\Fichas'
path_fichas_casa = r'C:\Users\livia\Desktop\pastas\fichas'
path_contatos = r'C:\Users\meren\OneDrive - Secretaria de Estado da Educação\Secretaria\2025\Dados\Estudantes\Base de dados\Contatos'
path_contatos_casa = r'C:\Users\livia\Desktop\pastas\Contatos'

URL_SIGE = 'https://sige.educacao.go.gov.br/sige/login.asp'






######################### Config de impressão
chrome_options = Options()
settings = {
    "recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,  # Cabeçalhos e rodapés desativados
    "scalingType": 3,
    "scaling": "60",  # Escala de 60%
    "mediaSize": {"height_microns": 210000, "width_microns": 297000, "name": "ISO_A4", "is_continuous_feed": False},
    "landscape": True,  # Layout paisagem
    "backgroundGraphicsEnabled": False  # Elementos gráficos de fundo desativados
}

prefs = {
    "printing.print_preview_sticky_settings.appState": json.dumps(settings),
    "savefile.default_directory": path_fichas  # Define o diretório de salvamento
}

chrome_options.add_experimental_option("prefs", prefs)

################################################



from Parâmetros import turmas_por_serie, Series, start_time
from Funções import (menu_de_fichas, selecionar_série, Sessão_downloads_fichas, Sessão_downloads_contatos,
                     menu_de_contatos, menu_de_situações, Sessão_downloads_situações, Sessão_downloads_gêneros,
                     menu_de_gêneros)
import time

from time import sleep


#-----------------------------------------------------------------------
# 1º Etapa: Download de fichas cadastrais

menu_de_fichas()

primeira_execucao = True
for serie in Series:
    selecionar_série(serie)
    turmas_correspondentes = turmas_por_serie[serie]
    for turma in turmas_correspondentes:
        Sessão_downloads_fichas(turma, primeira_execucao)
        primeira_execucao = False
end_time_fichas = time.time()
sleep(1)

print('')
print(f'    Tempo para extrair as fichas: {(end_time_fichas - start_time)/60:.2f} minutos')

#-----------------------------------------------------------------------
# 2º Etapa: Download de relatórios de contatos

menu_de_contatos()

print('PDFs de contatos:')

primeira_execucao = True
for serie in Series:
    selecionar_série(serie)
    turmas_correspondentes = turmas_por_serie[serie]
    for turma in turmas_correspondentes:
        Sessão_downloads_contatos(turma, primeira_execucao)
        primeira_execucao = False

end_time_contatos = time.time()
sleep(1)
print('')
print(f'    Tempo para extrair os contatos: {(end_time_contatos - end_time_fichas)/60:.2f} minutos')

#-----------------------------------------------------------------------
# 3º Etapa: Download de relatórios de situações

menu_de_situações()

print('PDFs de Situações:')

primeira_execucao = True
for serie in Series:
    selecionar_série(serie)
    turmas_correspondentes = turmas_por_serie[serie]
    for turma in turmas_correspondentes:
        Sessão_downloads_situações(turma, primeira_execucao)
        primeira_execucao = False

end_time_situações = time.time()
sleep(1)
print('')
print(f'    Tempo para extrair as situações: {(end_time_situações - end_time_contatos)/60:.2f} minutos')

#-------------------------------------------------------------------------------
# 4º Etapa: Download de relatórios de gênero

menu_de_gêneros()

print('Pdfs de Situações')

primeira_execucao = True
for serie in Series:
    selecionar_série(serie)
    turmas_correspondentes = turmas_por_serie[serie]
    for turma in turmas_correspondentes:
        Sessão_downloads_gêneros(turma, primeira_execucao)
        primeira_execucao = False

end_time_gêneros = time.time()
sleep(1)
print('')

print(f'    Tempo para extrair os gêneros: {(end_time_gêneros - end_time_situações)/60:.2f} minutos')

sleep(1000)







#________________
#Construindo função das funções
# def baixar_relatórios(local_do_menu, sessão):
#
#     for serie in Series:
#         selecionar_série(serie)
#         turmas_correspondentes = turmas_por_serie[serie]
#         for turma in turmas_correspondentes:
#             sessão
#             primeira_execucao = False
#     end_dessa_parte = time.time()
#     sleep(1)

import pyautogui
from selenium import webdriver
from Parâmetros import URL_SIAP, ID_SIAP, Senha_SIAP, xpaths_SIAP
from Funções import clicar_xpath, select_option, digitar_por_xpath, esperar_pagina_carregar
from time import sleep

navegador = webdriver.Chrome()

navegador.get(URL_SIAP)
navegador.maximize_window()


digitar_por_xpath(navegador=navegador, xpath=xpaths_SIAP['campo senha'], texto=ID_SIAP)
digitar_por_xpath(navegador=navegador, xpath=xpaths_SIAP['campo senha'], texto=Senha_SIAP)

captcha = navegador.find_element('xpath', xpaths_SIAP['captcha'])
digitar_por_xpath(navegador=navegador, xpath=xpaths_SIAP['captcha input'], texto=captcha)
clicar_xpath(navegador=navegador, xpath=xpaths_SIAP['botão login'])

print(captcha.text)



sleep(1000)
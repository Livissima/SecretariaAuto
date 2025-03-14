import pyautogui
from selenium import webdriver
from Parâmetros import URL_SIAP, ID_SIAP, Senha_SIAP

navegador = webdriver.Chrome()

navegador.get(URL_SIAP)

navegador.maximize_window()

navegador.find_element('id', '').send_keys(ID_SIAP)
navegador.find_element('id', '').send_keys(Senha_SIAP)

navegador.find_element('id', '').click()


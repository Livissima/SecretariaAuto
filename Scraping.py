from Parâmetros import ID_SIGE, Senha_SIGE, URL_SIGE
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()

navegador.get(URL_SIGE)

navegador.maximize_window()

navegador.find_element('id', 'txtCPF').send_keys(ID_SIGE)
navegador.find_element('id', 'txtSenha').send_keys(Senha_SIGE)
navegador.find_element('id', 'cmdOK').click()

sleep(2)

#Close
navegador.find_element('xpath', '//*[@id="mensagensSIGE"]/a').click()
sleep(2)

#Lapis docs
navegador.find_element('class name', 'documentos').click()
sleep(2)

#Relatórios
navegador.find_element('xpath', '/html/body/div[7]/ul/li[4]/ul/li[2]/a').click()
sleep(2)

#Dados cadastrais
navegador.find_element('xpath', '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[1]/a').click()
sleep(3)

#Fichas
navegador.find_element('xpath', '/html/body/div[7]/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[2]').click()
sleep(1)


#Composição
# Function to select an option from a dropdown
def select_option(dropdown_id, option_value=None, option_text=None):
    select_element = navegador.find_element('id', dropdown_id)
    select = Select(select_element)

    if option_value:
        select.select_by_value(option_value)
    elif option_text:
        select.select_by_visible_text(option_text)
    else:
        raise ValueError("You must provide either option_value or option_text.")


# Select options from dropdowns
select_option('cmbComposicao', option_value='199')  # Select by value
select_option('cmbSerie', option_text='6º Ano')  # Select by visible text
select_option('cmbTurno', option_value='1')  # Select by value

# Wait for the 'cmbTurma' dropdown to be populated
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, 'cmbTurma'))
)

# Now select an option from the 'cmbTurma' dropdown
# After waiting, select an option from the 'cmbTurma' dropdown
turma_select = Select(navegador.find_element('id', 'cmbTurma'))

# Get all options and filter out the default option
turma_options = [option for option in turma_select.options if
                 option.get_attribute('value') != '0']  # Exclude the default option

if turma_options:
    turma_select.select_by_value(turma_options[0].get_attribute('value'))  # Select the first available option
else:
    print("No options available in 'cmbTurma'.")

#Marcar todos
navegador.find_element('xpath', '/html/body/div[8]/form/table/tbody/tr[9]/td/table/tbody/tr[1]/td[1]/input').click()

#Gerar relatório
navegador.find_element('id', 'gerarRel').click()

#Print
navegador.find_element('xpath', '/html/body/div[2]/img[2]').click()

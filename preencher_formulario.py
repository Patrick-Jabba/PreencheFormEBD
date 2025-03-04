import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Ler CPFs do arquivo
with open("cpfs.txt", "r", encoding="utf-8") as f:
    cpfs = [line.strip() for line in f.readlines()]

# Ler texto de participação do arquivo
with open("participacao.txt", "r", encoding="utf-8") as f:
    participacao_texto = f.read().strip()

# Abrir o site
url = "https://www.igrejacristamaranata.org.br/ebd/participacoes/"
driver.get(url)
time.sleep(3)  # Tempo para a página carregar completamente

for cpf in cpfs:
    print(f"Preenchendo formulário para CPF: {cpf}")

    # Preencher CPF
    cpf_input = driver.find_element(By.NAME, "icm_member_cpf")
    cpf_input.clear()
    cpf_input.send_keys(cpf)
    time.sleep(2)  # Espera os dados serem carregados automaticamente

    # Função para preencher um campo selectize digitando o valor e pressionando Enter
    def preencher_selectize(campo_placeholder, valor):
        try:
            # Localizar o campo de entrada real dentro do selectize
            campo_selectize = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'selectize-input') and .//input[@placeholder='{campo_placeholder}']]//input"))
            )

            # Rolar até o elemento para garantir que ele esteja visível
            driver.execute_script("arguments[0].scrollIntoView(true);", campo_selectize)
            time.sleep(1)  # Pequena pausa após rolar

            # Forçar foco no campo usando JavaScript
            driver.execute_script("arguments[0].focus();", campo_selectize)

            # Limpar o campo e enviar o texto do valor desejado
            campo_selectize.clear()
            campo_selectize.send_keys(valor)

            # Pressionar Enter para confirmar a seleção
            campo_selectize.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Erro ao preencher campo '{campo_placeholder}' com valor '{valor}': {e}")
            raise

    # Selecionar "Membro" no campo Função
    preencher_selectize("Escolha uma função", "Membro")

    # Selecionar "Participação Individual" no campo Trabalho
    preencher_selectize("Escolha uma Trabalho", "Participação Individual")

    # Selecionar a categoria "Participação"
    categoria_participacao = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='icm_member_categoria' and @value='2']"))
    )
    categoria_participacao.click()
    time.sleep(1)

    # Preencher o campo de texto no Quill Editor
    try:
        # Localizar o campo de texto do Quill Editor
        campo_participacao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ql-editor"))
        )

        # Limpar o campo (se necessário)
        driver.execute_script("arguments[0].innerHTML = '';", campo_participacao)

        # Enviar o texto da participação
        campo_participacao.send_keys(participacao_texto)
    except Exception as e:
        print(f"Erro ao preencher o campo de participação: {e}")
        raise

    # Marcar o checkbox "Li e estou de Acordo com o Termo"
    try:
        checkbox_acordo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "aceitoOsTermos"))
        )

        # Rolar até o elemento para garantir que ele esteja visível
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox_acordo)
        time.sleep(1)  # Pequena pausa após rolar

        # Tentar clicar no checkbox usando JavaScript se o clique normal falhar
        driver.execute_script("arguments[0].click();", checkbox_acordo)
    except Exception as e:
        print(f"Erro ao marcar o checkbox 'Li e estou de Acordo com o Termo': {e}")
        raise

    # Clicar no botão "Enviar participação"
    botao_enviar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-submit"))
    )
    botao_enviar.click()
    time.sleep(3)  # Espera a página processar antes de preencher o próximo CPF

    # Atualizar a página para o próximo CPF
    driver.get(url)
    time.sleep(3)

# Fechar o navegador após processar todos os CPFs
driver.quit()
print("Todos os formulários foram preenchidos com sucesso! 🚀")
# Passo a passo do projeto

# 1. Abrir o sistema da empresa
     # https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmxfY1ZYN3ZGVWhMQXhNMXVETjM3VnB2TWthUXxBQ3Jtc0ttM3hXYkYyMVdQM3BySVVjcmhEWVN6VXh2R0NTVW43RGZUdDBLcWgycGJTcWE5cVQ4S25WTEk5b05MNGotTjNhV3pabHFFMk9MWmxqRUlVelhhRXRyeXR3V2cxeDN1WXR6QXJ5QTVPVkxISHBlOGVVaw&q=https%3A%2F%2Fdlp.hashtagtreinamentos.com%2Fpython%2Fintensivao%2Flogin&v=qc39uUfYraQ

# para instalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> click com o mouse
# pyautogui.white -> escreve um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey ->apertar um conjunto de teclas ( Ctrl C,V,Alt)

# abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)


# 2. Fazer login
pyautogui.click(x=571, y=447)
pyautogui.write("python@gmail.com")

pyautogui.press("tab") #passo para o campo de senha
pyautogui.write("sua senha aqui")

pyautogui.press("tab") # passou para o botao de login
pyautogui.press("enter")

time.sleep(3)

# 3.Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)


# 4.Cadastrar um produto
# STR = STRING = texto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do código do produto
    pyautogui.click(x=274, y=382)
    # preencher o codigo
    pyautogui.write(codigo)
    # passar pro proximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passar pro proximo campo
    pyautogui.press("tab")
    # apertar o botao
    pyautogui.press("enter")

    pyautogui.scroll(5000)


# 5. Repetir isso tudo até acabar a lista de produtos
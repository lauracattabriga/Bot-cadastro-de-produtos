import pyautogui
import time
import pandas

# pyautogui.click -> clica
# pyautogui.write -> escreve
# pyautogui.press -> pressiona uma tecla
# pyautogui.hotkey -> pressiona um atalho (ex: ctrl+c)
pyautogui.PAUSE = 0.5  # tempo de espera entre cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir o navegador e acessar o link
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Clicar no campo de email e senha
pyautogui.click(x=-1132, y=176)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")

pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

#Cadastrar os produtos
    pyautogui.click(x=-1155, y=29)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
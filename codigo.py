import pyautogui
import time

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
pyautogui.click(x=-1139, y=299)
pyautogui.write("123456")
pyautogui.click(x=-807, y=375)

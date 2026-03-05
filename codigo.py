import pyautogui

# pyautogui.click -> clica
# pyautogui.write -> escreve
# pyautogui.press -> pressiona uma tecla
# pyautogui.hotkey -> pressiona um atalho (ex: ctrl+c)
pyautogui.PAUSE = 0.5  # tempo de espera entre cada comando

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
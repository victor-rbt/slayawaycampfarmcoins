import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
def buscar_cor_tela(cor):
    captura = pyautogui.screenshot()

    x = 190
    while x < 610:
        cor_encontrada = captura.getpixel((x, 495))
        if cor_encontrada == cor:
            return True

        x += 1

    return False

for indice in range(10000):
    if buscar_cor_tela((255, 0, 0)):
        pyautogui.click()

    try:
        pyautogui.locateOnScreen('atabou.png')
        pyautogui.click(x=575, y=535)
    except:
        pass
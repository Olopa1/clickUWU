import pyautogui as pgui

while True:
    posX, posY = pgui.position()
    print(f"X : {posX} Y: {posY}")
import pyperclip as pyc
import pyautogui as pgui

def copyToClipboard():
    pgui.press(['ctrl','c'])
    pgui.keyUp(['ctrl','c'])
    validateClipboard()

def validateClipboard():
    text = pyc.paste()
    text.replace
    notValidChars = [ '#', '"', '*', ':', '<', '>', '?', '/', '\\', '|']
    for i in notValidChars:
        text.replace(i,' ')
    pyc.copy(text)
    
def pasteFromClipboard():
    pgui.press(['ctrl','v'])
    pgui.keyUp(['ctrl','v'])
    
def click(posX,posY,clicks,delay,action):
    pgui.moveTo(posX,posY)
    if clicks > 0:
        for i in range(clicks):
            pgui.click()
    if action == 1:
        copyToClipboard()
    elif action == 2:
        pasteFromClipboard()
        
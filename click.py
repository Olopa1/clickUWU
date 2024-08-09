import pyperclip as pyc
import pyautogui as pgui
import time

def copyToClipboard():
    text = pyc.paste()
    pgui.hotkey("ctrl","c")
    validateClipboard()
    checkForRepeat(text)


def validateClipboard():
    text = pyc.paste()
    text.replace
    notValidChars = [ '#', '"', '*', ':', '<', '>', '?', '/', '\\', '|']
    for i in notValidChars:
        text.replace(i,' ')
    pyc.copy(text)
    
def pasteFromClipboard():
    pgui.hotkey("ctrl","v")

def checkForRepeat(text):
    if text == pyc.paste():
        exit(0)

def click(posX,posY,clicks,delay,action):
    pgui.moveTo(posX,posY)
    if clicks > 0:
        for i in range(clicks):
            pgui.click()
    if action == 1:
        copyToClipboard()
    elif action == 2:
        pasteFromClipboard()
    if delay > 0:
        time.sleep(delay)
        
def main():
    time.sleep(5)
    click(393,354,3,4,1)
    click(974,64,1,1,2)

main()
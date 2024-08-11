import pyperclip as pyc
import pyautogui as pgui
import time
import os

def copyToClipboard():
    text = pyc.paste()
    pgui.hotkey("ctrl","c")
    validateClipboard()
    checkForRepeat(text)

def killPopUpProcess(processName):
    os.system("tasklist | findstr " + processName + " > isRunning.txt")
    f = open("isRunning.txt" ,"r")
    isLine = f.readline()
    f.close()
    if isLine == "":
        return
    os.system("taskkill /IM " + '"' + processName +'"' + "/F")

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
        pgui.alert(text="Koniec programu" , title="Koniec", button="OK")
        exit(0)

def click(posX,posY,clicks,delay,action):
    killPopUpProcess("adobeReader.exe")
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
    killPopUpProcess("adobeReader.exe")
        
def main():
    time.sleep(5)
    while True:
        click(303,206,3,1,1)
        click(3271,211,1,1,0)
        click(2785,131,1,1,0)
        click(2372,1139,1,0,0)
        click(2372,1139,0,1,2)
        click(995,684,1,2,0)
        click(3410,26,1,1,0)
        click(2906,127,1,1,0)
        click(3407,783,1,2,0)
        
            
main()
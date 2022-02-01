from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

conf = 0.85
pressButtonSpeed = 0.5

varAct = 0
varWait = 0

varBasicSkill = 0
varGuts = 0



#qual botao e quantas vezes apertar

def pressButton(button, times): 
    if button == 'Down':
        while(times != 0):
            keyboard.press('s')
            time.sleep(0.05)
            keyboard.release('s')
            time.sleep(pressButtonSpeed)
            times = times - 1
        
    if button == 'Circle':
        while(times != 0):
            keyboard.press('l')
            time.sleep(0.05)
            keyboard.release('l')
            time.sleep(pressButtonSpeed)
            times = times - 1

#funcao para selecionar actions
            
def selectAct():
    while keyboard.is_pressed('x') == False:
        varAct = pyautogui.locateOnScreen('status.png', confidence = conf, grayscale = True)
        if varAct != None:
            pressButton('Down', 1)
            time.sleep(0.5)
            pressButton('Circle', 1)
            time.sleep(0.5)
            break

#funcao para usar accumulate
        
def accumulate():  
    #seleciona basic skill/guts e depois accumulate
    while keyboard.is_pressed('x') == False:
        varBasicSkill = pyautogui.locateOnScreen('basicSkill.png', confidence = conf, grayscale = True)
        varGuts = pyautogui.locateOnScreen('guts.png', confidence = conf, grayscale = True)
            
        if varBasicSkill != None:
            pressButton('Circle', 4)
            break
        if varGuts != None:
            pressButton('Circle', 4)
            break
        time.sleep(0.5)
        pressButton('Down', 1)

    #seleciona wait e passa a vez
    while keyboard.is_pressed('x') == False:
        varWait = pyautogui.locateOnScreen('status.png', confidence = conf, grayscale = True)
            
        if varWait != None:
            pressButton('Down', 2)
            pressButton('Circle', 3)
            break
        time.sleep(0.05)

        
#Main()         
while keyboard.is_pressed('x') == False:
    selectAct()
    accumulate()






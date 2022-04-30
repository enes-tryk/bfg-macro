import keyboard
import pyautogui
import time
from art import *

print('\ngithub.com/enes-tryk/')
print(text2art('BFG-MACRO'))

res = int(input('\nSELECT YOUR SCREEN RESOLUTION:\n[1] 1920:1080\n[2] 1280:768\n> '))
pos = int(input('\nSELECT YOUR FARMING POSITION:\n[1] RIGHT TO LEFT\n[2] LEFT TO RIGHT\n> '))
aim = int(input('\nSELECT THE RANGE TO FARM IN:\n[1] SINGLE BLOCK\n[2] TWO BLOCKS\n> '))
hit = int(input('\nENTER THE HIT POINTS OF THE ITEM YOU ARE FARMING:\n> '))

print('\nSTARTING IN 5 SECONDS...\n[HOLD ALT+A TO STOP]\n'), time.sleep(5)
state = True

while state:
    while not keyboard.is_pressed('alt+a'):

        if pos == 1 and aim == 1 and res == 1:
            pyautogui.click(x=1080, y=1020)
            pyautogui.click(x=650, y=500)
            pyautogui.click(x=840, y=1020)
            pyautogui.click(x=650, y=500, clicks=hit, interval=0.25)

        elif pos == 1 and aim == 2 and res == 1:
            pyautogui.click(x=1080, y=1020)
            pyautogui.click(x=650, y=500)
            pyautogui.click(x=350, y=500)
            pyautogui.click(x=840, y=1020)
            pyautogui.click(x=650, y=500, clicks=hit, interval=0.25)
            pyautogui.click(x=350, y=500, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 1 and res == 1:
            pyautogui.click(x=1080, y=1020)
            pyautogui.click(x=1250, y=500)
            pyautogui.click(x=840, y=1020)
            pyautogui.click(x=1250, y=500, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 2 and res == 1:
            pyautogui.click(x=1080, y=1020)
            pyautogui.click(x=1250, y=500)
            pyautogui.click(x=1550, y=500)
            pyautogui.click(x=840, y=1020)
            pyautogui.click(x=1250, y=500, clicks=hit, interval=0.25)
            pyautogui.click(x=1550, y=500, clicks=hit, interval=0.25)

        elif pos == 1 and aim == 1 and res == 2:
            pyautogui.click(x=800, y=700)
            pyautogui.click(x=275, y=333)
            pyautogui.click(x=500, y=700)
            pyautogui.click(x=275, y=333, clicks=hit, interval=0.25)

        elif pos == 1 and aim == 2 and res == 2:
            pyautogui.click(x=800, y=700)
            pyautogui.click(x=275, y=333)
            pyautogui.click(x=150, y=333)
            pyautogui.click(x=500, y=700)
            pyautogui.click(x=275, y=333, clicks=hit, interval=0.25)
            pyautogui.click(x=150, y=333, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 1 and res == 2:
            pyautogui.click(x=800, y=700)
            pyautogui.click(x=950, y=333)
            pyautogui.click(x=500, y=700)
            pyautogui.click(x=950, y=333, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 2 and res == 2:
            pyautogui.click(x=800, y=700)
            pyautogui.click(x=950, y=333)
            pyautogui.click(x=1125, y=333)
            pyautogui.click(x=500, y=700)
            pyautogui.click(x=950, y=333, clicks=hit, interval=0.25)
            pyautogui.click(x=1125, y=333, clicks=hit, interval=0.25)

        else:
            break

    else:
        restart = int(input('\nSTOPPED THE PROGRAM. CONTINUE WITH THE SAME SETTINGS?\n[1] CONTINUE\n[2] CHANGE '
                            'SETTINGS\n[3] EXIT PROGRAM\n> '))
        state = False

        if restart == 1:
            print('\nSTARTING IN 5 SECONDS...\n[HOLD ALT+A TO STOP]'), time.sleep(5)
            state = True

        elif restart == 2:
            pos = int(input('\nSELECT YOUR FARMING POSITION:\n[1] RIGHT TO LEFT\n[2] LEFT TO RIGHT\n> '))
            aim = int(input('\nSELECT THE RANGE TO FARM IN:\n[1] SINGLE BLOCK\n[2] TWO BLOCKS\n> '))
            hit = int(input('\nENTER THE HIT POINTS OF THE ITEM YOU ARE FARMING:\n> '))

            print('\nSTARTING IN 5 SECONDS...\n[HOLD ALT+A TO STOP]'), time.sleep(5)
            state = True

        else:
            break

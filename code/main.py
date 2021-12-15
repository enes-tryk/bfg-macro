import keyboard, pyautogui, time
from art import *

print('\ngithub.com/enes-tryk/')
print(text2art('BFG-MACRO'))

res = int(input('\nSELECT YOUR SCREEN RESOLUTION:\n[1] 1920:1080\n[2] 1280:768\n> '))
pos = int(input('\nSELECT YOUR FARMING POSITION:\n[1] RIGHT TO LEFT\n[2] LEFT TO RIGHT\n> '))
aim = int(input('\nSELECT THE RANGE TO FARM IN:\n[1] SINGLE BLOCK\n[2] TWO BLOCKS\n> '))
hit = int(input('\nENTER THE HIT POINTS OF THE ITEM YOU ARE FARMING:\n> '))

print('\nSTARTING SCRIPT IN 5 SECONDS...\n[HOLD ALT+A TO ABORT PROGRAM]\n'), time.sleep(5)
state = True

while state:
    while not keyboard.is_pressed('alt+a'):

        if pos == 1 and aim == 1 and res == 1:
            pyautogui.click(x=920, y=1020)
            pyautogui.click(x=660, y=500)
            pyautogui.click(x=820, y=1020)
            pyautogui.click(x=660, y=500, clicks=hit, interval=0.25)

        elif pos == 1 and aim == 2 and res == 1:
            pyautogui.click(x=920, y=1020)
            pyautogui.click(x=660, y=500)
            pyautogui.click(x=360, y=500)
            pyautogui.click(x=820, y=1020)
            pyautogui.click(x=660, y=500, clicks=hit, interval=0.25)
            pyautogui.click(x=360, y=500, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 1 and res == 1:
            pyautogui.click(x=920, y=1020)
            pyautogui.click(x=1200, y=500)
            pyautogui.click(x=820, y=1020)
            pyautogui.click(x=1200, y=500, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 2 and res == 1:
            pyautogui.click(x=920, y=1020)
            pyautogui.click(x=1200, y=500)
            pyautogui.click(x=1500, y=500)
            pyautogui.click(x=820, y=1020)
            pyautogui.click(x=1200, y=500, clicks=hit, interval=0.25)
            pyautogui.click(x=1500, y=500, clicks=hit, interval=0.25)

        elif pos == 1 and aim == 1 and res == 2:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=400, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=400, y=330, clicks=hit, interval=0.25)

        elif pos == 1 and aim == 2 and res == 2:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=400, y=330)
            pyautogui.click(x=120, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=400, y=330, clicks=hit, interval=0.25)
            pyautogui.click(x=120, y=330, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 1 and res == 2:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=950, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=950, y=330, clicks=hit, interval=0.25)

        elif pos == 2 and aim == 2 and res == 2:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=950, y=330)
            pyautogui.click(x=1250, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=950, y=330, clicks=hit, interval=0.25)
            pyautogui.click(x=1250, y=330, clicks=hit, interval=0.25)

        else:
            break

    else:
        restart, state = input('\nSCRIPT HALTED. DO YOU WANT TO CONTINUE? [Y/N]\n> '), False

        if restart.lower() == "y":
            res = int(input('\nSELECT YOUR SCREEN RESOLUTION:\n[1] 1920:1080\n[2] 1280:768\n> '))
            pos = int(input('\nSELECT YOUR FARMING POSITION:\n[1] RIGHT TO LEFT\n[2] LEFT TO RIGHT\n> '))
            aim = int(input('\nSELECT THE RANGE TO FARM IN:\n[1] SINGLE BLOCK\n[2] TWO BLOCKS\n> '))
            hit = int(input('\nENTER THE HIT POINTS OF THE ITEM YOU ARE FARMING:\n> '))

            print('\nSTARTING SCRIPT IN 5 SECONDS...\n[HOLD ALT+A TO ABORT PROGRAM]'), time.sleep(5)
            state = True

        else:
            break

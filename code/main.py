import keyboard, pyautogui, time
from art import *

print(text2art('BFG-MACRO'))
pos = int(input('SELECT YOUR FARMING POSITION:\n[1] RIGHT TO LEFT\n[2] LEFT TO RIGHT\n> '))
block = int(input('\nSELECT THE RANGE TO FARM IN:\n[1] SINGLE BLOCK\n[2] TWO BLOCKS\n> '))
hit = int(input('\nENTER THE HIT POINTS OF THE ITEM YOU ARE FARMING:\n> '))
print('\nSTARTING SCRIPT IN 5 SECONDS...\n[HOLD ALT+A TO ABORT PROGRAM]'), time.sleep(5)

state = True

while state:
    while not keyboard.is_pressed('alt+a'):

        if pos == 1 and block == 1:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=400, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=400, y=330, clicks=hit, interval=0.25)

        elif pos == 1 and block == 2:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=400, y=330)
            pyautogui.click(x=120, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=400, y=330, clicks=hit, interval=0.25)
            pyautogui.click(x=120, y=330, clicks=hit, interval=0.25)

        elif pos == 2 and block == 1:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=950, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=950, y=330, clicks=hit, interval=0.25)

        elif pos == 2 and block == 2:
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=950, y=330)
            pyautogui.click(x=1250, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=950, y=330, clicks=hit, interval=0.25)
            pyautogui.click(x=1250, y=330, clicks=hit, interval=0.25)

        else:
            break

    else:
        state = False
        restart = input('\nSCRIPT HALTED. DO YOU WANT TO CONTINUE? [Y/N]\n> ')

        if restart.lower() == "y":
            pos = int(input('SELECT YOUR FARMING POSITION:\n[1] RIGHT TO LEFT\n[2] LEFT TO RIGHT\n> '))
            block = int(input('\nSELECT THE RANGE TO FARM IN:\n[1] SINGLE BLOCK\n[2] TWO BLOCKS\n> '))
            hit = int(input('\nENTER THE HIT POINTS OF THE ITEM YOU ARE FARMING:\n> '))
            print('\nSTARTING SCRIPT IN 5 SECONDS...\n[HOLD ALT+A TO ABORT PROGRAM]'), time.sleep(5)

            state = True

        else:
            break

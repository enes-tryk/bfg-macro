import keyboard
import pyautogui
import time

hit = int(input('\nENTER HIT POINTS:\n> '))
print('\nSTARTING SCRIPT IN 5 SECONDS.\n[HOLD ALT+A TO ABORT]')
time.sleep(5)

state = True
while state:

    while not keyboard.is_pressed('alt+a'):

        # Select the deployable
        pyautogui.click(x=592, y=709)

        # Place the deployable
        pyautogui.click(x=405, y=340)
        pyautogui.click(x=105, y=340)

        # Select the fist
        pyautogui.click(x=492, y=709)

        # Destroy the deployable
        pyautogui.click(x=405, y=340, clicks=hit, interval=0.21)
        pyautogui.click(x=105, y=340, clicks=hit, interval=0.21)

    else:
        state = False
        CONT = input('\nSCRIPT HALTED. DO YOU WANT TO CONTINUE? [Y/N]\n> ')

        if CONT.lower() == "y":
            hit = int(input('\nENTER HIT POINTS:\n> '))
            print('\nSTARTING SCRIPT IN 5 SECONDS.\n[HOLD ALT+A TO ABORT]')
            time.sleep(5)

            state = True
        else:
            break

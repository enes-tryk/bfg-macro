import keyboard, pyautogui, time

hit = int(input('\nENTER HIT POINTS:\n> '))
pos = input('\nSELECT YOUR POSITION: [L/R]\n> ')
print('\nSTARTING SCRIPT IN 5 SECONDS.\n[HOLD ALT+A TO ABORT]')
time.sleep(5)
state = True

while state:
    while not keyboard.is_pressed('alt+a'):

        if pos.lower() == 'l':
            pyautogui.click(x=630, y=700)
            pyautogui.click(x=400, y=330)
            pyautogui.click(x=120, y=330)
            pyautogui.click(x=530, y=700)
            pyautogui.click(x=400, y=330, clicks=hit, interval=0.25)
            pyautogui.click(x=120, y=330, clicks=hit, interval=0.25)
        
        elif pos.lower() == 'r':
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
            hit = int(input('\nENTER HIT POINTS:\n> '))
            pos = input('\nSELECT YOUR POSITION: [L/R]\n> ')
            print('\nSTARTING SCRIPT IN 5 SECONDS.\n[HOLD ALT+A TO ABORT]')
            time.sleep(5)
            state = True
        
        else:
            break
            

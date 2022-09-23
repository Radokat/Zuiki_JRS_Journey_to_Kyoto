import pyautogui  # install via pip install pyautogui
import pygame  # install via pip install pygame

pygame.init()

clock = pygame.time.Clock()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick_list = []
joyid = "joyid"
joyname = "joyname"

for i in range(pygame.joystick.get_count()):
    jid = {joyid: i, joyname: pygame.joystick.Joystick(i).get_name()}
    joystick_list.append(jid)
mascon_select = next((i for i, item in enumerate(joystick_list) if item["joyname"] == "Nintendo Switch Pro Controller"), None)
# for i in range(pygame.joystick.get_count()): print(i, pygame.joystick.Joystick(i).get_name())
if mascon_select is None:
    print("No Nintendo Switch Pro Controller found. Connect the correct controller and restart the script")
    exit()
mascon_counter = 99
pygame.event.clear()
print('#########################################################')
print('Start the game and use the EB notch to sync controller.')
print('Press CTRL + C to end the script.')
print('#########################################################')   
try:
    while 1:
        pygame.event.pump()
        for event in pygame.event.get():
            mascon_axis = (joysticks[mascon_select].get_axis(1))
            mascon_axis = (round(mascon_axis, 2))
            # Disabled P5 and original P4 behaviour, as it's not needed.
            # if mascon_axis == 1.0:
            #    print("P5")
            #    pyautogui.keyDown('z')
            #    pyautogui.keyUp('z')
            #    mascon_counter = 0
            # if mascon_axis == 0.8:
            #    print("P4")
            #    if mascon_counter == 2:
            #        pyautogui.keyDown('x')  # Increase
            #        pyautogui.keyUp('x')
            #        mascon_counter = 1
            #    if mascon_counter == 0:
            #        pyautogui.keyDown('d')  # Decrease
            #        pyautogui.keyUp('d')
            #        mascon_counter = 1
            if mascon_axis == 0.8:
                print("P4")
                pyautogui.keyDown('z')
                pyautogui.keyUp('z')
                mascon_counter = 1
            if mascon_axis == 0.62:
                print("P3")
                if mascon_counter == 3:
                    pyautogui.keyDown('x')  # Increase
                    pyautogui.keyUp('x')
                    mascon_counter = 2
                if mascon_counter == 1:
                    pyautogui.keyDown('d')  # Decrease
                    pyautogui.keyUp('d')
                    mascon_counter = 2
            if mascon_axis == 0.44:
                print("P2")
                if mascon_counter == 4:
                    pyautogui.keyDown('x')  # Increase
                    pyautogui.keyUp('x')
                    mascon_counter = 3
                if mascon_counter == 2:
                    pyautogui.keyDown('d')  # Decrease
                    pyautogui.keyUp('d')
                    mascon_counter = 3
            if mascon_axis == 0.25:
                print("P1")
                if mascon_counter == 5:
                    pyautogui.keyDown('x')  # Increase
                    pyautogui.keyUp('x')
                    mascon_counter = 4
                if mascon_counter == 3:
                    pyautogui.keyDown('d')  # Decrease
                    pyautogui.keyUp('d')
                    mascon_counter = 4
            if mascon_axis == 0.0:
                print("N")
                pyautogui.keyDown('s')
                pyautogui.keyUp('s')
                pyautogui.keyDown('h')
                pyautogui.keyUp('h')
                mascon_counter = 5
            if mascon_axis == -0.21:
                print("B1")
                print(mascon_axis)
                if mascon_counter == 5:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 6
                if mascon_counter == 7:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 6
            if mascon_axis == -0.32:
                print("B2")
                print(mascon_axis)
                if mascon_counter == 6:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 7
                if mascon_counter == 8:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 7
            if mascon_axis == -0.43:
                print("B3")
                print(mascon_axis)
                if mascon_counter == 7:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 8
                if mascon_counter == 9:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 8
            if mascon_axis == -0.53:
                print("B4")
                print(mascon_axis)
                if mascon_counter == 8:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 9
                if mascon_counter == 10:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 9
            if mascon_axis == -0.64:
                print("B5")
                print(mascon_axis)
                if mascon_counter == 9:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 10
                if mascon_counter == 11:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 10
            if mascon_axis == -0.75:
                print("B6")
                print(mascon_axis)
                if mascon_counter == 10:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 11
                if mascon_counter == 12:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 11
            if mascon_axis == -0.85:
                print("B7")
                print(mascon_axis)
                if mascon_counter == 11:
                    pyautogui.keyDown('k')  # Increase
                    pyautogui.keyUp('k')
                    mascon_counter = 12
                if mascon_counter >= 13:
                    pyautogui.keyDown('j')  # Decrease
                    pyautogui.keyUp('j')
                    mascon_counter = 12
            # if mascon_axis == -0.96:
            #    print("B8")
            #    print(mascon_axis)
            #    if mascon_counter == 12:
            #        # pyautogui.keyDown('k')  # Increase
            #        # pyautogui.keyUp('k')
            #        mascon_counter = 13
            #    if mascon_counter == 14:
            #        # pyautogui.keyDown('j')  # Decrease
            #        # pyautogui.keyUp('j')
            #        mascon_counter = 13
            if mascon_axis == -1.00:
                print("EB")
                print(mascon_axis)
                pyautogui.keyDown('l')
                pyautogui.keyUp('l')
                pyautogui.keyDown('l')
                pyautogui.keyUp('l')
                mascon_counter = 14
        clock.tick(60)
except KeyboardInterrupt:
    pass

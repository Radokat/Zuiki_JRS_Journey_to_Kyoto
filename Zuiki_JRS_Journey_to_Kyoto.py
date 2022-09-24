import pyautogui  # install via pip install pyautogui
import pygame  # install via pip install pygame
import threading
import queue

pyautogui.PAUSE = 0.0571  # Lowest possible delay before the game starts dropping key presses.
pygame.init()

clock = pygame.time.Clock()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick_list = []
joyid = "joyid"
joyname = "joyname"

q1 = queue.Queue()


# Define functions


def brake_inc():
    pyautogui.keyDown('k')  # Increase brake
    pyautogui.keyUp('k')


def brake_dec():
    pyautogui.keyDown('j')  # Decrease brake
    pyautogui.keyUp('j')


def brake_eb():
    pyautogui.keyDown('l')  # Set brake to EB
    pyautogui.keyUp('l')


def neutral():
    pyautogui.keyDown('s')  # Set master controller to off
    pyautogui.keyUp('s')
    pyautogui.keyDown('h')  # Release brakes
    pyautogui.keyUp('h')


def power_inc():
    pyautogui.keyDown('x')  # Increase power
    pyautogui.keyUp('x')


def power_dec():
    pyautogui.keyDown('d')  # Decrease power
    pyautogui.keyUp('d')


def power_max():
    pyautogui.keyDown('z')  # Set power to max
    pyautogui.keyUp('z')


for i in range(pygame.joystick.get_count()):
    jid = {joyid: i, joyname: pygame.joystick.Joystick(i).get_name()}
    joystick_list.append(jid)
mascon_select = next((i for i, item in enumerate(joystick_list) if item["joyname"] == "Nintendo Switch Pro Controller"),
                     None)

if mascon_select is None:
    print("No Nintendo Switch Pro Controller found. Connect the correct controller and restart the script")
    exit()

mascon_counter = 99
pygame.event.clear()  # Clear events to remove wrong inputs.

print('#########################################################')
print('Start the game and use the EB notch to sync controller.')
print('Press CTRL + C to end the script.')
print('#########################################################')

# Queue worker


def worker():
    while True:
        item = q1.get()
        item()
        q1.task_done()


try:
    threading.Thread(target=worker, daemon=True).start()

    while 1:
        for event in pygame.event.get():
            mascon_axis = (joysticks[mascon_select].get_axis(1))
            mascon_axis = (round(mascon_axis, 2))
            # Disabled P5 and original P4 behaviour, as it's not needed.
            # if mascon_axis == 1.0:
            #      # print("P5")
            #    pyautogui.keyDown('z')
            #    pyautogui.keyUp('z')
            #    mascon_counter = 0
            # if mascon_axis == 0.8:
            #      # print("P4")
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
                q1.put(power_max)
                mascon_counter = 1
            if mascon_axis == 0.62:
                print("P3")
                if mascon_counter == 3:
                    q1.put(power_inc)
                    mascon_counter = 2
                if mascon_counter == 1:
                    q1.put(power_dec)
                    mascon_counter = 2
            if mascon_axis == 0.44:
                print("P2")
                if mascon_counter == 4:
                    q1.put(power_inc)
                    mascon_counter = 3
                if mascon_counter == 2:
                    q1.put(power_dec)
                    mascon_counter = 3
            if mascon_axis == 0.25:
                print("P1")
                if mascon_counter == 5:
                    q1.put(power_inc)
                    mascon_counter = 4
                if mascon_counter == 3:
                    q1.put(power_dec)
                    mascon_counter = 4
            if mascon_axis == 0.0:
                print("N")
                q1.put(neutral)
                mascon_counter = 5
            if mascon_axis == -0.21:
                print("B1")
                if mascon_counter == 5:
                    q1.put(brake_inc)
                    mascon_counter = 6
                if mascon_counter == 7:
                    q1.put(brake_dec)
                    mascon_counter = 6
            if mascon_axis == -0.32:
                print("B2")
                if mascon_counter == 6:
                    q1.put(brake_inc)
                    mascon_counter = 7
                if mascon_counter == 8:
                    q1.put(brake_dec)
                    mascon_counter = 7
            if mascon_axis == -0.43:
                print("B3")
                if mascon_counter == 7:
                    q1.put(brake_inc)
                    mascon_counter = 8
                if mascon_counter == 9:
                    q1.put(brake_dec)
                    mascon_counter = 8
            if mascon_axis == -0.53:
                print("B4")
                if mascon_counter == 8:
                    q1.put(brake_inc)
                    mascon_counter = 9
                if mascon_counter == 10:
                    q1.put(brake_dec)
                    mascon_counter = 9
            if mascon_axis == -0.64:
                print("B5")
                if mascon_counter == 9:
                    q1.put(brake_inc)
                    mascon_counter = 10
                if mascon_counter == 11:
                    q1.put(brake_dec)
                    mascon_counter = 10
            if mascon_axis == -0.75:
                print("B6")
                if mascon_counter == 10:
                    q1.put(brake_inc)
                    mascon_counter = 11
                if mascon_counter == 12:
                    q1.put(brake_dec)
                    mascon_counter = 11
            if mascon_axis == -0.85:
                print("B7")
                if mascon_counter == 11:
                    q1.put(brake_inc)
                    mascon_counter = 12
                if mascon_counter >= 13:
                    q1.put(brake_dec)
                    mascon_counter = 12
            # if mascon_axis == -0.96:
            #      # print("B8")
            #      #
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
                q1.put(brake_eb)
                mascon_counter = 14
        pygame.time.Clock().tick_busy_loop(60)
except KeyboardInterrupt:
    pass


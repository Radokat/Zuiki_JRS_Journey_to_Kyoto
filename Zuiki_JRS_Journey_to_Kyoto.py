import pyautogui  # install via pip install pyautogui
import pygame  # install via pip install pygame
import threading
import queue
import os

pyautogui.PAUSE = 0.0571  # Lowest possible delay before the game starts dropping key presses.
pygame.init()
clock = pygame.time.Clock()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick_list = []
joyid = "joyid"
joyname = "joyname"

qMascon = queue.Queue()
qButton = queue.Queue()
notchfix = False

# Define functions

def menu():
    clearscreen()
    print('#####################################################################################')
    print('# Start the game and use the EB notch to sync controller once you are in the train.')
    print('# Press CTRL + C to end the script.')
    print(f'# Notchfix enabled: {notchfix}')

def clearscreen():
    os.system('clear')


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


def button_a():
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


def button_b():
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')


def button_y():
    pyautogui.keyDown('z')
    pyautogui.keyUp('z')


def button_l():
    pyautogui.keyDown('l')
    pyautogui.keyUp('l')


def button_r():
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')


def button_dpad_left():
    pyautogui.keyDown('left')
    pyautogui.keyUp('right')


def button_dpad_right():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')


def button_dpad_up():
    pyautogui.keyDown('up')
    pyautogui.keyUp('up')


def button_dpad_down():
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')


def button_pause():
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')


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
clearscreen()
print('Please enter the number of the line you want to drive and confirm with enter:')
print('1:   Kurama Line')
print('2:   Eizan Line')

rtselect = input()
if rtselect == '2':
    notchfix = True
clearscreen()
menu()

# Queue worker functions


def wmascon():
    while True:
        item1 = qMascon.get()
        item1()
        qMascon.task_done()


def wbutton():
    while True:
        item2 = qButton.get()
        item2()
        qButton.task_done()


try:
    threading.Thread(target=wmascon, daemon=True).start()
    threading.Thread(target=wbutton, daemon=True).start()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Lever section
                mascon_axis = (joysticks[mascon_select].get_axis(1))
                mascon_axis = (round(mascon_axis, 2))
                if mascon_axis == 0.8:
                    #print("P4")
                    qMascon.put(power_max)
                    mascon_counter = 1
                if mascon_axis == 0.62:
                    if mascon_counter == 3:
                        qMascon.put(power_inc)
                        mascon_counter = 2
                    if mascon_counter == 1:
                        qMascon.put(power_dec)
                        mascon_counter = 2
                if mascon_axis == 0.44:
                    if mascon_counter == 4:
                        qMascon.put(power_inc)
                        mascon_counter = 3
                    if mascon_counter == 2:
                        qMascon.put(power_dec)
                        mascon_counter = 3
                if mascon_axis == 0.25:
                    if mascon_counter == 5:
                        qMascon.put(power_inc)
                        mascon_counter = 4
                    if mascon_counter == 3:
                        qMascon.put(power_dec)
                        mascon_counter = 4
                if mascon_axis == 0.0:
                    qMascon.put(neutral)
                    mascon_counter = 5
                if mascon_axis == -0.21:
                    if mascon_counter == 5:
                        qMascon.put(brake_inc)
                        mascon_counter = 6
                    if mascon_counter == 7:
                        qMascon.put(brake_dec)
                        if notchfix:
                            qMascon.put(brake_dec)
                        mascon_counter = 6
                if mascon_axis == -0.32:
                    if mascon_counter == 6:
                        qMascon.put(brake_inc)
                        if notchfix:
                            qMascon.put(brake_inc)
                        mascon_counter = 7
                    if mascon_counter == 8:
                        qMascon.put(brake_dec)
                        mascon_counter = 7
                if mascon_axis == -0.43:
                    if mascon_counter == 7:
                        qMascon.put(brake_inc)
                        mascon_counter = 8
                    if mascon_counter == 9:
                        qMascon.put(brake_dec)
                        if notchfix:
                            qMascon.put(brake_dec)
                        mascon_counter = 8
                if mascon_axis == -0.53:
                    if mascon_counter == 8:
                        qMascon.put(brake_inc)
                        if notchfix:
                            qMascon.put(brake_inc)
                        mascon_counter = 9
                    if mascon_counter == 10:
                        qMascon.put(brake_dec)
                        mascon_counter = 9
                if mascon_axis == -0.64:
                    if mascon_counter == 9:
                        qMascon.put(brake_inc)
                        mascon_counter = 10
                    if mascon_counter == 11:
                        qMascon.put(brake_dec)
                        mascon_counter = 10
                if mascon_axis == -0.75:
                    if mascon_counter == 10:
                        qMascon.put(brake_inc)
                        if notchfix:
                            qMascon.put(brake_inc)
                        mascon_counter = 11
                    if mascon_counter == 12:
                        qMascon.put(brake_dec)
                        mascon_counter = 11
                if mascon_axis == -0.85:
                    if mascon_counter == 11:
                        qMascon.put(brake_inc)
                        mascon_counter = 12
                    if mascon_counter >= 13:
                        qMascon.put(brake_dec)
                        mascon_counter = 12
                if mascon_axis == -1.00:
                    qMascon.put(brake_eb)
                    mascon_counter = 14

            # Button section
            if event.type == pygame.JOYBUTTONUP and event.button == 0:
                qButton.put(button_a)
            if event.type == pygame.JOYBUTTONUP and event.button == 1:
                qButton.put(button_b)
            if event.type == pygame.JOYBUTTONUP and event.button == 3:
                qButton.put(button_y)
            if event.type == pygame.JOYBUTTONUP and event.button == 5:
                qButton.put(button_pause)
            if event.type == pygame.JOYBUTTONUP and event.button == 9:
                qButton.put(button_l)
            if event.type == pygame.JOYBUTTONUP and event.button == 10:
                qButton.put(button_r)
            if event.type == pygame.JOYBUTTONUP and event.button == 11:
                qButton.put(button_dpad_up)
            if event.type == pygame.JOYBUTTONUP and event.button == 12:
                qButton.put(button_dpad_down)
            if event.type == pygame.JOYBUTTONUP and event.button == 13:
                qButton.put(button_dpad_left)
            if event.type == pygame.JOYBUTTONUP and event.button == 14:
                qButton.put(button_dpad_right)

        clock.tick_busy_loop(60)
except KeyboardInterrupt:
    pass

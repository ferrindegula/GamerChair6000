import pydirectinput as pdi
import pyautogui
from pynput import keyboard
import time

zoomedIn = True
pyautogui.PAUSE = 0


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    



def on_release(key):

    print('{0} released'.format(
        key))
    if key == keyboard.Key.alt_l:
        global zoomedIn
        if zoomedIn == True:
            zoomedIn = False
            return(False)
        else:
            zoomedIn = True
            return(False)
    # if key == keyboard.Key.x07:
    #     return(False)
            

    



# Collect events until released
while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    print(zoomedIn)

    if zoomedIn == False:
        time.sleep(.1)
        pyautogui.moveTo(960, 540)
        pyautogui.hotkey('win','+')
        print("zoom in")
        time.sleep(.1)
    if zoomedIn == True:
        time.sleep(.1)
        pyautogui.hotkey('win','-')
        print("zoom out")
        time.sleep(.1)
#960 540
# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

while True:
    # zoomedIn = listener.start()
    print("dab")
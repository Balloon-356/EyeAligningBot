# Done by Balloon_356
# Bilibili: https://space.bilibili.com/244384103

import pydirectinput as pd
import time



def mc_pause():
    pd.keyDown('f3')
    pd.keyDown('esc')
    pd.keyUp('esc')
    pd.keyUp('f3')

def mc_mouse_move(dx, dy, paused=False):  
    if paused:
        pd.keyDown('esc')
        pd.keyUp('esc')
    pd.moveRel(0, 1)  # to activate the cursor
    pd.moveRel(dy, dx)
    if paused:
        mc_pause()

def EyeAlign(startX, startY, destX, destY):
    time.sleep(0.1)
    dx = destX - startX
    dy = destY - startY
    print(dx, dy)
    if dy == 0 and abs(dx)<=10:
        return True
    elif abs(dy) <= 10:
        mc_mouse_move(3*dx, 3*dy, paused=True)
    elif abs(dy) <= 3:
        mc_mouse_move(3*dx, 2*dy, paused=True)
    else:
        mc_mouse_move(4*dx, 4*dy, paused=True)
    time.sleep(0.1)
    return False



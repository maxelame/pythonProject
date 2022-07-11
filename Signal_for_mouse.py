import pyautogui as pag
import traceback
import time

def click_up():
    print(pag.size())
    pag.moveTo(1233, 188, 0.2)
    pag.click()  # щелчок мыши
    time.sleep(4)
    pag.moveTo(1313, 163, 0.2)
    pag.click()  # щелчок мыши
def click_down():
    print(pag.size())
    pag.moveTo(1220, 270, 0.2)
    pag.click()  # щелчок мыши
    time.sleep(4)
    pag.moveTo(1313, 163, 0.2)
    pag.click()  # щелчок мыши


while True:
    try:
        time.sleep(0.5)
        with open('click_direction.txt') as fd:
            direction = fd.read()
            if direction == "up":
                click_up()
            elif direction == "down":
                click_down()
    except Exception:
        print(traceback.format_exc())

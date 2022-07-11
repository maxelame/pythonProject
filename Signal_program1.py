import time
import traceback
import winsound
import matplotlib.pyplot as plt
import pyautogui as pag
import matplotlib.animation as animation

#######################
def sound_up():
    frequency = 1400  # Set Frequency To 2500 Hertz
    duration = 80  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def sound_down():
    frequency = 1000  # Set Frequency To 2500 Hertz
    duration = 80  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def click_up():
    print(pag.size())
    pag.moveTo(1233, 188, 0.5)
    pag.click()  # щелчок мыши
    pag.moveTo(1313, 163, 5)
    pag.click()  # щелчок мыши


def click_down():
    print(pag.size())
    pag.moveTo(1220, 270, 0.5)
    pag.click()  # щелчок мыши
    pag.moveTo(1313, 163, 5)
    pag.click()  # щелчок мыши

line_1 = 0
while True:
    # ani = animation.FuncAnimation(fig, animate, interval=100)
    # plt.show()
    try:
        time.sleep(0.01)
        with open('Ticks_1\R_50.dat') as fd:
                lines = fd.read().split("&")
                digit = int(str(int(float(lines[4])*100000))[-2])
                if line_1 != lines[4]:
                    print(lines[0], lines[4], digit, sep= '---')
                    line_1 = lines[4]
                    if digit % 2 == 0:
                        direction = 1
                        sound_up()
                    else:
                        direction = -1
                        sound_down()

    except Exception:
        print(traceback.format_exc())

print(li)
print(string1)
print("".join(str(li)))
new_ticks_file = open("new_ticks.txt", "w")
new_ticks_file.write(string1)
new_ticks_file.close()

import pyautogui as pag

print(pag.size())
pag.moveTo(1800, 219, 2)
pag.click()    #  щелчок мыши
pag.moveTo(1869, 190, 5)
pag.click()    #  щелчок мыши
pag.moveTo(1521, 277, 2)
pag.click()    #  щелчок мыши
pag.typewrite("2")
#pag.click(x=100, y=200)  # перемещение на 100, 200, а затем нажатие левой кнопкой

#pag.click(button='right')  # щелчок правой кнопкой мыши

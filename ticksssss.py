import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#with open('Ticks_1\R_100.dat') as fd:
#    lines = fd.read()
#print(lines)
previous_ticks = None
s = 0
r = 0
li = []
while r < 100:
    time.sleep(1 - time.monotonic() % 1)
    with open('Ticks_1\R_100.dat') as fd:
        lines = fd.read().split(".")
        if int(lines[3]) < 10: # если окончание тика представлено одним числом, то это десятки и добавляем к ним ноль
            new_tick = int(lines[3]) * 10
        else:
            new_tick = int(lines[3])  # если окончание тика представлено двумя числами, то это десятки и добавляем к ним ноль
        if new_tick != previous_ticks:
            # остаток от деления %
            if int(new_tick) % 2 == 0:
                a = 1
            else:
                a = -1
            s += a
            r += 1
            previous_ticks = int(new_tick)
            li.append(s)
            print(li)



print(li)

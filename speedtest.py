import time

previous_ticks = None
previous_ticks2 = None
s = 0
r = 0
li = ""
a = None
while r < 1000:
    time.sleep(0.1)
    with open('Ticks_1\R_100.dat') as fd:
        lines = fd.read().split("&")
    with open('Ticks_2\R_100.dat') as fd:
        lines2 = fd.read().split("&")
        new_tick = int(float(lines[4])*100)
        digit = str(new_tick)
        new_tick2 = int(float(lines2[4])*100)
        digit2 = str(new_tick2)
#        if int(lines[3]) < 10: # если окончание тика представлено одним числом, то это десятки и добавляем к ним ноль
#            new_tick = int(lines[3]) * 10
#        else:
 #           new_tick = int(lines[3])  # если окончание тика представлено двумя числами, то это десятки и добавляем к ним ноль
        if new_tick != previous_ticks and new_tick2 != previous_ticks2:
            if int(new_tick) % 2 == 0:
                a = 1
            else:
                a = 0
            previous_ticks = new_tick
            previous_ticks2 = new_tick2
            r += 1
            li += str(a)
            print("{2}    {6}  " .format(new_tick, new_tick2, r, digit[5], digit2[5], a, li))




    #        if int(lines[3]) < 10: # если окончание тика представлено одним числом, то это десятки и добавляем к ним ноль
    #            new_tick = int(lines[3]) * 10
    #        else:
     #           new_tick = int(lines[3])  # если окончание тика представлено двумя числами, то это десятки и добавляем к ним ноль

                # остаток от деления %
"""            if int(new_tick) % 2 == 0:
                a = 1
            else:
                a = -1
                s += a

            r += 1
            previous_ticks = int(new_tick)
            li.append(a)

print(li)
"""

# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

import math


def PiWithPrecision(precision):
    count = 0
    while(precision < 1):
        precision *= 10
        count += 1
    piConst = ((math.pi*10**count)-(math.pi*10**count) % 1)/10**count
    return piConst


piConst = PiWithPrecision(0.0001)
print(piConst)

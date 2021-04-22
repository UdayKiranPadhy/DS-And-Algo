import math


def nearest2power(num):
    return pow(2, math.ceil(math.log(num) / math.log(2)))


def nextmultiple(i, X):
    return X if i <= X else nextmultiple(i, X + d)


def GG(L, R, X):
    sensor1 = []
    sensor1times = []
    sensor2 = []
    sensor2times = []
    for i in range(L, R + 1):
        gg1 = nearest2power(i)
        sensor1.append(gg1)
        gg2 = nextmultiple(i, X)
        sensor2.append(gg2)

        if gg1 < gg2:
            sensor1times.append(gg1)
        elif gg2 < gg1:
            sensor2times.append(gg2)
    if len(sensor1times) > len(sensor2times):
        return 1
    if len(sensor1times) < len(sensor2times):
        return 2
    return 0


d = 1
print(GG(4, 10, 1))

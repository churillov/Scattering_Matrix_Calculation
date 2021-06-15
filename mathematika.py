import numpy as np

# функция реализующая окно блэкмана


def blackman_win(data):
    blackman = np.blackman(8192)
    blackman[0] = 0
    blackman = np.float32(blackman / sum(blackman))
    z = data * blackman
    return z

# функция нахождения min, max


def min_max(data):
    x = max(data)
    y = min(data)
    return (x,y)


def col_iterac(maxim, minim, data_1, step):
    z = []
    z = data_1.copy()
    z.sort()
    iterac = maxim - minim 
    step_1 = iterac / step
    x = []
    schetchik = 0
    for i in range(step):
        if len(z) == 0:
            return x
        else:
            for k in range(len(z)):
                if minim == z[k]:
                    schetchik += 1 
            for k in z:
                if (minim + step_1 * i) < k <= (minim + step_1 * (i + 1)):
                    schetchik += 1  
                elif k > (minim + step_1 * (i + 1)):
                    break
        x.append(schetchik)
        del (z[:schetchik])
        schetchik = 0 
    return (x, step_1)


def parog(data, min_max, data_1):
    if data_1 <= data:
        return min_max[1]
    else:
        return min_max[0]


def plot_prav_obnar(data, parog, x):
    minim = min(data)
    maxim = max(data)
    iterac = maxim - minim 
    step = iterac / 100
    data_1 = []
    for k in range(100):
        if (minim + step * k) <= parog <= (minim + step * (k + 1)):
            y = 1
            break
        else:
            y = 0

    if y == 1:
        if parog == x[1]:
            for k in data:
                if k <= parog:
                    data_1.append(k)
            return data_1

        elif parog == x[0]:
            for k in data:
                if k >= parog:
                    data_1.append(k)
            return data_1
    elif y == 0:
        if parog == x[1]:
            if (sum(data)/len(data)) < parog:
                return 1
            else:
                return 0
        elif parog == x[0]:
            if (sum(data)/len(data)) > parog:
                return 1
            else:
                return 0


def srednee(data):
    x = sum(data) / len(data)
    return x


def summ(data):
    x = 0 
    if type(data) == list:
        for i in data:
            x = x + i
        return x
    else:
        x = x + data
        return x

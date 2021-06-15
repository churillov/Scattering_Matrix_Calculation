import struct
import numpy as np

#  функции для чтения заголовка

def uint32_type(uint32_type):  # функция преобразовывет bin и возвращает uint32
    uint32_type_1 = struct.unpack('<I', uint32_type)
    return uint32_type_1[0]


def float_type(float_type):     # функция преобразовывет bin и возвращает float
    float_type = struct.unpack('<f', float_type)
    return float_type[0]


def uint8_type(uint8_type):        # функция преобразовывет bin и возвращает uint8
    i = 0
    while i < len(uint8_type):
        uint8_type_1 = np.uint8(int.from_bytes(uint8_type[i:i+1],  byteorder="little"))
        i = i + 1
    return uint8_type_1


def uint16_type(uint16_type):   # функция преобразовывет bin и возвращает uint16
    i = 0
    while i < len(uint16_type):
        uint16_type_1 = np.uint16(int.from_bytes(uint16_type[i:i+2],  byteorder="little"))
        i = i + 2
    return uint16_type_1

# commit
# функция считает сколько бит занимает коментарий
# и преобразовывает bin  в char big-endian


def commit_char_big(commit_char_big):
    i = 0
    commit_1 = str("")
    while i < len(commit_char_big):
        commit_char_big_1 = np.uint16(int.from_bytes(commit_char_big[i:i+2],  byteorder="big"))
        commit_1 = commit_1 + chr(commit_char_big_1)
        i = i + 2
    return commit_char_big_1, commit_1

#  структура данных
    
#  функция возвращающая начальный и конечный бит в итерации


def structure(number_relis, front_relis_1):
    back_relis = 16384 * number_relis + front_relis_1 + number_relis * 8 
    front_relis = back_relis - 16384 - 8 
    return front_relis, back_relis


#  пример
#  Danye
#  number_relis нужно указать число итерации
#  num_relis = byte [structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] : structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] + 4]
#  angle = byte [structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] + 4 : structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] + 6]
#  xxx = byte [structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] + 6 : structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] + 8]
#  data = byte [structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[0] + 8 : structure (number_relis, 60 + commit_char_big(col_byte_commit)[0])[1]]
 
#  функция преобразует int в short


def preob_short(data):
    z = (np.short(data))
    return z

#  функция преобразует bin в int


def preob_int_bit(data):
    i = 0
    z = []
    while i < 16384:
        z.append(int.from_bytes(data[i:i+2], byteorder='little'))
        i += 2
    return z


#  в radarconsol  не отображаются начальные отсчеты
#  эта функия сопоставляет отсчеты radarconsol и отсчеты в файле
#  в radarconsol не хватает первых 5 отсчетов, поэтому в этой функции к каждому
#  отсчету прибовляется 5


def Countdown_radar_consol(countdown, k=5):
    countdown_1 = []
    for i in countdown:
        countdown_1.append(i + k)
    return countdown_1


def test(data):
    data = struct.unpack('<8192h', data)
    lst = list(data)
    return lst

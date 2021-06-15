import numpy as np
import zagolovok
import mathematika


class Parser:

    def __init__(self, file_name, number_countdown):
        self.file_name = file_name
        # Жестко закодировал +5 потому, что в RadarConsol сдвинуты на 5
        self.number_countdown = int(number_countdown) + 5

    @staticmethod
    def sum_po_countdown(datanum, list_countdown, func):
        for i in range(len(list_countdown)):
            func[i] = func[i] + datanum[i]
        return func

    def comment(self):
        with open(self.file_name, "rb") as f:  # открытие файла
            byte = f.read(60)  # чтение файла
            col_byte_comment = byte[56:60]  # Количество байт в комментарии
        with open(self.file_name, "rb") as f:  # открытие файла
            byte = f.read(60 + zagolovok.commit_char_big(col_byte_comment)[0])  # чтение файла
            comment_1 = byte[60:60 + zagolovok.commit_char_big(col_byte_comment)[0]]
            comment_1 = zagolovok.commit_char_big(comment_1)[1]
        return comment_1

    def number_of_lines(self):
        with open(self.file_name, "rb") as f:  # открытие файла
            byte = f.read(48)  # чтение файла
            num_of_lin = byte[46:48]  # количество реализации (линий)
            num_of_lin = zagolovok.uint16_type(num_of_lin)
        return num_of_lin

    def data(self):
        with open(self.file_name, "rb") as f:  # открытие файла
            byte = f.read()  # чтение файла
            #  структура данных
            #  заголовок
            location = byte[0:12]
            name = byte[12:24]
            polarization = byte[24:36]
            version = byte[36:40]
            # attenuator = byte[44:45]
            num_of_lin = byte[46:48]  # количество реализации (линий)
            # Пустые байты
            # r_angle = byte[40:44]
            signal = byte[45:46]
            # r_average = byte[48:49]
            # type_data = byte[49:50]
            # r_discrete = byte[50:54]
            # r_numpoint = byte[54:56]

            #    commit
            col_byte_comment = byte[56:60]    # Количество байт в комментарии
            comment_1 = byte[60:60 + zagolovok.commit_char_big(col_byte_comment)[0]]
            # Тут хранится комментарий, завист от его длины col_byte_comment

            encoding = 'windows-1251'

            # print(str("Местоположение: ") + location.decode(encoding))
            # print(str("Имя: ") + name.decode(encoding))
            # print(str("Поляризация: ") + polarization.decode(encoding))
            print(str("Версия ") + str(zagolovok.uint32_type(version)))
            print(str("Ослабление ") + str(zagolovok.uint8_type(signal)))
            print(str("Количество линий ") + str(zagolovok.uint16_type(num_of_lin)))
            print(str("Количество байт для коментария ") + str(zagolovok.commit_char_big(col_byte_comment)[0]))
            print(str("Коментарий ") + str(zagolovok.commit_char_big(comment_1)[1]))
            print()

            #  пробегает все линии т.е. все измерения
            #  каждое измерение умножает на окно блэкмана
            i = 1   # i <= счетчик проходящий всё количество реализаций!!!
            z = []
            while i <= zagolovok.uint16_type(num_of_lin):
                data = byte[zagolovok.structure(i, 60 + zagolovok.commit_char_big(col_byte_comment)[0])[0] + 8:
                            zagolovok.structure(i, 60 + zagolovok.commit_char_big(col_byte_comment)[0])[1]]
                n = zagolovok.test(data)
                nn = mathematika.blackman_win(n)
                z.append(nn)
                i = i + 1
                del (data, nn, n)

        z = np.array(z)

        #  преобразование фурье
        fyr = np.fft.fft(z, n=None, axis=-1, norm=None).transpose()
        return fyr[self.number_countdown]

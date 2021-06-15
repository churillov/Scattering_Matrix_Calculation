from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QMessageBox

import numpy as np
import bin_parser
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.file_name = {"path_to_file_1": None, "path_to_file_2": None, "path_to_file_3": None, "path_to_file_4": None,
                          "path_to_file_5": None, "path_to_file_6": None, "path_to_file_7": None, "path_to_file_8": None,
                          "path_to_file_9": None, "path_to_file_10": None, "path_to_file_11": None, "path_to_file_12": None}

        self.gate_range = {"gate_range_1": None, "gate_range_2": None, "gate_range_3": None}
        self.amplitude = {"amplitude_1": None, "amplitude_2": None, "amplitude_3": None, "amplitude_4": None}
        self.phase = {"phase_1": None, "phase_2": None, "phase_3": None, "phase_4": None}

        self.amplitude_1 = None
        self.amplitude_2 = None
        self.phase_1 = None
        self.phase_2 = None

        self.betta = None
        self.gamma = None
        self.alpha = None
        self.phi = None

        self.setWindowTitle("Представление данных эксперементальных измерений")
        self.setGeometry(300, 300, 950, 350)

        self.statusBar()

        # Панель переключения между параметрами
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(10, 10, 930, 300)

        # 1-ая группа параметров "Амплитуда и фаза"
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "Калибровка 1")

        # 2-ая группа параметров "Амплитуда и фаза"
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "Калибровка 2")

        # 3-ая группа параметров "Амплитуда и фаза"
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "Эксперимент")

        # Кнопка выхода из программы
        self.pushButton_1 = QtWidgets.QPushButton("Выход", self)
        self.pushButton_1.setObjectName(u"pushButton_2")
        self.pushButton_1.setGeometry(850, 315, 75, 25)
        self.pushButton_1.clicked.connect(self.exit)

        # Кнопка для рассчета Амплитуды и фазы
        self.pushButton = QtWidgets.QPushButton("Рассчитать", self)
        self.pushButton.setObjectName(u"pushButton_2")
        self.pushButton.setGeometry(290, 270, 75, 25)
        self.pushButton.clicked.connect(self.data)

        # Кнопка 1
        self.toolButton = QtWidgets.QPushButton("Открыть", self.tab)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(280, 50, 59, 19)
        self.toolButton.clicked.connect(self.action_cliked)

        # Кнопка 2
        self.toolButton_2 = QtWidgets.QPushButton("Открыть", self.tab)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(280, 100, 59, 19)
        self.toolButton_2.clicked.connect(self.action_cliked)

        # Кнопка 3
        self.toolButton_3 = QtWidgets.QPushButton("Открыть", self.tab)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(280, 150, 59, 19)
        self.toolButton_3.clicked.connect(self.action_cliked)

        # Кнопка 4
        self.toolButton_4 = QtWidgets.QPushButton("Открыть", self.tab)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(280, 200, 59, 19)
        self.toolButton_4.clicked.connect(self.action_cliked)

        # label Путь к файлу 1
        self.label = QtWidgets.QLabel("Путь к файлу 1", self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(30, 55, 80, 25)
        self.label.setMaximumSize(10000, 30)

        # label Путь к файлу 2
        self.label_2 = QtWidgets.QLabel("Путь к файлу 2", self)
        self.label.setObjectName(u"label")
        self.label_2.setGeometry(30, 105, 80, 25)
        self.label_2.setMaximumSize(10000, 30)

        # label Путь к файлу 3
        self.label_3 = QtWidgets.QLabel("Путь к файлу 3", self)
        self.label.setObjectName(u"label")
        self.label_3.setGeometry(30, 155, 80, 25)
        self.label_3.setMaximumSize(10000, 30)

        # label Путь к файлу 4
        self.label_4 = QtWidgets.QLabel("Путь к файлу 4", self)
        self.label.setObjectName(u"label")
        self.label_4.setGeometry(30, 205, 80, 25)
        self.label_4.setMaximumSize(10000, 30)

        # Задаем строб дальности для раздела калибровки
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(350, 50, 75, 20)
        self.lineEdit.returnPressed.connect(self.get_gate_range)

        # label Амплитуда для 1 файла
        self.label_5 = QtWidgets.QLabel("Амплитуда", self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(500, 60, 70, 30)
        self.label_5.setMaximumSize(100, 30)

        # label Амплитуда для 2 файла
        self.label_6 = QtWidgets.QLabel("Амплитуда", self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(700, 60, 70, 30)
        self.label_6.setMaximumSize(100, 30)

        # label Амплитуда для 3 файла
        self.label_7 = QtWidgets.QLabel("Амплитуда", self)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(500, 110, 70, 30)
        self.label_7.setMaximumSize(100, 30)

        # label Амплитуда для 4 файла
        self.label_8 = QtWidgets.QLabel("Амплитуда", self)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(700, 110, 70, 30)
        self.label_8.setMaximumSize(100, 30)

        # label Фаза для 1 файла
        self.label_9 = QtWidgets.QLabel("Фаза", self)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(600, 60, 70, 30)
        self.label_9.setMaximumSize(100, 30)

        # label Фаза для 2 файла
        self.label_10 = QtWidgets.QLabel("Фаза", self)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(800, 60, 70, 30)
        self.label_10.setMaximumSize(100, 30)

        # label Фаза для 3 файла
        self.label_11 = QtWidgets.QLabel("Фаза", self)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(600, 110, 70, 30)
        self.label_11.setMaximumSize(100, 30)

        # label Фаза для 4 файла
        self.label_12 = QtWidgets.QLabel("Фаза", self)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(800, 110, 70, 30)
        self.label_12.setMaximumSize(100, 30)

        # Вывод Амплитуды 1
        self.lineEdit_5 = QLineEdit(self.tab)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(490, 60, 60, 20)
        self.lineEdit_5.setReadOnly(True)

        # Вывод Амплитуды 2
        self.lineEdit_6 = QLineEdit(self.tab)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(690, 60, 60, 20)
        self.lineEdit_6.setReadOnly(True)

        # Вывод Амплитуды 3
        self.lineEdit_7 = QLineEdit(self.tab)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(490, 110, 60, 20)
        self.lineEdit_7.setReadOnly(True)

        # Вывод Амплитуды 4
        self.lineEdit_8 = QLineEdit(self.tab)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(690, 110, 60, 20)
        self.lineEdit_8.setReadOnly(True)

        # Вывод Фазы 1
        self.lineEdit_9 = QLineEdit(self.tab)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(570, 60, 60, 20)
        self.lineEdit_9.setReadOnly(True)

        # Вывод Фазы 2
        self.lineEdit_10 = QLineEdit(self.tab)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(770, 60, 60, 20)
        self.lineEdit_10.setReadOnly(True)

        # Вывод Фазы 3
        self.lineEdit_11 = QLineEdit(self.tab)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(570, 110, 60, 20)
        self.lineEdit_11.setReadOnly(True)

        # Вывод Фазы 4
        self.lineEdit_12 = QLineEdit(self.tab)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(770, 110, 60, 20)
        self.lineEdit_12.setReadOnly(True)

        self.pushButton_2 = QtWidgets.QPushButton("Сохранить калибровку", self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(680, 150, 150, 25)
        self.pushButton_2.setMaximumSize(150, 30)
        self.pushButton_2.clicked.connect(self.save)

        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(850, 155, 70, 17)
        self.checkBox.setEnabled(False)

        # Раздел № 2 Калибровка 2
        # Кнопка 1
        self.toolButton_5 = QtWidgets.QPushButton("Открыть", self.tab_2)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(280, 50, 59, 19)
        self.toolButton_5.clicked.connect(self.action_cliked)

        # Кнопка 2
        self.toolButton_6 = QtWidgets.QPushButton("Открыть", self.tab_2)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setGeometry(280, 100, 59, 19)
        self.toolButton_6.clicked.connect(self.action_cliked)

        # Кнопка 3
        self.toolButton_7 = QtWidgets.QPushButton("Открыть", self.tab_2)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setGeometry(280, 150, 59, 19)
        self.toolButton_7.clicked.connect(self.action_cliked)

        # Кнопка 4
        self.toolButton_8 = QtWidgets.QPushButton("Открыть", self.tab_2)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setGeometry(280, 200, 59, 19)
        self.toolButton_8.clicked.connect(self.action_cliked)

        # Задаем строб дальности для раздела калибровки 2
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit")
        self.lineEdit_2.setGeometry(350, 50, 75, 20)
        self.lineEdit_2.returnPressed.connect(self.get_gate_range)

        # Вывод Амплитуды 1
        self.lineEdit_13 = QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(490, 60, 60, 20)
        self.lineEdit_13.setReadOnly(True)

        # Вывод Амплитуды 2
        self.lineEdit_14 = QLineEdit(self.tab_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(690, 60, 60, 20)
        self.lineEdit_14.setReadOnly(True)

        # Вывод Амплитуды 3
        self.lineEdit_15 = QLineEdit(self.tab_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(490, 110, 60, 20)
        self.lineEdit_15.setReadOnly(True)

        # Вывод Амплитуды 4
        self.lineEdit_16 = QLineEdit(self.tab_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(690, 110, 60, 20)
        self.lineEdit_16.setReadOnly(True)

        # Вывод Фазы 1
        self.lineEdit_17 = QLineEdit(self.tab_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(570, 60, 60, 20)
        self.lineEdit_17.setReadOnly(True)

        # Вывод Фазы 2
        self.lineEdit_18 = QLineEdit(self.tab_2)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(770, 60, 60, 20)
        self.lineEdit_18.setReadOnly(True)

        # Вывод Фазы 3
        self.lineEdit_19 = QLineEdit(self.tab_2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(570, 110, 60, 20)
        self.lineEdit_19.setReadOnly(True)

        # Вывод Фазы 4
        self.lineEdit_20 = QLineEdit(self.tab_2)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(770, 110, 60, 20)
        self.lineEdit_20.setReadOnly(True)

        self.pushButton_3 = QtWidgets.QPushButton("Сохранить калибровку", self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(680, 150, 150, 25)
        self.pushButton_3.setMaximumSize(150, 30)
        self.pushButton_3.clicked.connect(self.save)

        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(850, 155, 70, 17)
        self.checkBox_2.setEnabled(False)

        # Раздел 3 Эксперимент
        # Кнопка 1
        self.toolButton_9 = QtWidgets.QPushButton("Открыть", self.tab_3)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setGeometry(280, 50, 59, 19)
        self.toolButton_9.clicked.connect(self.action_cliked)

        # Кнопка 2
        self.toolButton_10 = QtWidgets.QPushButton("Открыть", self.tab_3)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setGeometry(280, 100, 59, 19)
        self.toolButton_10.clicked.connect(self.action_cliked)

        # Кнопка 3
        self.toolButton_11 = QtWidgets.QPushButton("Открыть", self.tab_3)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setGeometry(280, 150, 59, 19)
        self.toolButton_11.clicked.connect(self.action_cliked)

        # Кнопка 4
        self.toolButton_12 = QtWidgets.QPushButton("Открыть", self.tab_3)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setGeometry(280, 200, 59, 19)
        self.toolButton_12.clicked.connect(self.action_cliked)

        # Задаем строб дальности для 3 файла
        self.lineEdit_3 = QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName(u"lineEdit")
        self.lineEdit_3.setGeometry(350, 50, 75, 20)
        self.lineEdit_3.returnPressed.connect(self.get_gate_range)

        # Вывод Амплитуды 1
        self.lineEdit_21 = QLineEdit(self.tab_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(490, 60, 60, 20)
        self.lineEdit_21.setReadOnly(True)

        # Вывод Амплитуды 2
        self.lineEdit_22 = QLineEdit(self.tab_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(690, 60, 60, 20)
        self.lineEdit_22.setReadOnly(True)

        # Вывод Амплитуды 3
        self.lineEdit_23 = QLineEdit(self.tab_3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(490, 110, 60, 20)
        self.lineEdit_23.setReadOnly(True)

        # Вывод Амплитуды 4
        self.lineEdit_24 = QLineEdit(self.tab_3)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(690, 110, 60, 20)
        self.lineEdit_24.setReadOnly(True)

        # Вывод Фазы 1
        self.lineEdit_25 = QLineEdit(self.tab_3)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(570, 60, 60, 20)
        self.lineEdit_25.setReadOnly(True)

        # Вывод Фазы 2
        self.lineEdit_26 = QLineEdit(self.tab_3)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(770, 60, 60, 20)
        self.lineEdit_26.setReadOnly(True)

        # Вывод Фазы 3
        self.lineEdit_27 = QLineEdit(self.tab_3)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(570, 110, 60, 20)
        self.lineEdit_27.setReadOnly(True)

        # Вывод Фазы 4
        self.lineEdit_28 = QLineEdit(self.tab_3)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(770, 110, 60, 20)
        self.lineEdit_28.setReadOnly(True)

        self.pushButton_4 = QtWidgets.QPushButton("Сохранить", self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(680, 150, 150, 25)
        self.pushButton_4.setMaximumSize(150, 30)
        self.pushButton_4.clicked.connect(self.save)

        self.pushButton_5 = QtWidgets.QPushButton("Сбросить калибровку", self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(680, 180, 150, 25)
        # self.pushButton_5.setMaximumSize(150, 30)
        self.pushButton_5.clicked.connect(self.clear_1)

        self.pushButton_6 = QtWidgets.QPushButton("Сбросить калибровку", self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(680, 180, 150, 25)
        self.pushButton_6.setMaximumSize(150, 30)
        self.pushButton_6.clicked.connect(self.clear_1)

        self.pushButton_7 = QtWidgets.QPushButton("Сбросить сохранение", self.tab_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(680, 180, 150, 25)
        self.pushButton_7.setMaximumSize(150, 30)
        self.pushButton_7.clicked.connect(self.clear_1)

        self.lineEdit_29 = QLineEdit(self.tab)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(20, 50, 250, 20)
        self.lineEdit_29.setReadOnly(True)

        self.lineEdit_30 = QLineEdit(self.tab)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(20, 100, 250, 20)
        self.lineEdit_30.setReadOnly(True)

        self.lineEdit_31 = QLineEdit(self.tab)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(20, 150, 250, 20)
        self.lineEdit_31.setReadOnly(True)

        self.lineEdit_32 = QLineEdit(self.tab)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setGeometry(20, 200, 250, 20)
        self.lineEdit_32.setReadOnly(True)

        self.lineEdit_33 = QLineEdit(self.tab_2)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setGeometry(20, 50, 250, 20)
        self.lineEdit_33.setReadOnly(True)

        self.lineEdit_34 = QLineEdit(self.tab_2)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setGeometry(20, 100, 250, 20)
        self.lineEdit_34.setReadOnly(True)

        self.lineEdit_35 = QLineEdit(self.tab_2)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setGeometry(20, 150, 250, 20)
        self.lineEdit_35.setReadOnly(True)

        self.lineEdit_36 = QLineEdit(self.tab_2)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setGeometry(20, 200, 250, 20)
        self.lineEdit_36.setReadOnly(True)

        self.lineEdit_37 = QLineEdit(self.tab_3)
        self.lineEdit_37.setObjectName(u"lineEdit_29")
        self.lineEdit_37.setGeometry(20, 50, 250, 20)
        self.lineEdit_37.setReadOnly(True)

        self.lineEdit_38 = QLineEdit(self.tab_3)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setGeometry(20, 100, 250, 20)
        self.lineEdit_38.setReadOnly(True)

        self.lineEdit_39 = QLineEdit(self.tab_3)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setGeometry(20, 150, 250, 20)
        self.lineEdit_39.setReadOnly(True)

        self.lineEdit_40 = QLineEdit(self.tab_3)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setGeometry(20, 200, 250, 20)
        self.lineEdit_40.setReadOnly(True)

    def save(self):
        sender = self.sender()
        try:
            if sender == self.pushButton_2:
                self.amplitude_1 = dict(self.amplitude)
                self.phase_1 = dict(self.phase)
                self.gamma = self.amplitude_1["amplitude_1"] / self.amplitude_1["amplitude_4"]
                self.alpha = self.phase_1["phase_1"] - self.phase_1["phase_4"]
                self.checkBox.setCheckState(2)
            elif sender == self.pushButton_3:
                self.amplitude_2 = dict(self.amplitude)
                self.phase_2 = dict(self.phase)
                self.betta = self.amplitude_2["amplitude_2"] / self.amplitude_2["amplitude_3"]
                self.phi = self.phase_2["phase_2"] - self.phase_2["phase_3"]
                self.checkBox_2.setCheckState(2)
            else:
                print()
        except TypeError:
            QMessageBox.about(self, "Error", "Вы не ввели путь к файлам или строб дальности")

    @QtCore.pyqtSlot()
    def get_gate_range(self):
        sender = self.sender()
        if sender == self.lineEdit:
            self.clear_1()
            self.gate_range["gate_range_1"] = self.lineEdit.text()
        elif sender == self.lineEdit_2:
            self.gate_range["gate_range_2"] = self.lineEdit_2.text()
        elif sender == self.lineEdit_3:
            self.gate_range["gate_range_3"] = self.lineEdit_3.text()

    def path_to_file(self, lineEdit, path):
        lineEdit.setText("{}".format(path))

    @QtCore.pyqtSlot()
    def action_cliked(self):
        sender = self.sender()
        if sender == self.toolButton:
            self.clear_1()
            self.file_name["path_to_file_1"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_29, self.file_name["path_to_file_1"])
        elif sender == self.toolButton_2:
            self.checkBox.setCheckState(0)
            self.file_name["path_to_file_2"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_30, self.file_name["path_to_file_2"])
        elif sender == self.toolButton_3:
            self.file_name["path_to_file_3"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_31, self.file_name["path_to_file_3"])
        elif sender == self.toolButton_4:
            self.file_name["path_to_file_4"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_32, self.file_name["path_to_file_4"])
        elif sender == self.toolButton_5:
            self.file_name["path_to_file_5"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_33, self.file_name["path_to_file_5"])
        elif sender == self.toolButton_6:
            self.file_name["path_to_file_6"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_34, self.file_name["path_to_file_6"])
        elif sender == self.toolButton_7:
            self.file_name["path_to_file_7"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_35, self.file_name["path_to_file_7"])
        elif sender == self.toolButton_8:
            self.file_name["path_to_file_8"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_36, self.file_name["path_to_file_8"])
        elif sender == self.toolButton_9:
            self.file_name["path_to_file_9"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_37, self.file_name["path_to_file_9"])
        elif sender == self.toolButton_10:
            self.file_name["path_to_file_10"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_38, self.file_name["path_to_file_10"])
        elif sender == self.toolButton_11:
            self.file_name["path_to_file_11"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_39, self.file_name["path_to_file_11"])
        elif sender == self.toolButton_12:
            self.file_name["path_to_file_12"] = QFileDialog.getOpenFileName(self)[0]
            self.path_to_file(self.lineEdit_40, self.file_name["path_to_file_12"])

    def data(self):
        if not self.checkBox.checkState() and self.amplitude_1 != None:
            range_ = range(1, 5)
            gate = 1
        elif self.checkBox.checkState() and not self.checkBox_2.checkState():
            range_ = range(5, 9)
            gate = 2
        else:
            range_ = range(9, 13)
            gate = 3
        for k in range_:
            try:
                data = bin_parser.Parser(self.file_name["path_to_file_{}".format(k)], self.gate_range["gate_range_{}".format(gate)])
                comlex = data.data()
                meanReal = np.mean([i.real for i in comlex])
                meanImag = np.mean([i.imag for i in comlex])
                self.amplitude["amplitude_{}".format(k)] = round(np.sqrt(meanReal**2 + meanImag**2), 3)
                self.phase["phase_{}".format(k)] = round(np.arctan(meanImag / meanReal), 3)
            except TypeError:
                QMessageBox.about(self, "Error", "Вы не ввели путь к файлам или строб дальности")
                break

        self.set_data()

    def set_data(self):
        if not self.checkBox.checkState():
            self.lineEdit_5.setText("{}".format(self.amplitude["amplitude_1"]))
            self.lineEdit_6.setText("{}".format(self.amplitude["amplitude_2"]))
            self.lineEdit_7.setText("{}".format(self.amplitude["amplitude_3"]))
            self.lineEdit_8.setText("{}".format(self.amplitude["amplitude_4"]))
            self.lineEdit_9.setText("{}".format(self.phase["phase_1"]))
            self.lineEdit_10.setText("{}".format(self.phase["phase_2"]))
            self.lineEdit_11.setText("{}".format(self.phase["phase_3"]))
            self.lineEdit_12.setText("{}".format(self.phase["phase_4"]))

        elif self.checkBox.checkState() and not self.checkBox_2.checkState():
            self.lineEdit_13.setText("{}".format(self.amplitude["amplitude_5"]))
            self.lineEdit_14.setText("{}".format(self.amplitude["amplitude_6"]))
            self.lineEdit_15.setText("{}".format(self.amplitude["amplitude_7"]))
            self.lineEdit_16.setText("{}".format(self.amplitude["amplitude_8"]))
            self.lineEdit_17.setText("{}".format(self.phase["phase_5"]))
            self.lineEdit_18.setText("{}".format(self.phase["phase_6"]))
            self.lineEdit_19.setText("{}".format(self.phase["phase_7"]))
            self.lineEdit_20.setText("{}".format(self.phase["phase_8"]))
        else:
            self.lineEdit_21.setText("{}".format(self.amplitude["amplitude_9"]))
            self.lineEdit_22.setText("{}".format(self.amplitude["amplitude_10"]))
            self.lineEdit_23.setText("{}".format(self.amplitude["amplitude_11"] * self.betta))
            self.lineEdit_24.setText("{}".format(self.amplitude["amplitude_12"] * self.gamma))
            self.lineEdit_25.setText("{}".format(self.phase["phase_9"]))
            self.lineEdit_26.setText("{}".format(self.phase["phase_10"]))
            self.lineEdit_27.setText("{}".format(self.phase["phase_11"] + self.alpha))
            self.lineEdit_28.setText("{}".format(self.phase["phase_12"] + self.phi))

    @QtCore.pyqtSlot()
    def exit(self):
        quit()

    def clear_1(self):
        sender = self.sender()
        if sender == self.pushButton_5 or sender == self.toolButton or sender == self.toolButton_2 or sender == self.toolButton_3 or sender == self.toolButton_4 or self.lineEdit:
            self.checkBox.setCheckState(0)
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_10.setText("")
            self.lineEdit_11.setText("")
            self.lineEdit_12.setText("")
            self.amplitude_1 = None

        elif sender == self.pushButton_6 or sender == self.toolButton_5 or sender == self.toolButton_6 or sender == self.toolButton_7 or sender == self.toolButton_8 or self.lineEdit_2:
            self.checkBox_2.setCheckState(0)
            self.lineEdit_13.setText("")
            self.lineEdit_14.setText("")
            self.lineEdit_15.setText("")
            self.lineEdit_16.setText("")
            self.lineEdit_17.setText("")
            self.lineEdit_18.setText("")
            self.lineEdit_19.setText("")
            self.lineEdit_20.setText("")
            self.amplitude_2 = None



def application():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Заказы.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Заказы(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 727)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 240, 871, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(500, 58, 290, 33))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delete_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.delete_3.setFont(font)
        self.delete_3.setObjectName("delete_3")
        self.horizontalLayout_3.addWidget(self.delete_3)
        self.leclear_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leclear_2.setFont(font)
        self.leclear_2.setObjectName("leclear_2")
        self.horizontalLayout_3.addWidget(self.leclear_2)
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(500, 20, 370, 33))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.find_2 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_2.setFont(font)
        self.find_2.setObjectName("find_2")
        self.horizontalLayout_4.addWidget(self.find_2)
        self.leinsert = QtWidgets.QLineEdit(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leinsert.setFont(font)
        self.leinsert.setObjectName("leinsert")
        self.horizontalLayout_4.addWidget(self.leinsert)
        self.cbinsert_2 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbinsert_2.setObjectName("cbinsert_2")
        self.horizontalLayout_4.addWidget(self.cbinsert_2)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 449, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.patronymic_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.patronymic_2.setFont(font)
        self.patronymic_2.setObjectName("patronymic_2")
        self.gridLayout.addWidget(self.patronymic_2, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.iddepartment_4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.iddepartment_4.setObjectName("iddepartment_4")
        self.gridLayout.addWidget(self.iddepartment_4, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.iddepartment_3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.iddepartment_3.setObjectName("iddepartment_3")
        self.gridLayout.addWidget(self.iddepartment_3, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(900, 240, 211, 461))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.find_5 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_5.setFont(font)
        self.find_5.setObjectName("find_5")
        self.gridLayout_2.addWidget(self.find_5, 0, 0, 1, 1)
        self.find_8 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_8.setFont(font)
        self.find_8.setObjectName("find_8")
        self.gridLayout_2.addWidget(self.find_8, 2, 0, 1, 1)
        self.find_9 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_9.setFont(font)
        self.find_9.setObjectName("find_9")
        self.gridLayout_2.addWidget(self.find_9, 1, 0, 1, 1)
        self.find_7 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_7.setFont(font)
        self.find_7.setObjectName("find_7")
        self.gridLayout_2.addWidget(self.find_7, 3, 0, 1, 1)
        self.find_10 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_10.setFont(font)
        self.find_10.setObjectName("find_10")
        self.gridLayout_2.addWidget(self.find_10, 4, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(501, 100, 290, 33))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_3 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.open_3.setFont(font)
        self.open_3.setObjectName("open_3")
        self.horizontalLayout.addWidget(self.open_3)
        self.leclear_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leclear_3.setFont(font)
        self.leclear_3.setObjectName("leclear_3")
        self.horizontalLayout.addWidget(self.leclear_3)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(501, 139, 95, 71))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_2 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.open_2.setFont(font)
        self.open_2.setObjectName("open_2")
        self.verticalLayout.addWidget(self.open_2)
        self.insert_2 = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.insert_2.setFont(font)
        self.insert_2.setObjectName("insert_2")
        self.verticalLayout.addWidget(self.insert_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.delete_3.setText(_translate("Form", "Удалить"))
        self.find_2.setText(_translate("Form", "Найти"))
        self.label_10.setText(_translate("Form", "Статус:"))
        self.label_8.setText(_translate("Form", "id ответсвенного сотрудника:"))
        self.label_9.setText(_translate("Form", "Дата заказа:"))
        self.label_7.setText(_translate("Form", "id основного средства:"))
        self.find_5.setText(_translate("Form", "Сотрудники"))
        self.find_8.setText(_translate("Form", "Поставки"))
        self.find_9.setText(_translate("Form", "Основные средства"))
        self.find_7.setText(_translate("Form", "Поставщики"))
        self.find_10.setText(_translate("Form", "Акты списания"))
        self.open_3.setText(_translate("Form", "Изменить"))
        self.open_2.setText(_translate("Form", "Открыть"))
        self.insert_2.setText(_translate("Form", "Добавить"))

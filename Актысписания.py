# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Актысписания.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Актысписания(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(833, 614)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 781, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 392, 123))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spisanie = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.spisanie.setFont(font)
        self.spisanie.setObjectName("spisanie")
        self.gridLayout.addWidget(self.spisanie, 1, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(429, 58, 290, 33))
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
        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(431, 140, 95, 71))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.open_2.setFont(font)
        self.open_2.setObjectName("open_2")
        self.verticalLayout.addWidget(self.open_2)
        self.insert_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.insert_2.setFont(font)
        self.insert_2.setObjectName("insert_2")
        self.verticalLayout.addWidget(self.insert_2)
        self.layoutWidget_5 = QtWidgets.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(430, 100, 290, 33))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.open_3.setFont(font)
        self.open_3.setObjectName("open_3")
        self.horizontalLayout.addWidget(self.open_3)
        self.leclear_3 = QtWidgets.QLineEdit(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leclear_3.setFont(font)
        self.leclear_3.setObjectName("leclear_3")
        self.horizontalLayout.addWidget(self.leclear_3)
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(429, 20, 370, 33))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Причина списания:"))
        self.label_5.setText(_translate("Form", "Дата списания:"))
        self.label_6.setText(_translate("Form", "id основного средства:"))
        self.delete_3.setText(_translate("Form", "Удалить"))
        self.open_2.setText(_translate("Form", "Открыть"))
        self.insert_2.setText(_translate("Form", "Добавить"))
        self.open_3.setText(_translate("Form", "Изменить"))
        self.find_2.setText(_translate("Form", "Найти"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Сотрудники.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Сотрудники (object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(782, 581)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 721, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(139, 19, 190, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.surname = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.verticalLayout.addWidget(self.surname)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.patronymic = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.patronymic.setFont(font)
        self.patronymic.setObjectName("patronymic")
        self.verticalLayout.addWidget(self.patronymic)
        self.post = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.post.setFont(font)
        self.post.setObjectName("post")
        self.verticalLayout.addWidget(self.post)
        self.iddepartment = QtWidgets.QSpinBox(self.layoutWidget)
        self.iddepartment.setObjectName("iddepartment")
        self.verticalLayout.addWidget(self.iddepartment)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 20, 105, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(341, 100, 290, 33))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.open_4.setFont(font)
        self.open_4.setObjectName("open_4")
        self.horizontalLayout_2.addWidget(self.open_4)
        self.leclear_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leclear_4.setFont(font)
        self.leclear_4.setObjectName("leclear_4")
        self.horizontalLayout_2.addWidget(self.leclear_4)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(341, 139, 95, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.open_5 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.open_5.setFont(font)
        self.open_5.setObjectName("open_5")
        self.verticalLayout_2.addWidget(self.open_5)
        self.insert_3 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.insert_3.setFont(font)
        self.insert_3.setObjectName("insert_3")
        self.verticalLayout_2.addWidget(self.insert_3)
        self.layoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_4.setGeometry(QtCore.QRect(340, 58, 290, 33))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delete_4 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.delete_4.setFont(font)
        self.delete_4.setObjectName("delete_4")
        self.horizontalLayout_3.addWidget(self.delete_4)
        self.leclear_5 = QtWidgets.QLineEdit(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leclear_5.setFont(font)
        self.leclear_5.setObjectName("leclear_5")
        self.horizontalLayout_3.addWidget(self.leclear_5)
        self.layoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_5.setGeometry(QtCore.QRect(340, 20, 370, 33))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.find_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_3.setFont(font)
        self.find_3.setObjectName("find_3")
        self.horizontalLayout_4.addWidget(self.find_3)
        self.leinsert_2 = QtWidgets.QLineEdit(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leinsert_2.setFont(font)
        self.leinsert_2.setObjectName("leinsert_2")
        self.horizontalLayout_4.addWidget(self.leinsert_2)
        self.cbinsert_3 = QtWidgets.QComboBox(self.layoutWidget_5)
        self.cbinsert_3.setObjectName("cbinsert_3")
        self.horizontalLayout_4.addWidget(self.cbinsert_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Фамилия:"))
        self.label_2.setText(_translate("Dialog", "Имя:"))
        self.label.setText(_translate("Dialog", "Отчество:"))
        self.label_4.setText(_translate("Dialog", "Должность:"))
        self.label_3.setText(_translate("Dialog", "id отдела:"))
        self.open_4.setText(_translate("Dialog", "Изменить"))
        self.open_5.setText(_translate("Dialog", "Открыть"))
        self.insert_3.setText(_translate("Dialog", "Добавить"))
        self.delete_4.setText(_translate("Dialog", "Удалить"))
        self.find_3.setText(_translate("Dialog", "Найти"))

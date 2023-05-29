import sqlite3
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog
from PyQt5 import QtWidgets
import Регистрация
import Вход
from Заказы import Ui_Заказы
from Актысписания import Ui_Актысписания
from Основныесредства import Ui_Основныесредства
from Поставки import Ui_Поставки
from Поставщики import Ui_Поставщики
from Сотрудники import Ui_Сотрудники

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(login TEXT, password TEXT)''')
db.commit()

class Registration(QtWidgets.QMainWindow, Регистрация.Ui_Регистрация):  # регистрация
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.patronymic_2.setPlaceholderText('Введите логин')
        self.patronymic_3.setPlaceholderText('Введите пароль')
        self.pushButton_2.pressed.connect(self.reg)  # регитрация
        self.pushButton.pressed.connect(self.login)  # переход на вход

    def login(self):  # показ класса логин (вход)
        self.login = Login()
        self.login.show()
        self.hide()

    def reg(self):  # регитрация
        try:
           user_login = self.patronymic_2.text()
           user_password = self.patronymic_3.text()

           if len(user_login) == 0:
               return
           if len(user_password) == 0:
               return
           cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
           if cursor.fetchone() is None:
               cursor.execute(f'INSERT INTO users VALUES("{user_login}","{user_password}")')
               self.label_9.setText(f'Аккаунт {user_login} успешно зарегистрирован')
               db.commit()
           else:
               self.label_9.setText('Такая запись уже имеется')
        except Exception as e:
            self.label_9.setText(f'Аккаунт {user_login} успешно зарегистрирован')


class Login(QtWidgets.QMainWindow, Вход.Ui_Вход):  # вход
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.patronymic_2.setPlaceholderText('Введите логин')
        self.patronymic_3.setPlaceholderText('Введите пароль')
        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.reg)

    def reg(self):
        self.reg = Registration()
        self.reg.show()
        self.hide()

    def login(self):
        try:
            user_login = self.patronymic_2.text()
            user_password = self.patronymic_3.text()

            if len(user_login) == 0:
                return
            if len(user_password) == 0:
                return

            cursor.execute(f'SELECT password FROM users WHERE login = "{user_login}"')
            check_pass = cursor.fetchall()

            cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
            check_login = cursor.fetchall()
            print(check_login)
            print(check_pass)

            if check_pass[0][0] == user_password and check_login[0][0] == user_login:
                self.label_9.setText(f'Успешная авториазация')
                self.Заказы = Заказы()
                self.Заказы.show()
                self.hide()
            else:
                self.label_9.setText(f'Ошибка авторизации')
        except Exception as e:
            self.label_9.setText(f'Ошибка авторизации')


POISK = ['id_заказа', 'id_основного_средства', 'id_ответственного_сотрудника', 'дата_заказа', 'статус']
STATYS = ['в обработке', 'выполнено']
class Заказы(QWidget, Ui_Заказы):
    def __init__(self):
        super(Заказы, self).__init__()
        self.setupUi(self)
        self.open_2.clicked.connect(self.open_zakazi)
        self.delete_3.clicked.connect(self.delete_zakazi)
        self.insert_2.clicked.connect(self.insert_zakazi)
        self.comboBox.addItems(STATYS)
        self.cbinsert_2.addItems(POISK)
        self.find_2.clicked.connect(self.search_zakazi)
        self.open_3.clicked.connect(self.update_zakazi)

        self.find_5.clicked.connect(self.show_St)
        self.find_9.clicked.connect(self.show_Os)
        self.find_8.clicked.connect(self.show_Po)
        self.find_7.clicked.connect(self.show_Pos)
        self.find_10.clicked.connect(self.show_Ak)

    def open_zakazi(self):  # кнопка
        try:
            self.conn = sqlite3.connect('kurs.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Заказы;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Заказы"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
        # заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_zakazi(self):  # кнопка добавить
        row = [self.iddepartment_3.text(), self.iddepartment_4.text(), self.patronymic_2.text(),
               self.comboBox.itemText(self.comboBox.currentIndex())]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Заказы( id_основного_средства, id_ответственного_сотрудника, дата_заказа, статус)
            values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_zakazi(self):
        id = self.leclear_2.text()
        conn = sqlite3.connect('kurs.db')
        c = conn.cursor()
        c.execute("DELETE FROM Заказы WHERE id_заказа=?", (id,))
        conn.commit()
        conn.close()
        self.update()

    def search_zakazi(self):
        column_name = self.cbinsert_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.leinsert.text()
        query = f"select * from Заказы where {column_name} like '%{search_text}%'"
        self.update(query)

    def update_zakazi(self):  # изменение
        # Открываем соединение с базой данных
        conn = sqlite3.connect('kurs.db')
        cursor = conn.cursor()

        id_основного_средства = self.iddepartment_3.text()
        id_ответственного_сотрудника = self.iddepartment_4.text()
        дата_заказа = self.patronymic_2.text()
        статус =  self.comboBox.itemText(self.comboBox.currentIndex())


        # Получаем ID_emploee из поля ввода
        id_заказа = self.leclear_3.text()

        # Обновляем запись в таблице
        try:
            cursor.execute(
                """UPDATE Заказы SET id_основного_средства=?, id_ответственного_сотрудника=?, дата_заказа=?, статус=? WHERE id_заказа=?""",
                (id_основного_средства, id_ответственного_сотрудника, дата_заказа, статус, id_заказа))
            conn.commit()
        except Exception as e:
            print("Ошибка при обновлении записи в таблице:", e)
        finally:
            cursor.close()
            conn.close()

        # Обновляем данные в таблице на форме
        self.update()


    def show_St(self):
        self.SH_st = Сотрудники()
        self.SH_st.show()

    def show_Os(self):
        self.SH_os = Основныесредства()
        self.SH_os.show()

    def show_Po(self):
        self.SH_po = Поставки()
        self.SH_po.show()

    def show_Pos(self):
        self.SH_pos = Поставщики()
        self.SH_pos.show()

    def show_Ak(self):
        self.SH_ak = Актысписания()
        self.SH_ak.show()


POISKST = ['id_сотрудника', 'фамилия', 'имя', 'отчество', 'должность', 'id_отдела']
class Сотрудники (QWidget, Ui_Сотрудники):
    def __init__(self):
        super(Сотрудники, self).__init__()
        self.setupUi(self)
        self.open_5.clicked.connect(self.open_sotrydniki)
        self.insert_3.clicked.connect(self.insert_sotrydniki)
        self.delete_4.clicked.connect(self.delete_sotrydniki)
        self.cbinsert_3.addItems(POISKST)
        self.find_3.clicked.connect(self.search_sotrydniki)
        self.open_4.clicked.connect(self.update_sotrydniki)

    def open_sotrydniki(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kurs.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Сотрудники;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Сотрудники"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
        # заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_sotrydniki(self):  # кнопка добавить
        row = [self.surname.text(), self.name.text(), self.patronymic.text(),
               self.post.text(),self.iddepartment.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Сотрудники( фамилия, имя, отчество, должность, id_отдела)
            values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_sotrydniki(self):
        id = self.leclear_5.text()
        conn = sqlite3.connect('kurs.db')
        c = conn.cursor()
        c.execute("DELETE FROM Сотрудники WHERE id_сотрудника=?", (id,))
        conn.commit()
        conn.close()
        self.update()

    def search_sotrydniki(self):
        column_name = self.cbinsert_3.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.leinsert_2.text()
        query = f"select * from Сотрудники where {column_name} like '%{search_text}%'"
        self.update(query)

    def update_sotrydniki(self):  # изменение
        # Открываем соединение с базой данных
        conn = sqlite3.connect('kurs.db')
        cursor = conn.cursor()

        фамилия = self.surname.text()
        имя = self.name.text()
        отчество = self.patronymic.text()
        должность =  self.post.text()
        id_отдела = self.iddepartment.text()


        # Получаем ID_ из поля ввода
        id_сотрудника = self.leclear_4.text()

        # Обновляем запись в таблице Emploee
        try:
            cursor.execute(
                """UPDATE Сотрудники SET фамилия=?, имя=?, отчество=?, должность=?, id_отдела=? WHERE id_сотрудника=?""",
                (фамилия, имя, отчество, должность, id_отдела, id_сотрудника))
            conn.commit()
        except Exception as e:
            print("Ошибка при обновлении записи в таблице:", e)
        finally:
            cursor.close()
            conn.close()

        # Обновляем данные в таблице на форме
        self.update()


POISKOS = ['id_основного_средства', 'наименование', 'дата_ввода_в_эксплуатацию', 'стоимость', 'id_ответственного_сотрудника']
class Основныесредства (QWidget, Ui_Основныесредства):
    def __init__(self):
        super(Основныесредства, self).__init__()
        self.setupUi(self)
        self.open_2.clicked.connect(self.open_sredstva)
        self.insert_2.clicked.connect(self.insert_sredstva)
        self.delete_3.clicked.connect(self.delete_sredstva)
        self.cbinsert_2.addItems(POISKOS)
        self.find_2.clicked.connect(self.search_sredstva)
        self.open_3.clicked.connect(self.update_sredstva)

    def open_sredstva(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kurs.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Основные_средства;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Основные_средства"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
        # заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_sredstva(self):  # кнопка добавить
        row = [self.patronymic_3.text(), self.patronymic_4.text(),
               self.patronymic_2.text(),self.iddepartment_3.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Основные_средства( наименование, дата_ввода_в_эксплуатацию, стоимость, id_ответственного_сотрудника)
            values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_sredstva(self):
        id = self.leclear_2.text()
        conn = sqlite3.connect('kurs.db')
        c = conn.cursor()
        c.execute("DELETE FROM Основные_средства WHERE id_основного_средства=?", (id,))
        conn.commit()
        conn.close()
        self.update()

    def search_sredstva(self):
        column_name = self.cbinsert_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.leinsert.text()
        query = f"select * from Основные_средства where {column_name} like '%{search_text}%'"
        self.update(query)

    def update_sredstva(self):  # изменение
        # Открываем соединение с базой данных
        conn = sqlite3.connect('kurs.db')
        cursor = conn.cursor()

        наименование = self.patronymic_4.text()
        стоимость = self.patronymic_2.text()
        id_ответственного_сотрудника = self.iddepartment_3.text()
        дата_ввода_в_эксплуатацию =  self.patronymic_3.text()


        # Получаем ID_ из поля ввода
        id_основного_средства = self.leclear_3.text()

        # Обновляем запись в таблице
        try:
            cursor.execute(
                """UPDATE Основные_средства SET наименование=?, дата_ввода_в_эксплуатацию=?, стоимость=?, id_ответственного_сотрудника=? WHERE id_основного_средства=?""",
                (наименование, дата_ввода_в_эксплуатацию, стоимость, id_ответственного_сотрудника, id_основного_средства))
            conn.commit()
        except Exception as e:
            print("Ошибка при обновлении записи в таблице:", e)
        finally:
            cursor.close()
            conn.close()

        # Обновляем данные в таблице на форме
        self.update()


POISKPO = ['id_поставки', 'id_основного_средства', 'id_поставщика', 'дата_поставки', 'стоимость']
class Поставки (QWidget, Ui_Поставки):
    def __init__(self):
        super(Поставки, self).__init__()
        self.setupUi(self)
        self.open_2.clicked.connect(self.open_postavki)
        self.insert_2.clicked.connect(self.insert_postavki)
        self.delete_3.clicked.connect(self.delete_postavki)
        self.cbinsert_2.addItems(POISKPO)
        self.find_2.clicked.connect(self.search_postavki)
        self.open_3.clicked.connect(self.update_postavki)

    def open_postavki(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kurs.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Поставки;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Поставки"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
        # заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_postavki(self):  # кнопка добавить
        row = [self.iddepartment_3.text(), self.iddepartment_4.text(),
               self.patronymic_2.text(),self.patronymic_3.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Поставки( id_основного_средства, id_поставщика, дата_поставки, стоимость)
            values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_postavki(self):
        id = self.leclear_2.text()
        conn = sqlite3.connect('kurs.db')
        c = conn.cursor()
        c.execute("DELETE FROM Поставки WHERE id_поставки=?", (id,))
        conn.commit()
        conn.close()
        self.update()

    def search_postavki(self):
        column_name = self.cbinsert_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.leinsert.text()
        query = f"select * from Поставки where {column_name} like '%{search_text}%'"
        self.update(query)

    def update_postavki(self):  # изменение
        # Открываем соединение с базой данных
        conn = sqlite3.connect('kurs.db')
        cursor = conn.cursor()

        id_основного_средства = self.iddepartment_3.text()
        id_поставщика = self.iddepartment_4.text()
        дата_поставки = self.patronymic_2.text()
        стоимость =  self.patronymic_3.text()


        # Получаем ID_ из поля ввода
        id_поставки = self.leclear_3.text()

        # Обновляем запись в таблице
        try:
            cursor.execute(
                """UPDATE Поставки SET id_основного_средства=?, id_поставщика=?, дата_поставки=?, стоимость=? WHERE id_поставки=?""",
                (id_основного_средства, id_поставщика, дата_поставки, стоимость, id_поставки))
            conn.commit()
        except Exception as e:
            print("Ошибка при обновлении записи в таблице:", e)
        finally:
            cursor.close()
            conn.close()

        # Обновляем данные в таблице на форме
        self.update()


POISKPOS = ['id_поставщика', 'наименование', 'адрес', 'телефон']
class Поставщики (QWidget, Ui_Поставщики):
    def __init__(self):
        super(Поставщики, self).__init__()
        self.setupUi(self)
        self.open_2.clicked.connect(self.open_postavhiki)
        self.insert_2.clicked.connect(self.insert_postavhiki)
        self.delete_3.clicked.connect(self.delete_postavhiki)
        self.cbinsert_2.addItems(POISKPOS)
        self.find_2.clicked.connect(self.search_postavhiki)
        self.open_3.clicked.connect(self.update_postavhiki)

    def open_postavhiki(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kurs.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Поставщики;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Поставщики"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
        # заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_postavhiki(self):  # кнопка добавить
        row = [self.patronymic_4.text(), self.patronymic_3.text(),
               self.patronymic_2.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Поставщики( наименование, адрес, телефон)
            values('{row[0]}','{row[1]}','{row[2]}')""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_postavhiki(self):
        id = self.leclear_2.text()
        conn = sqlite3.connect('kurs.db')
        c = conn.cursor()
        c.execute("DELETE FROM Поставщики WHERE id_поставщика=?", (id,))
        conn.commit()
        conn.close()
        self.update()

    def search_postavhiki(self):
        column_name = self.cbinsert_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.leinsert.text()
        query = f"select * from Поставщики where {column_name} like '%{search_text}%'"
        self.update(query)

    def update_postavhiki (self):  # изменение
        # Открываем соединение с базой данных
        conn = sqlite3.connect('kurs.db')
        cursor = conn.cursor()

        наименование = self.patronymic_4.text()
        адрес = self.patronymic_3.text()
        телефон = self.patronymic_2.text()


        # Получаем ID_ из поля ввода
        id_поставщика = self.leclear_3.text()

        # Обновляем запись в таблице
        try:
            cursor.execute(
                """UPDATE Поставщики SET наименование=?, адрес=?, телефон=?  WHERE id_поставщика=?""",
                (наименование, адрес, телефон, id_поставщика ))
            conn.commit()
        except Exception as e:
            print("Ошибка при обновлении записи в таблице:", e)
        finally:
            cursor.close()
            conn.close()

        # Обновляем данные в таблице на форме
        self.update()


POISKAK = ['id_акта', 'id_основного_средства', 'дата_списания', 'причина_списания']
class Актысписания (QWidget, Ui_Актысписания):
    def __init__(self):
        super(Актысписания, self).__init__()
        self.setupUi(self)
        self.open_2.clicked.connect(self.open_akti)
        self.insert_2.clicked.connect(self.insert_akti)
        self.delete_3.clicked.connect(self.delete_akti)
        self.cbinsert_2.addItems(POISKAK)
        self.find_2.clicked.connect(self.search_akti)
        self.open_3.clicked.connect(self.update_akti)

    def open_akti(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kurs.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Акты_списания;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Акты_списания"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
        # заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_akti(self):  # кнопка добавить
        row = [self.spinBox.text(), self.spisanie.text(),
               self.name.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Акты_списания( id_основного_средства, дата_списания, причина_списания)
            values('{row[0]}','{row[1]}','{row[2]}')""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_akti(self):
        id = self.leclear_2.text()
        conn = sqlite3.connect('kurs.db')
        c = conn.cursor()
        c.execute("DELETE FROM Акты_списания WHERE id_акта=?", (id,))
        conn.commit()
        conn.close()
        self.update()

    def search_akti(self):
        column_name = self.cbinsert_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.leinsert.text()
        query = f"select * from Акты_списания where {column_name} like '%{search_text}%'"
        self.update(query)

    def update_akti(self):  # изменение
        # Открываем соединение с базой данных
        conn = sqlite3.connect('kurs.db')
        cursor = conn.cursor()

        id_основного_средства = self.spinBox.text()
        дата_списания = self.spisanie.text()
        причина_списания = self.name.text()


        # Получаем ID_ из поля ввода
        id_акта = self.leclear_3.text()

        # Обновляем запись в таблице
        try:
            cursor.execute(
                """UPDATE Акты_списания SET id_основного_средства=?, дата_списания=?, причина_списания=?  WHERE id_акта=?""",
                (id_основного_средства, дата_списания, причина_списания, id_акта ))
            conn.commit()
        except Exception as e:
            print("Ошибка при обновлении записи в таблице:", e)
        finally:
            cursor.close()
            conn.close()

        # Обновляем данные в таблице на форме
        self.update()



App = QtWidgets.QApplication([])
window = Login()
window.show()
App.exec()

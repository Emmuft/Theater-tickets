from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import imgvx_rc, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel, QTableWidgetItem, QPushButton, QFileDialog
from registratewindow_ui import Registering
from profile_ui import Profile
from afisha_ui import Playbill
from places_ui import Places
from bye_ui import Dialog
from zakazi_ui import Order
from ticket_ui import Ticket
from onas_ui import Onas
import sqlite3
import datetime


class Entrance(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(19, 19, 741, 561))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(24, 15, 350, 530))
        self.label.setStyleSheet("border-image: url(:/newPrefix/image/vximg.jpg);\n"
                                 "border-top-left-radius:80px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(343, 15, 361, 530))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-bottom-right-radius:80px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(390, 110, 301, 61))
        self.label_3.setStyleSheet("font: 20pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.email_line_voiti = QtWidgets.QLineEdit(self.widget)
        self.email_line_voiti.setGeometry(QtCore.QRect(380, 210, 271, 61))
        self.email_line_voiti.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(46,82,101,200);\n"
                                            "color:rgba(0 ,0 ,0 ,240);\n"
                                            "padding-bottom:7px")
        self.email_line_voiti.setText("")
        self.email_line_voiti.setObjectName("email_line_voiti")
        self.password_line_voiti = QtWidgets.QLineEdit(self.widget)
        self.password_line_voiti.setGeometry(QtCore.QRect(380, 280, 271, 61))
        self.password_line_voiti.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                               "border:none;\n"
                                               "border-bottom:2px solid rgba(46,82,101,200);\n"
                                               "color:rgba(0 ,0 ,0 ,240);\n"
                                               "padding-bottom:5px")
        self.password_line_voiti.setObjectName("password_line_voiti")
        self.btn_voiti = QtWidgets.QPushButton(self.widget)
        self.btn_voiti.setGeometry(QtCore.QRect(430, 360, 181, 41))
        self.btn_voiti.setStyleSheet("QPushButton#btn_voiti{\n"
                                     "    font: 12pt \"MS Shell Dlg 2\";\n"
                                     "    background-color: rgb(152, 152, 152);\n"
                                     "    border-radius:5px;\n"
                                     "}\n"
                                     "QPushButton#pushButton:hover, #btn_voiti:hover{\n"
                                     "    background-color: rgb(97, 97, 97);\n"
                                     "}\n"
                                     "QPushButton#pushButton:pressed, #btn_voiti:pressed{\n"
                                     "    padding-left:5px;\n"
                                     "    padding-top:5px;\n"
                                     "    background-color: rgb(186, 186, 186);\n"
                                     "}")
        self.btn_voiti.setObjectName("btn_voiti")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(350, 450, 171, 20))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.registrate_btn_voiti = QtWidgets.QPushButton(self.widget)
        self.registrate_btn_voiti.setGeometry(QtCore.QRect(520, 440, 161, 41))
        self.registrate_btn_voiti.setStyleSheet("border:none;\n"
                                                "font: 10pt \"MS Shell Dlg 2\";\n"
                                                "text-decoration: underline;\n"
                                                "color: rgb(168, 55, 44);")
        self.registrate_btn_voiti.setObjectName("registrate_btn_voiti")
        self.closebtn_2 = QtWidgets.QPushButton(self.widget)
        self.closebtn_2.setGeometry(QtCore.QRect(670, 20, 31, 28))
        self.closebtn_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.closebtn_2.setObjectName("closebtn_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Добро пожаловать!"))
        self.email_line_voiti.setPlaceholderText(_translate("MainWindow", "Email"))
        self.password_line_voiti.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btn_voiti.setText(_translate("MainWindow", "Войти"))
        self.label_5.setText(_translate("MainWindow", "Нет учетной записи?"))
        self.registrate_btn_voiti.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.closebtn_2.setText(_translate("MainWindow", "X"))


class MainWindow(QtWidgets.QMainWindow, Entrance):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.registrate_btn_voiti.clicked.connect(self.openWindowTest)
        self.closebtn_2.clicked.connect(self.Closeprogram)
        self.btn_voiti.clicked.connect(self.GotoProfile)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(780, 600)
        self.password_line_voiti.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signupWindow = Register()

        self.con = sqlite3.connect("users_db.sqlite")

    def GotoProfile(self):
        cur = self.con.cursor()
        email_ = self.email_line_voiti.text()
        passw = self.password_line_voiti.text()
        result = cur.execute("SELECT * FROM user WHERE email=? AND password=?",
                             (email_, passw,)).fetchall()
        if result:
            self.profileWindow = Prof(result[0][0])
            self.profileWindow.show()
            self.close()
        else:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Данные не корректы.")

    def Closeprogram(self):
        self.destroy()
        sys.exit(app.exec_())

    def openWindowTest(self):
        self.signupWindow.show()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Register(QtWidgets.QWidget, Registering):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(780, 600)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.closebtn.clicked.connect(self.CloseProgram)
        self.btn_registrate.clicked.connect(self.Regist)
        self.btn_registrate_2.clicked.connect(self.GotoVoiti)
        self.password1_registrate.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2_registrate.setEchoMode(QtWidgets.QLineEdit.Password)
        self.con = sqlite3.connect("users_db.sqlite")

    def CloseProgram(self):
        self.destroy()
        sys.exit(app.exec_())

    def GotoVoiti(self):
        self.mainwin = MainWindow()
        self.mainwin.show()
        self.close()

    def Regist(self):
        cur = self.con.cursor()
        email_ = self.email_registrate.text()
        passw = self.password1_registrate.text()
        passw2 = self.password2_registrate.text()
        result = cur.execute("SELECT email, password FROM user WHERE email=? AND password=?",
                             (email_, passw,)).fetchall()
        if email_ and passw and passw2 and (passw == passw2) and "@" in email_ and (not result):
            cur.execute(f"INSERT INTO user(email, password) VALUES(?, ?)", (email_, passw))
            self.con.commit()
            QtWidgets.QMessageBox.information(self, "Успешно", "Вы зарегистрированы.")
        elif len(email_) == 0 or len(passw) == 0 or len(passw2) == 0:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Введите данные.")
        elif "@" not in email_:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Email должен содержать @.")
        elif result:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Такая запись имеется.")
        else:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Данные не корректы.")


class Prof(QtWidgets.QWidget, Profile):
    def __init__(self, id_user):
        super().__init__()
        self.id_user = id_user
        self.setupUi(self)
        self.setWindowTitle("Профиль")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(940, 670)
        self.email_lineprofile.setEnabled(False)
        self.con = sqlite3.connect("users_db.sqlite")
        self.update()
        self.savebutton.clicked.connect(self.Save)
        self.afisha_btn.clicked.connect(self.GotoPlaybill)
        self.zakazi_btn.clicked.connect(self.GotoZakazi)
        self.onas_btn.clicked.connect(self.GotoOnas)

    def GotoOnas(self):
        self.onas = Theatre(self, self.id_user)
        self.onas.show()
        self.hide()

    def GotoZakazi(self):
        self.zakazi = Reservation(self, self.id_user)
        self.zakazi.show()
        self.hide()

    def GotoPlaybill(self):
        self.afisha = Afisha(self, self.id_user)
        self.afisha.show()
        self.hide()

    def update(self):
        cur = self.con.cursor()
        res = cur.execute('SELECT email FROM user WHERE id=?', (self.id_user,)).fetchone()
        self.email_lineprofile.setText(res[0])
        res = cur.execute('SELECT name FROM user WHERE id=?', (self.id_user,)).fetchone()
        self.name_line.setText(res[0])
        res = cur.execute('SELECT familia FROM user WHERE id=?', (self.id_user,)).fetchone()
        self.surname_line.setText(res[0])
        res = cur.execute('SELECT surname FROM user WHERE id=?', (self.id_user,)).fetchone()
        self.patronymic_line.setText(res[0])
        res = cur.execute('SELECT number FROM user WHERE id=?', (self.id_user,)).fetchone()
        self.number_line.setText(res[0])
        res = cur.execute('SELECT gender FROM user WHERE id=?', (self.id_user,)).fetchone()
        if self.man_radioButton.text() == res[0]:
            self.man_radioButton.click()
        if self.woman_radioButton.text() == res[0]:
            self.woman_radioButton.click()
        if self.notspecified_radioButton.text() == res[0]:
            self.notspecified_radioButton.click()
        res = cur.execute('SELECT datehb FROM user WHERE id=?', (self.id_user,)).fetchone()
        self.happy_line.setText(res[0])

    def Save(self):
        cur = self.con.cursor()
        name = self.name_line.text()
        cur.execute("UPDATE user SET name=? WHERE id=? ", (name, self.id_user,)).fetchone()

        surname = self.surname_line.text()
        cur.execute("UPDATE user SET familia=? WHERE id=? ", (surname, self.id_user,)).fetchone()

        patr = self.patronymic_line.text()
        cur.execute("UPDATE user SET surname=? WHERE id=? ", (patr, self.id_user,)).fetchone()

        number = self.number_line.text()
        if len(number) == 11:
            cur.execute("UPDATE user SET number=? WHERE id=? ", (number, self.id_user,)).fetchone()

        elif len(number) == 0:
            pass
        else:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Номер телефона должен содержать 11 цифр.")

        date_line = self.happy_line.text()
        if len(date_line) == 10:
            b = date_line.split(".")
            date = str(datetime.date.today())
            a = date.split("-")
            if b[2] < a[0]:
                datehbz = self.happy_line.text()
                cur.execute("UPDATE user SET datehb=? WHERE id=? ", (datehbz, self.id_user,)).fetchone()
            else:
                QtWidgets.QMessageBox.information(self, "Ошибка", "Неверная дата.")
        elif len(date_line) == 0:
            pass
        else:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Дата должна быть формата 'ДД.ММ.ГГГГ'.")

        if self.notspecified_radioButton.isChecked():
            text = self.notspecified_radioButton.text()
            cur.execute("UPDATE user SET gender=? WHERE id=? ", (text, self.id_user,)).fetchone()
        if self.woman_radioButton.isChecked():
            text = self.woman_radioButton.text()
            cur.execute("UPDATE user SET gender=? WHERE id=? ", (text, self.id_user,)).fetchone()
        if self.man_radioButton.isChecked():
            text = self.man_radioButton.text()
            cur.execute("UPDATE user SET gender=? WHERE id=? ", (text, self.id_user,)).fetchone()
        self.con.commit()


class Afisha(QtWidgets.QWidget, Playbill):
    def __init__(self, obj, id_user):
        super().__init__()
        self.setupUi(self)
        self.id_user = id_user
        self.obj = obj
        self.setWindowTitle("Афиша")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(940, 670)
        self.bye_ticket1.clicked.connect(self.Bye_Ticket)
        self.profile_btn.clicked.connect(self.GotoProfile)
        self.zakazi_btn.clicked.connect(self.GotoZakazi)
        self.onas_btn.clicked.connect(self.GotoOnas)

    def GotoOnas(self):
        self.obj.show()
        self.close()

    def GotoZakazi(self):
        self.obj.show()
        self.close()

    def GotoProfile(self):
        self.obj.show()
        self.close()

    def Bye_Ticket(self):
        self.places = Place(self.id_user)
        self.places.show()


class Place(QtWidgets.QWidget, Places):
    def __init__(self, id_user):
        super().__init__()
        self.setupUi(self)
        self.id_user = id_user
        self.setFixedSize(450, 379)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.pushButton.clicked.connect(self.CloseProgram)
        self.con = sqlite3.connect("users_db.sqlite")

        self.pushButton_2.clicked.connect(self.Bye)
        self.pushButton_3.clicked.connect(self.Bye)
        self.pushButton_4.clicked.connect(self.Bye)
        self.pushButton_5.clicked.connect(self.Bye)
        self.pushButton_6.clicked.connect(self.Bye)
        self.pushButton_7.clicked.connect(self.Bye)
        self.pushButton_8.clicked.connect(self.Bye)
        self.pushButton_9.clicked.connect(self.Bye)
        self.pushButton_10.clicked.connect(self.Bye)
        self.pushButton_11.clicked.connect(self.Bye)
        self.pushButton_12.clicked.connect(self.Bye)
        self.pushButton_13.clicked.connect(self.Bye)
        self.pushButton_14.clicked.connect(self.Bye)
        self.pushButton_15.clicked.connect(self.Bye)
        self.pushButton_16.clicked.connect(self.Bye)
        self.pushButton_17.clicked.connect(self.Bye)
        self.pushButton_18.clicked.connect(self.Bye)
        self.pushButton_19.clicked.connect(self.Bye)
        self.pushButton_20.clicked.connect(self.Bye)
        self.pushButton_21.clicked.connect(self.Bye)
        self.pushButton_22.clicked.connect(self.Bye)
        self.pushButton_23.clicked.connect(self.Bye)
        self.pushButton_24.clicked.connect(self.Bye)
        self.pushButton_25.clicked.connect(self.Bye)
        self.pushButton_26.clicked.connect(self.Bye)
        self.pushButton_27.clicked.connect(self.Bye)
        self.pushButton_28.clicked.connect(self.Bye)
        self.pushButton_29.clicked.connect(self.Bye)
        self.pushButton_30.clicked.connect(self.Bye)
        self.pushButton_31.clicked.connect(self.Bye)
        self.pushButton_32.clicked.connect(self.Bye)
        self.pushButton_33.clicked.connect(self.Bye)
        self.pushButton_34.clicked.connect(self.Bye)
        self.pushButton_35.clicked.connect(self.Bye)
        self.pushButton_36.clicked.connect(self.Bye)
        self.pushButton_37.clicked.connect(self.Bye)
        self.pushButton_38.clicked.connect(self.Bye)
        self.pushButton_39.clicked.connect(self.Bye)
        self.pushButton_40.clicked.connect(self.Bye)
        self.pushButton_41.clicked.connect(self.Bye)
        self.pushButton_42.clicked.connect(self.Bye)
        self.pushButton_43.clicked.connect(self.Bye)
        self.pushButton_44.clicked.connect(self.Bye)
        self.pushButton_45.clicked.connect(self.Bye)
        self.pushButton_46.clicked.connect(self.Bye)
        self.pushButton_47.clicked.connect(self.Bye)
        self.pushButton_48.clicked.connect(self.Bye)
        self.pushButton_49.clicked.connect(self.Bye)
        self.pushButton_50.clicked.connect(self.Bye)
        self.pushButton_51.clicked.connect(self.Bye)
        self.pushButton_52.clicked.connect(self.Bye)
        self.pushButton_53.clicked.connect(self.Bye)
        self.pushButton_54.clicked.connect(self.Bye)
        self.pushButton_55.clicked.connect(self.Bye)
        self.pushButton_56.clicked.connect(self.Bye)
        self.pushButton_57.clicked.connect(self.Bye)
        self.pushButton_58.clicked.connect(self.Bye)
        self.pushButton_59.clicked.connect(self.Bye)

    def Bye(self):
        self.byeticket = Byeticket(self.sender().text(), self.id_user)
        self.byeticket.show()

    def CloseProgram(self):
        self.close()


class Byeticket(QtWidgets.QWidget, Dialog):
    def __init__(self, place, id_user):
        super().__init__()
        self.setupUi(self)
        self.place = place
        self.id_user = id_user
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(400, 119)
        self.setWindowTitle("Покупка")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.yes.clicked.connect(self.ChoiceYes)
        self.pushButton.clicked.connect(self.ChoiceNo)
        self.con = sqlite3.connect("users_db.sqlite")

    def ChoiceNo(self):
        self.close()

    def ChoiceYes(self):
        cur = self.con.cursor()
        data = datetime.date.today()
        organisat, prace = "ТЕАТР", "500"
        result = cur.execute("SELECT place FROM ticket WHERE place=?", (self.place,)).fetchall()
        if not result:
            cur.execute(f"INSERT INTO ticket(date, organisate, prace, place) VALUES(?, ?, ?, ?)",
                        (data, organisat, prace, self.place))
            res = cur.execute("SELECT number FROM ticket").fetchall()[-1][0]
            cur.execute("INSERT INTO ticket_user(id_user, id_ticket) VALUES(?, ?)", (self.id_user, res))
            self.close()
        else:
            QtWidgets.QMessageBox.information(self, "Ошибка", "Билет куплен")

        self.con.commit()


class Reservation(QtWidgets.QWidget, Order):
    def __init__(self, obj, id_user):
        super().__init__()
        self.setupUi(self)
        self.id_user = id_user
        self.obj = obj
        self.setWindowTitle("Билеты")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(940, 670)
        self.profile_btn.clicked.connect(self.Goto)
        self.con = sqlite3.connect("users_db.sqlite")
        cur = self.con.cursor()
        res = cur.execute("SELECT id_ticket FROM ticket_user WHERE id_user=?", (self.id_user,)).fetchall()
        for elem in res:
            for elem2 in elem:
                res2 = cur.execute("SELECT * FROM ticket WHERE number=?", (elem2,)).fetchall()
                for val in res2:
                    number = str(val[0])
                    data = val[1]
                    organisat = val[2]
                    prace = str(val[3])
                    self.Podrob = QtWidgets.QPushButton("Подробнее")
                    rowPosition = self.table_zakazi.rowCount()
                    self.table_zakazi.insertRow(rowPosition)
                    self.table_zakazi.setItem(rowPosition, 0, QTableWidgetItem(number))
                    self.table_zakazi.setItem(rowPosition, 1, QTableWidgetItem(data))
                    self.table_zakazi.setItem(rowPosition, 2, QTableWidgetItem(organisat))
                    self.table_zakazi.setItem(rowPosition, 3, QTableWidgetItem(prace))
                    self.table_zakazi.setCellWidget(rowPosition, 4, self.Podrob)
                    self.Podrob.clicked.connect(self.podrobnee)

    def podrobnee(self):
        self.tic = Tickets(self.id_user)
        self.tic.show()

    def Goto(self):
        self.obj.show()
        self.close()


class Tickets(QtWidgets.QWidget, Ticket):
    def __init__(self, id_user):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(981, 331)
        self.id_user = id_user
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.pushButton.clicked.connect(self.CloseProgram)
        self.saveticket.clicked.connect(self.savetick)
        self.con = sqlite3.connect("users_db.sqlite")
        cur = self.con.cursor()
        res = cur.execute("SELECT id_ticket FROM ticket_user WHERE id_user=?", (self.id_user,)).fetchall()
        for elem in res:
            for elem2 in elem:
                res2 = cur.execute("SELECT * FROM ticket WHERE number=?", (elem2,)).fetchall()
                for val in res2:
                    if val:
                        organisat = val[2]
                        prace = str(val[3])
                        place = val[4]
                        self.organisattick.setText(organisat)
                        self.placetic.setText(place)
                        self.pracetic.setText(prace)
                    else:
                        pass
        res2 = cur.execute("SELECT * FROM user WHERE id=?", (self.id_user,)).fetchall()
        for elem in res2:
            if (elem[3] and elem[4] and elem[5]) != None:
                fio = elem[3] + " " + elem[4] + " " + elem[5]
                numberphone = elem[8]
                self.fiotic.setText(fio)
                self.numbertic.setText(numberphone)
            else:
                fio = elem[3]
                numberphone = elem[8]
                self.fiotic.setText(fio)
                self.numbertic.setText(numberphone)

    def savetick(self):
        self.label_4.setText("Файл сохранен")
        global fio, numberphone
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'w') as file:
                cur = self.con.cursor()
                res = cur.execute("SELECT id_ticket FROM ticket_user WHERE id_user=?", (self.id_user,)).fetchall()
                for elem in res:
                    for elem2 in elem:
                        res2 = cur.execute("SELECT * FROM ticket WHERE number=?", (elem2,)).fetchall()
                        for val in res2:
                            organisat = val[2]
                            prace = str(val[3])
                            place = val[4]
                            file.write(
                                f"Организация {organisat} \nМесто {place} \nЦена {prace} \n")
                    break
                res2 = cur.execute("SELECT * FROM user WHERE id=?", (self.id_user,)).fetchall()
                for elem in res2:
                    fio = elem[3] + " " + elem[4] + " " + elem[5]
                    numberphone = elem[8]
                    file.write(f"ФИО {fio} \nНомер телефона {numberphone}")

    def CloseProgram(self):
        self.close()


class Theatre(QtWidgets.QWidget, Onas):
    def __init__(self, obj, id_user):
        super().__init__()
        self.setupUi(self)
        self.id_user = id_user
        self.obj = obj
        self.setWindowTitle("О театре")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setFixedSize(940, 670)
        self.profile_btn.clicked.connect(self.Goto)
        self.zakazi_btn.clicked.connect(self.Goto)
        self.afisha_btn.clicked.connect(self.Goto)

    def Goto(self):
        self.obj.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    w = MainWindow()
    w.setWindowIcon(QtGui.QIcon('icon.png'))
    w.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

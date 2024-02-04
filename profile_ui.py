from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Profile(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 670)
        self.profile_btn = QtWidgets.QPushButton(Form)
        self.profile_btn.setGeometry(QtCore.QRect(630, 20, 141, 61))
        self.profile_btn.setStyleSheet("QPushButton#profile_btn {\n"
                                       " font: 16pt \"Arial\";\n"
                                       " border: 1px solid #bfbfbf;\n"
                                       " background-color: rgb(255, 255, 255);\n"
                                       " border-radius: 4px;\n"
                                       " padding: 0.8em 1.2em 0.8em 1em;\n"
                                       " transition: all ease-in-out 0.2s;\n"
                                       " font-size: 16px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#profile_btn span {\n"
                                       " display: flex;\n"
                                       " justify-content: center;\n"
                                       " align-items: center;\n"
                                       " color: #fff;\n"
                                       " font-weight: 600;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#profile_btn:hover, #profile_btn:hover {\n"
                                       "    background-color: rgb(231, 231, 231);\n"
                                       "}")
        self.profile_btn.setObjectName("profile_btn")
        self.zakazi_btn = QtWidgets.QPushButton(Form)
        self.zakazi_btn.setGeometry(QtCore.QRect(770, 20, 141, 61))
        self.zakazi_btn.setStyleSheet("QPushButton#zakazi_btn {\n"
                                      " font: 16pt \"Arial\";\n"
                                      " border: 1px solid #bfbfbf;\n"
                                      " background-color: rgb(255, 255, 255);\n"
                                      " border-radius: 4px;\n"
                                      " padding: 0.8em 1.2em 0.8em 1em;\n"
                                      " transition: all ease-in-out 0.2s;\n"
                                      " font-size: 16px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#zakazi_btn span {\n"
                                      " display: flex;\n"
                                      " justify-content: center;\n"
                                      " align-items: center;\n"
                                      " color: #fff;\n"
                                      " font-weight: 600;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#zakazi_btn:hover, #zakazi_btn:hover {\n"
                                      "        background-color: rgb(199, 199, 199);\n"
                                      "}")
        self.zakazi_btn.setObjectName("zakazi_btn")
        self.afisha_btn = QtWidgets.QPushButton(Form)
        self.afisha_btn.setGeometry(QtCore.QRect(30, 20, 201, 61))
        self.afisha_btn.setStyleSheet("QPushButton#afisha_btn {\n"
                                      " font: 16pt \"MS Shell Dlg 2\";\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      " border: 1px solid #bfbfbf;\n"
                                      " border-radius: 4px;\n"
                                      " padding: 0.8em 1.2em 0.8em 1em;\n"
                                      " transition: all ease-in-out 0.2s;\n"
                                      " font-size: 16px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#afisha_btn span {\n"
                                      " display: flex;\n"
                                      " justify-content: center;\n"
                                      " align-items: center;\n"
                                      " color: #fff;\n"
                                      " font-weight: 600;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#afisha_btn:hover, #afisha_btn:hover {\n"
                                      "        background-color: rgb(231, 231, 231);\n"
                                      "}")
        self.afisha_btn.setObjectName("afisha_btn")
        self.onas_btn = QtWidgets.QPushButton(Form)
        self.onas_btn.setGeometry(QtCore.QRect(230, 20, 141, 61))
        self.onas_btn.setStyleSheet("QPushButton#onas_btn {\n"
                                    " font: 16pt \"MS Shell Dlg 2\";\n"
                                    " border: 1px solid #bfbfbf;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    " border-radius: 4px;\n"
                                    " padding: 0.8em 1.2em 0.8em 1em;\n"
                                    " transition: all ease-in-out 0.2s;\n"
                                    " font-size: 16px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#onas_btn span {\n"
                                    " display: flex;\n"
                                    " justify-content: center;\n"
                                    " align-items: center;\n"
                                    " color: #fff;\n"
                                    " font-weight: 600;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#onas_btn:hover, #onas_btn:hover {\n"
                                    "    background-color: rgb(231, 231, 231);\n"
                                    "}")
        self.onas_btn.setObjectName("onas_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 120, 331, 51))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
                                 "\n"
                                 "\n"
                                 "")
        self.label.setObjectName("label")
        self.name_line = QtWidgets.QLineEdit(Form)
        self.name_line.setGeometry(QtCore.QRect(60, 230, 281, 31))
        self.name_line.setStyleSheet("border-radius:8px;\n"
                                     "background-color: rgb(229, 229, 229);\n"
                                     "")
        self.name_line.setObjectName("name_line")
        self.surname_line = QtWidgets.QLineEdit(Form)
        self.surname_line.setGeometry(QtCore.QRect(60, 320, 281, 31))
        self.surname_line.setStyleSheet("border-radius:8px;\n"
                                        "background-color: rgb(229, 229, 229);\n"
                                        "")
        self.surname_line.setObjectName("surname_line")
        self.patronymic_line = QtWidgets.QLineEdit(Form)
        self.patronymic_line.setGeometry(QtCore.QRect(60, 410, 281, 31))
        self.patronymic_line.setStyleSheet("border-radius:8px;\n"
                                           "background-color: rgb(229, 229, 229);\n"
                                           "")
        self.patronymic_line.setObjectName("patronymic_line")
        self.notspecified_radioButton = QtWidgets.QRadioButton(Form)
        self.notspecified_radioButton.setGeometry(QtCore.QRect(60, 598, 121, 31))
        self.notspecified_radioButton.setStyleSheet("\n"
                                                    "border-radius:1px;\n"
                                                    "color: rgb(0, 0, 0);\n"
                                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.notspecified_radioButton.setObjectName("notspecified_radioButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 560, 51, 31))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                   "\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.woman_radioButton = QtWidgets.QRadioButton(Form)
        self.woman_radioButton.setGeometry(QtCore.QRect(190, 596, 81, 41))
        self.woman_radioButton.setStyleSheet("\n"
                                             "border-radius:1px;\n"
                                             "color: rgb(0, 0, 0);\n"
                                             "font: 12pt \"MS Shell Dlg 2\";")
        self.woman_radioButton.setObjectName("woman_radioButton")
        self.man_radioButton = QtWidgets.QRadioButton(Form)
        self.man_radioButton.setGeometry(QtCore.QRect(270, 602, 121, 31))
        self.man_radioButton.setStyleSheet("\n"
                                           "border-radius:1px;\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "font: 12pt \"MS Shell Dlg 2\";")
        self.man_radioButton.setObjectName("man_radioButton")
        self.happy_line = QtWidgets.QLineEdit(Form)
        self.happy_line.setGeometry(QtCore.QRect(60, 500, 281, 31))
        self.happy_line.setStyleSheet("border-radius:8px;\n"
                                      "background-color: rgb(229, 229, 229);\n"
                                      "")
        self.happy_line.setObjectName("happy_line")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(-40, 90, 1011, 641))
        self.label_7.setStyleSheet("border-radius: 8px;\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(-26, -5, 1001, 101))
        self.label_8.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(530, 120, 391, 51))
        self.label_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
                                   "\n"
                                   "")
        self.label_9.setObjectName("label_9")
        self.number_line = QtWidgets.QLineEdit(Form)
        self.number_line.setGeometry(QtCore.QRect(570, 230, 301, 31))
        self.number_line.setStyleSheet("border-radius:8px;\n"
                                       "background-color: rgb(229, 229, 229);\n"
                                       "")
        self.number_line.setObjectName("number_line")
        self.email_lineprofile = QtWidgets.QLineEdit(Form)
        self.email_lineprofile.setGeometry(QtCore.QRect(570, 320, 301, 31))
        self.email_lineprofile.setStyleSheet("border-radius:8px;\n"
                                             "background-color: rgb(229, 229, 229);\n"
                                             "")
        self.email_lineprofile.setObjectName("email_lineprofile")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 331, 81))
        self.label_6.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                   "border-radius: 0px;\n"
                                   "")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(530, 110, 381, 71))
        self.label_10.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                    "border-radius: 0px;\n"
                                    "")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(60, 210, 281, 81))
        self.label_12.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                    "border-radius: 0px;\n"
                                    "")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(570, 210, 301, 81))
        self.label_14.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                    "border-radius: 0px;\n"
                                    "")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(60, 300, 281, 81))
        self.label_15.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                    "border-radius: 0px;\n"
                                    "")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(60, 380, 281, 91))
        self.label_13.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                    "border-radius: 0px;\n"
                                    "")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.savebutton = QtWidgets.QPushButton(Form)
        self.savebutton.setGeometry(QtCore.QRect(770, 590, 141, 61))
        self.savebutton.setStyleSheet("QPushButton#savebutton {\n"
                                      " font: 16pt \"Arial\";\n"
                                      " border: 1px solid #bfbfbf;\n"
                                      " background-color: rgb(255, 255, 255);\n"
                                      " border-radius: 4px;\n"
                                      " padding: 0.8em 1.2em 0.8em 1em;\n"
                                      " transition: all ease-in-out 0.2s;\n"
                                      " font-size: 16px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#savebutton span {\n"
                                      " display: flex;\n"
                                      " justify-content: center;\n"
                                      " align-items: center;\n"
                                      " color: #fff;\n"
                                      " font-weight: 600;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#savebutton:hover, #savebutton:hover {\n"
                                      "        background-color: rgb(199, 199, 199);\n"
                                      "}")
        self.savebutton.setObjectName("savebutton")
        self.label_7.raise_()
        self.label_14.raise_()
        self.label_13.raise_()
        self.label_15.raise_()
        self.label_12.raise_()
        self.label_8.raise_()
        self.profile_btn.raise_()
        self.zakazi_btn.raise_()
        self.afisha_btn.raise_()
        self.onas_btn.raise_()
        self.label.raise_()
        self.name_line.raise_()
        self.surname_line.raise_()
        self.patronymic_line.raise_()
        self.notspecified_radioButton.raise_()
        self.label_5.raise_()
        self.woman_radioButton.raise_()
        self.man_radioButton.raise_()
        self.happy_line.raise_()
        self.label_9.raise_()
        self.number_line.raise_()
        self.email_lineprofile.raise_()
        self.label_6.raise_()
        self.label_10.raise_()
        self.savebutton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.profile_btn.setText(_translate("Form", "Профиль"))
        self.zakazi_btn.setText(_translate("Form", "Заказы"))
        self.afisha_btn.setText(_translate("Form", "Купить билет"))
        self.onas_btn.setText(_translate("Form", "О нас"))
        self.label.setText(_translate("Form", "Личная информация"))
        self.name_line.setPlaceholderText(_translate("Form", "Имя"))
        self.surname_line.setPlaceholderText(_translate("Form", "Фамилия"))
        self.patronymic_line.setPlaceholderText(_translate("Form", "Отчество"))
        self.notspecified_radioButton.setText(_translate("Form", "Не указан"))
        self.label_5.setText(_translate("Form", "Пол"))
        self.woman_radioButton.setText(_translate("Form", "Жен."))
        self.man_radioButton.setText(_translate("Form", "Муж."))
        self.happy_line.setPlaceholderText(_translate("Form", "День рождения"))
        self.label_9.setText(_translate("Form", "Контактная информация"))
        self.number_line.setPlaceholderText(_translate("Form", "Мобильный телефон"))
        self.email_lineprofile.setText(_translate("Form", "-"))
        self.email_lineprofile.setPlaceholderText(_translate("Form", "Электронная почта"))
        self.savebutton.setText(_translate("Form", "Сохранить"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Form
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

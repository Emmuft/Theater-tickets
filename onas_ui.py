from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Onas(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 670)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(-20, 0, 1001, 101))
        self.label_8.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 210, 431, 61))
        self.label.setStyleSheet("font: 75 20pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 110, 121, 31))
        self.label_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(223, 223, 223);\n"
                                   "border-radius:10px")
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 120, 941, 21))
        self.label_7.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                   "border-radius: 5px;\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 340, 431, 71))
        self.label_2.setStyleSheet("font: 20pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 140, 581, 531))
        self.label_3.setStyleSheet("border-image: url(:/newPrefix/onasimg.jpg);\n"
                                   "border-radius:50%;\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.afisha_btn.setText(_translate("Form", "Купить билет"))
        self.onas_btn.setText(_translate("Form", "О нас"))
        self.profile_btn.setText(_translate("Form", "Профиль"))
        self.zakazi_btn.setText(_translate("Form", "Заказы"))
        self.label.setText(_translate("Form", "Номер телефона: \n"
                                              " +79645782341"))
        self.label_9.setText(_translate("Form", "Театр"))
        self.label_2.setText(_translate("Form", "Адрес: \n"
                                                " Люблинская 161"))


import onasimg_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Form
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

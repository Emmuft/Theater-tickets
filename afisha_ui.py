from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import imgafisha_rc


class Playbill(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(940, 670)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 90, 951, 581))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 949, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(10, 50, 941, 221))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 20, 191, 181))
        self.label.setStyleSheet("border-image: url(:/lol/2Gr5mb1g7dQ.jpg);\n"
                                 "border-radius: 5px;\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 641, 41))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 681, 121))
        self.label_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.bye_ticket1 = QtWidgets.QPushButton(self.widget)
        self.bye_ticket1.setGeometry(QtCore.QRect(710, 160, 181, 51))
        self.bye_ticket1.setStyleSheet("QPushButton#bye_ticket1 {\n"
                                       " font: 14pt \"MS Shell Dlg 2\";\n"
                                       " border: 1px solid #bfbfbf;\n"
                                       "background-color: rgb(223, 223, 223);\n"
                                       " border-radius: 4px;\n"
                                       " padding: 0.8em 1.2em 0.8em 1em;\n"
                                       " transition: all ease-in-out 0.2s;\n"
                                       " font-size: 16px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#bye_ticket1 {\n"
                                       " display: flex;\n"
                                       " justify-content: center;\n"
                                       " align-items: center;\n"
                                       " font-weight: 600;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#bye_ticket1:hover, #bye_ticket1:hover {\n"
                                       "    background-color: rgb(186, 186, 186);\n"
                                       "}")
        self.bye_ticket1.setObjectName("bye_ticket1")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(10, 320, 941, 221))
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 191, 181))
        self.label_4.setStyleSheet("border-image: url(:/lol/xV0w1WdZods.jpg);\n"
                                   "border-radius: 5px;\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(250, 20, 641, 41))
        self.label_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(250, 60, 681, 121))
        self.label_6.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.bye_ticket2 = QtWidgets.QPushButton(self.widget_2)
        self.bye_ticket2.setGeometry(QtCore.QRect(710, 160, 181, 51))
        self.bye_ticket2.setStyleSheet("QPushButton#bye_ticket2 {\n"
                                       " font: 14pt \"MS Shell Dlg 2\";\n"
                                       " border: 1px solid #bfbfbf;\n"
                                       "background-color: rgb(223, 223, 223);\n"
                                       " border-radius: 4px;\n"
                                       " padding: 0.8em 1.2em 0.8em 1em;\n"
                                       " transition: all ease-in-out 0.2s;\n"
                                       " font-size: 16px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#bye_ticket2 {\n"
                                       " display: flex;\n"
                                       " justify-content: center;\n"
                                       " align-items: center;\n"
                                       " font-weight: 600;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#bye_ticket2:hover, #bye_ticket2:hover {\n"
                                       "    background-color: rgb(186, 186, 186);\n"
                                       "}")
        self.bye_ticket2.setObjectName("bye_ticket2")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(10, 275, 941, 21))
        self.label_7.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                   "border-radius: 5px;\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(40, 10, 121, 31))
        self.label_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(223, 223, 223);\n"
                                   "border-radius:10px")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(10, 21, 941, 20))
        self.label_10.setStyleSheet("border-bottom: 1px solid #bfbfbf;\n"
                                    "border-radius: 5px;\n"
                                    "")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.widget.raise_()
        self.widget_2.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(-60, -10, 1001, 101))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Моя милая леди"))
        self.label_3.setText(
            _translate("Form", " Историю об ученом и филологе Генри Хиггинсе, который принимает на себя\n"
                               " задачу превратить девушку-цветочницу  по имени Эльиза Дулитл  в истинную \n"
                               " леди, с помощью своей уникальной методики обучения."))
        self.bye_ticket1.setText(_translate("Form", "Купить билеты"))
        self.label_5.setText(_translate("Form", "Шахерезада"))
        self.label_6.setText(_translate("Form", "Девушка была дочерью главного визиря персидского царя. Ее сестра \n"
                                                " была убита правителем  в ночь свадьбы, поэтому Шахиризада\n"
                                                " решила помститься и спасти других женщин от смерти. "))
        self.bye_ticket2.setText(_translate("Form", "Купить билеты"))
        self.label_9.setText(_translate("Form", "Афиша"))
        self.afisha_btn.setText(_translate("Form", "Купить билет"))
        self.onas_btn.setText(_translate("Form", "О нас"))
        self.profile_btn.setText(_translate("Form", "Профиль"))
        self.zakazi_btn.setText(_translate("Form", "Заказы"))


import imgafisha_rc
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Form
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
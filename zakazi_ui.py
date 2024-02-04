import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Order(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(939, 670)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 940, 670))
        self.widget.setObjectName("widget")
        self.afisha_btn = QtWidgets.QPushButton(self.widget)
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
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(-20, 0, 1001, 101))
        self.label_8.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.onas_btn = QtWidgets.QPushButton(self.widget)
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
        self.profile_btn = QtWidgets.QPushButton(self.widget)
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
        self.zakazi_btn = QtWidgets.QPushButton(self.widget)
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
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(-30, 100, 1011, 651))
        self.label_7.setStyleSheet("border-radius: 8px;\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.table_zakazi = QtWidgets.QTableWidget(self.widget)
        self.table_zakazi.setGeometry(QtCore.QRect(0, 100, 941, 571))
        self.table_zakazi.setStyleSheet("")
        self.table_zakazi.setObjectName("table_zakazi")
        self.table_zakazi.setColumnCount(5)
        self.table_zakazi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_zakazi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_zakazi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_zakazi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_zakazi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_zakazi.setHorizontalHeaderItem(4, item)
        self.table_zakazi.horizontalHeader().setDefaultSectionSize(185)
        self.table_zakazi.horizontalHeader().setMinimumSectionSize(51)
        self.table_zakazi.verticalHeader().setDefaultSectionSize(45)
        self.label_7.raise_()
        self.label_8.raise_()
        self.afisha_btn.raise_()
        self.onas_btn.raise_()
        self.profile_btn.raise_()
        self.zakazi_btn.raise_()
        self.table_zakazi.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.afisha_btn.setText(_translate("Form", "Купить билет"))
        self.onas_btn.setText(_translate("Form", "О нас"))
        self.profile_btn.setText(_translate("Form", "Профиль"))
        self.zakazi_btn.setText(_translate("Form", "Заказы"))
        item = self.table_zakazi.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Номер"))
        item = self.table_zakazi.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Дата"))
        item = self.table_zakazi.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Организация"))
        item = self.table_zakazi.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Сумма"))
        item = self.table_zakazi.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Подробнее"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Form
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

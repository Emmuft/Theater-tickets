import imgreg_rc, sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Registering(object):
    def setupUi(self, SignupWindow):
        SignupWindow.setObjectName("Form")
        SignupWindow.resize(780, 600)
        self.widget = QtWidgets.QWidget(SignupWindow)
        self.widget.setGeometry(QtCore.QRect(30, 20, 741, 561))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(24, 15, 350, 530))
        self.label.setStyleSheet("border-image: url(:/ahaha/rgimg.jpg);\n"
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
        self.label_3.setGeometry(QtCore.QRect(430, 80, 181, 61))
        self.label_3.setStyleSheet("font: 20pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.email_registrate = QtWidgets.QLineEdit(self.widget)
        self.email_registrate.setGeometry(QtCore.QRect(380, 150, 271, 61))
        self.email_registrate.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(46,82,101,200);\n"
                                            "color:rgba(0 ,0 ,0 ,240);\n"
                                            "padding-bottom:7px")
        self.email_registrate.setText("")
        self.email_registrate.setObjectName("email_registrate")
        self.password1_registrate = QtWidgets.QLineEdit(self.widget)
        self.password1_registrate.setGeometry(QtCore.QRect(380, 240, 271, 61))
        self.password1_registrate.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                                "border:none;\n"
                                                "border-bottom:2px solid rgba(46,82,101,200);\n"
                                                "color:rgba(0 ,0 ,0 ,240);\n"
                                                "padding-bottom:5px")
        self.password1_registrate.setObjectName("password1_registrate")
        self.btn_registrate = QtWidgets.QPushButton(self.widget)
        self.btn_registrate.setGeometry(QtCore.QRect(370, 430, 140, 40))
        self.btn_registrate.setStyleSheet("QPushButton#pushButton, #btn_registrate{\n"
                                          "    font: 12pt \"MS Shell Dlg 2\";\n"
                                          "    \n"
                                          "    background-color: rgb(152, 152, 152);\n"
                                          "    border-radius:5px;\n"
                                          "}\n"
                                          "QPushButton#pushButton:hover, #btn_registrate:hover{\n"
                                          "    background-color: rgb(97, 97, 97);\n"
                                          "}\n"
                                          "QPushButton#pushButton:pressed, #btn_registrate:pressed{\n"
                                          "    padding-left:5px;\n"
                                          "    padding-top:5px;\n"
                                          "    background-color: rgb(186, 186, 186);\n"
                                          "}")
        self.btn_registrate.setObjectName("btn_registrate")
        self.password2_registrate = QtWidgets.QLineEdit(self.widget)
        self.password2_registrate.setGeometry(QtCore.QRect(380, 330, 271, 61))
        self.password2_registrate.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                                "border:none;\n"
                                                "border-bottom:2px solid rgba(46,82,101,200);\n"
                                                "color:rgba(0 ,0 ,0 ,240);\n"
                                                "padding-bottom:7px")
        self.password2_registrate.setText("")
        self.password2_registrate.setObjectName("password2_registrate")
        self.closebtn = QtWidgets.QPushButton(self.widget)
        self.closebtn.setGeometry(QtCore.QRect(670, 20, 31, 28))
        self.closebtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.closebtn.setObjectName("closebtn")
        self.btn_registrate_2 = QtWidgets.QPushButton(self.widget)
        self.btn_registrate_2.setGeometry(QtCore.QRect(530, 430, 140, 40))
        self.btn_registrate_2.setStyleSheet("QPushButton#pushButton, #btn_registrate_2{\n"
                                            "    font: 12pt \"MS Shell Dlg 2\";\n"
                                            "    \n"
                                            "    background-color: rgb(152, 152, 152);\n"
                                            "    border-radius:5px;\n"
                                            "}\n"
                                            "QPushButton#pushButton:hover, #btn_registrate_2:hover{\n"
                                            "    background-color: rgb(97, 97, 97);\n"
                                            "}\n"
                                            "QPushButton#pushButton:pressed, #btn_registrate_2:pressed{\n"
                                            "    padding-left:5px;\n"
                                            "    padding-top:5px;\n"
                                            "    background-color: rgb(186, 186, 186);\n"
                                            "}")
        self.btn_registrate_2.setObjectName("btn_registrate_2")

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Регистрация"))
        self.email_registrate.setPlaceholderText(_translate("Form", "Email"))
        self.password1_registrate.setPlaceholderText(_translate("Form", "Придумайте пароль"))
        self.btn_registrate.setText(_translate("Form", "Регистрация"))
        self.password2_registrate.setPlaceholderText(_translate("Form", "Повторите пароль"))
        self.closebtn.setText(_translate("Form", "X"))
        self.btn_registrate_2.setText(_translate("Form", "Вход"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SignupWindow = QtWidgets.QMainWindow()
    ui = SignupWindow
    ui.setupUi(SignupWindow)
    SignupWindow.show()
    sys.exit(app.exec_())
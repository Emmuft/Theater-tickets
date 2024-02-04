import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 119)
        self.yes = QtWidgets.QPushButton(Form)
        self.yes.setGeometry(QtCore.QRect(40, 60, 121, 41))
        self.yes.setObjectName("yes")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 281, 51))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 60, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yes.setText(_translate("Form", "Да"))
        self.label.setText(_translate("Form", "Вы хотите купить билет?"))
        self.pushButton.setText(_translate("Form", "Нет"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Form
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

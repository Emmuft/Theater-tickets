import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Places(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 379)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 431, 361))
        self.widget.setStyleSheet("background-color: rgb(229, 229, 229);\n"
                                  "")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(390, 10, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 150, 21, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 150, 21, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 150, 21, 21))
        self.pushButton_4.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 150, 21, 21))
        self.pushButton_5.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 150, 21, 21))
        self.pushButton_6.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 150, 21, 21))
        self.pushButton_7.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 150, 21, 21))
        self.pushButton_8.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 150, 21, 21))
        self.pushButton_9.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 150, 21, 21))
        self.pushButton_10.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(340, 150, 21, 21))
        self.pushButton_11.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 180, 21, 21))
        self.pushButton_12.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setGeometry(QtCore.QRect(100, 180, 21, 21))
        self.pushButton_13.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setGeometry(QtCore.QRect(70, 180, 21, 21))
        self.pushButton_14.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.widget)
        self.pushButton_15.setGeometry(QtCore.QRect(40, 180, 21, 21))
        self.pushButton_15.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_16.setGeometry(QtCore.QRect(160, 180, 21, 21))
        self.pushButton_16.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget)
        self.pushButton_17.setGeometry(QtCore.QRect(190, 180, 21, 21))
        self.pushButton_17.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget)
        self.pushButton_18.setGeometry(QtCore.QRect(220, 180, 21, 21))
        self.pushButton_18.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.widget)
        self.pushButton_19.setGeometry(QtCore.QRect(250, 180, 21, 21))
        self.pushButton_19.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.widget)
        self.pushButton_20.setGeometry(QtCore.QRect(280, 180, 21, 21))
        self.pushButton_20.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.widget)
        self.pushButton_21.setGeometry(QtCore.QRect(310, 180, 21, 21))
        self.pushButton_21.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget)
        self.pushButton_22.setGeometry(QtCore.QRect(340, 180, 21, 21))
        self.pushButton_22.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.widget)
        self.pushButton_23.setGeometry(QtCore.QRect(370, 180, 21, 21))
        self.pushButton_23.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.widget)
        self.pushButton_24.setGeometry(QtCore.QRect(40, 210, 21, 21))
        self.pushButton_24.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.widget)
        self.pushButton_25.setGeometry(QtCore.QRect(70, 210, 21, 21))
        self.pushButton_25.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.widget)
        self.pushButton_26.setGeometry(QtCore.QRect(100, 210, 21, 21))
        self.pushButton_26.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.widget)
        self.pushButton_27.setGeometry(QtCore.QRect(130, 210, 21, 21))
        self.pushButton_27.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.widget)
        self.pushButton_28.setGeometry(QtCore.QRect(160, 210, 21, 21))
        self.pushButton_28.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.widget)
        self.pushButton_29.setGeometry(QtCore.QRect(190, 210, 21, 21))
        self.pushButton_29.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.widget)
        self.pushButton_30.setGeometry(QtCore.QRect(220, 210, 21, 21))
        self.pushButton_30.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.widget)
        self.pushButton_31.setGeometry(QtCore.QRect(250, 210, 21, 21))
        self.pushButton_31.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.widget)
        self.pushButton_32.setGeometry(QtCore.QRect(280, 210, 21, 21))
        self.pushButton_32.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.widget)
        self.pushButton_33.setGeometry(QtCore.QRect(310, 210, 21, 21))
        self.pushButton_33.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.widget)
        self.pushButton_34.setGeometry(QtCore.QRect(340, 210, 21, 21))
        self.pushButton_34.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.widget)
        self.pushButton_35.setGeometry(QtCore.QRect(370, 210, 21, 21))
        self.pushButton_35.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.widget)
        self.pushButton_36.setGeometry(QtCore.QRect(40, 240, 21, 21))
        self.pushButton_36.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.widget)
        self.pushButton_37.setGeometry(QtCore.QRect(70, 240, 21, 21))
        self.pushButton_37.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.widget)
        self.pushButton_38.setGeometry(QtCore.QRect(130, 240, 21, 21))
        self.pushButton_38.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.widget)
        self.pushButton_39.setGeometry(QtCore.QRect(160, 240, 21, 21))
        self.pushButton_39.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.widget)
        self.pushButton_40.setGeometry(QtCore.QRect(100, 240, 21, 21))
        self.pushButton_40.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.widget)
        self.pushButton_41.setGeometry(QtCore.QRect(190, 240, 21, 21))
        self.pushButton_41.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.widget)
        self.pushButton_42.setGeometry(QtCore.QRect(220, 240, 21, 21))
        self.pushButton_42.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.widget)
        self.pushButton_43.setGeometry(QtCore.QRect(250, 240, 21, 21))
        self.pushButton_43.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.widget)
        self.pushButton_44.setGeometry(QtCore.QRect(280, 240, 21, 21))
        self.pushButton_44.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.widget)
        self.pushButton_45.setGeometry(QtCore.QRect(310, 240, 21, 21))
        self.pushButton_45.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.widget)
        self.pushButton_46.setGeometry(QtCore.QRect(340, 240, 21, 21))
        self.pushButton_46.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.widget)
        self.pushButton_47.setGeometry(QtCore.QRect(370, 240, 21, 21))
        self.pushButton_47.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.widget)
        self.pushButton_48.setGeometry(QtCore.QRect(40, 270, 21, 21))
        self.pushButton_48.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.widget)
        self.pushButton_49.setGeometry(QtCore.QRect(70, 270, 21, 21))
        self.pushButton_49.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.widget)
        self.pushButton_50.setGeometry(QtCore.QRect(130, 270, 21, 21))
        self.pushButton_50.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.widget)
        self.pushButton_51.setGeometry(QtCore.QRect(100, 270, 21, 21))
        self.pushButton_51.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.widget)
        self.pushButton_52.setGeometry(QtCore.QRect(160, 270, 21, 21))
        self.pushButton_52.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.widget)
        self.pushButton_53.setGeometry(QtCore.QRect(220, 270, 21, 21))
        self.pushButton_53.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.widget)
        self.pushButton_54.setGeometry(QtCore.QRect(190, 270, 21, 21))
        self.pushButton_54.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.widget)
        self.pushButton_55.setGeometry(QtCore.QRect(250, 270, 21, 21))
        self.pushButton_55.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.widget)
        self.pushButton_56.setGeometry(QtCore.QRect(310, 270, 21, 21))
        self.pushButton_56.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.widget)
        self.pushButton_57.setGeometry(QtCore.QRect(280, 270, 21, 21))
        self.pushButton_57.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.widget)
        self.pushButton_58.setGeometry(QtCore.QRect(340, 270, 21, 21))
        self.pushButton_58.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.widget)
        self.pushButton_59.setGeometry(QtCore.QRect(370, 270, 21, 21))
        self.pushButton_59.setStyleSheet("background-color: rgb(147, 147, 147);")
        self.pushButton_59.setObjectName("pushButton_59")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 30, 271, 71))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "X"))
        self.pushButton_2.setText(_translate("Form", "1"))
        self.pushButton_3.setText(_translate("Form", "2"))
        self.pushButton_4.setText(_translate("Form", "3"))
        self.pushButton_5.setText(_translate("Form", "4"))
        self.pushButton_6.setText(_translate("Form", "5"))
        self.pushButton_7.setText(_translate("Form", "6"))
        self.pushButton_8.setText(_translate("Form", "7"))
        self.pushButton_9.setText(_translate("Form", "8"))
        self.pushButton_10.setText(_translate("Form", "9"))
        self.pushButton_11.setText(_translate("Form", "10"))
        self.pushButton_12.setText(_translate("Form", "14"))
        self.pushButton_13.setText(_translate("Form", "13"))
        self.pushButton_14.setText(_translate("Form", "12"))
        self.pushButton_15.setText(_translate("Form", "11"))
        self.pushButton_16.setText(_translate("Form", "15"))
        self.pushButton_17.setText(_translate("Form", "16"))
        self.pushButton_18.setText(_translate("Form", "17"))
        self.pushButton_19.setText(_translate("Form", "18"))
        self.pushButton_20.setText(_translate("Form", "19"))
        self.pushButton_21.setText(_translate("Form", "20"))
        self.pushButton_22.setText(_translate("Form", "21"))
        self.pushButton_23.setText(_translate("Form", "22"))
        self.pushButton_24.setText(_translate("Form", "23"))
        self.pushButton_25.setText(_translate("Form", "24"))
        self.pushButton_26.setText(_translate("Form", "25"))
        self.pushButton_27.setText(_translate("Form", "26"))
        self.pushButton_28.setText(_translate("Form", "27"))
        self.pushButton_29.setText(_translate("Form", "28"))
        self.pushButton_30.setText(_translate("Form", "29"))
        self.pushButton_31.setText(_translate("Form", "30"))
        self.pushButton_32.setText(_translate("Form", "31"))
        self.pushButton_33.setText(_translate("Form", "32"))
        self.pushButton_34.setText(_translate("Form", "33"))
        self.pushButton_35.setText(_translate("Form", "34"))
        self.pushButton_36.setText(_translate("Form", "35"))
        self.pushButton_37.setText(_translate("Form", "36"))
        self.pushButton_38.setText(_translate("Form", "38"))
        self.pushButton_39.setText(_translate("Form", "39"))
        self.pushButton_40.setText(_translate("Form", "37"))
        self.pushButton_41.setText(_translate("Form", "40"))
        self.pushButton_42.setText(_translate("Form", "41"))
        self.pushButton_43.setText(_translate("Form", "42"))
        self.pushButton_44.setText(_translate("Form", "43"))
        self.pushButton_45.setText(_translate("Form", "44"))
        self.pushButton_46.setText(_translate("Form", "45"))
        self.pushButton_47.setText(_translate("Form", "46"))
        self.pushButton_48.setText(_translate("Form", "47"))
        self.pushButton_49.setText(_translate("Form", "48"))
        self.pushButton_50.setText(_translate("Form", "50"))
        self.pushButton_51.setText(_translate("Form", "49"))
        self.pushButton_52.setText(_translate("Form", "51"))
        self.pushButton_53.setText(_translate("Form", "53"))
        self.pushButton_54.setText(_translate("Form", "52"))
        self.pushButton_55.setText(_translate("Form", "54"))
        self.pushButton_56.setText(_translate("Form", "56"))
        self.pushButton_57.setText(_translate("Form", "55"))
        self.pushButton_58.setText(_translate("Form", "57"))
        self.pushButton_59.setText(_translate("Form", "58"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Сцена</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Form
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbox2 = QtWidgets.QComboBox(self.centralwidget)
        self.cbox2.setStyleSheet("selection-background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.cbox2.setObjectName("cbox2")
        self.cbox2.addItem("")
        self.cbox2.addItem("")
        self.cbox2.addItem("")
        self.gridLayout_2.addWidget(self.cbox2, 1, 1, 1, 1)
        self.bitlbl = QtWidgets.QLabel(self.centralwidget)
        self.bitlbl.setMinimumSize(QtCore.QSize(165, 98))
        self.bitlbl.setMaximumSize(QtCore.QSize(165, 16777215))
        self.bitlbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bitlbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bitlbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bitlbl.setObjectName("bitlbl")
        self.gridLayout_2.addWidget(self.bitlbl, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.byte_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.byte_txt.setObjectName("byte_txt")
        self.gridLayout_2.addWidget(self.byte_txt, 3, 1, 1, 1)
        self.bit_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.bit_txt.setObjectName("bit_txt")
        self.gridLayout_2.addWidget(self.bit_txt, 3, 0, 1, 1)
        self.cbox1 = QtWidgets.QComboBox(self.centralwidget)
        self.cbox1.setStyleSheet("selection-background-color: rgb(0, 170, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.cbox1.setObjectName("cbox1")
        self.cbox1.addItem("")
        self.cbox1.addItem("")
        self.cbox1.addItem("")
        self.gridLayout_2.addWidget(self.cbox1, 1, 0, 1, 1)
        self.bytelbl = QtWidgets.QLabel(self.centralwidget)
        self.bytelbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bytelbl.setObjectName("bytelbl")
        self.gridLayout_2.addWidget(self.bytelbl, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.Headinglbl = QtWidgets.QLabel(self.centralwidget)
        self.Headinglbl.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Headinglbl.setObjectName("Headinglbl")
        self.gridLayout.addWidget(self.Headinglbl, 0, 0, 1, 1)
        self.calc_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calc_btn.setFont(font)
        self.calc_btn.setAcceptDrops(False)
        self.calc_btn.setAutoFillBackground(False)
        self.calc_btn.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.calc_btn.setAutoDefault(False)
        self.calc_btn.setDefault(False)
        self.calc_btn.setFlat(False)
        self.calc_btn.setObjectName("calc_btn")
        self.calc_btn.clicked.connect(self.conv)
        self.gridLayout.addWidget(self.calc_btn, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cbox2.setItemText(0, _translate("MainWindow", "KB"))
        self.cbox2.setItemText(1, _translate("MainWindow", "MB"))
        self.cbox2.setItemText(2, _translate("MainWindow", "GB"))
        self.bitlbl.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Bit</span></p></body></html>"))
        self.cbox1.setItemText(0, _translate("MainWindow", "Kb"))
        self.cbox1.setItemText(1, _translate("MainWindow", "Mb"))
        self.cbox1.setItemText(2, _translate("MainWindow", "Gb"))
        self.bytelbl.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Byte</span></p></body></html>"))
        self.Headinglbl.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Bit To Byte</span></p></body></html>"))
        self.calc_btn.setToolTip(_translate("MainWindow", "Calculate"))
        self.calc_btn.setText(_translate("MainWindow", "Convert"))

    def conv(self):
        val = self.bit_txt.text()
        uni1 = self.cbox1.currentText()
        uni2 = self.cbox2.currentText()

        if uni1 == 'Kb':
            if uni2 == 'KB':
                self.byte_txt.setText(str(int(val) / 8))
            elif uni2 == 'MB':
                self.byte_txt.setText(str(int(val) / 8000))
            elif uni2 == 'GB':
                self.byte_txt.setText(str(int(val) / 8000000))
        elif uni1 == 'Mb':
            if uni2 == 'KB':
                self.byte_txt.setText(str(int(val) * 125))
            elif uni2 == 'MB':
                self.byte_txt.setText(str(int(val) / 8))
            elif uni2 == 'GB':
                self.byte_txt.setText(str(int(val) / 8000))
        elif uni1 == 'Gb':
            if uni2 == 'KB':
                self.byte_txt.setText(str(int(val) * 125000))
            elif uni2 == 'MB':
                self.byte_txt.setText(str(int(val) * 125))
            elif uni2 == 'GB':
                self.byte_txt.setText(str(int(val) / 8))
        else:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

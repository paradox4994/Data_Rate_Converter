from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(190, 100, 271, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Headinglbl = QLabel(self.gridLayoutWidget)
        self.Headinglbl.setObjectName(u"Headinglbl")
        self.Headinglbl.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.gridLayout.addWidget(self.Headinglbl, 0, 0, 1, 1)

        self.calcbtn = QPushButton(self.gridLayoutWidget)
        self.calcbtn.setObjectName(u"calcbtn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calcbtn.setFont(font)
        self.calcbtn.setAcceptDrops(False)
        self.calcbtn.setAutoFillBackground(False)
        self.calcbtn.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.calcbtn.setAutoDefault(False)
        self.calcbtn.setFlat(False)

        self.gridLayout.addWidget(self.calcbtn, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(1)
        self.bytetxt = QLineEdit(self.gridLayoutWidget)
        self.bytetxt.setObjectName(u"bytetxt")

        self.gridLayout_2.addWidget(self.bytetxt, 1, 1, 1, 1)

        self.bittxt = QLineEdit(self.gridLayoutWidget)
        self.bittxt.setObjectName(u"bittxt")

        self.gridLayout_2.addWidget(self.bittxt, 1, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.calcbtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Headinglbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Bit To Byte</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.calcbtn.setToolTip(QCoreApplication.translate("MainWindow", u"Calculate", None))
#endif // QT_CONFIG(tooltip)
        self.calcbtn.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Bit</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#00aaff;\">Byte</span></p></body></html>", None))
    # retranslateUi

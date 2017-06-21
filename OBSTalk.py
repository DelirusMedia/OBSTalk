# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Delirus Media\Desktop\OBSTalk.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OBSTalk(object):
    def setupUi(self, OBSTalk):
        OBSTalk.setObjectName("OBSTalk")
        OBSTalk.resize(251, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OBSTalk.sizePolicy().hasHeightForWidth())
        OBSTalk.setSizePolicy(sizePolicy)
        OBSTalk.setMaximumSize(QtCore.QSize(251, 118))
        self.centralwidget = QtWidgets.QWidget(OBSTalk)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(251, 98))
        self.centralwidget.setMaximumSize(QtCore.QSize(251, 98))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(144, 70, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        OBSTalk.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OBSTalk)
        self.statusbar.setObjectName("statusbar")
        OBSTalk.setStatusBar(self.statusbar)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.retranslateUi(OBSTalk)
        QtCore.QMetaObject.connectSlotsByName(OBSTalk)

    def retranslateUi(self, OBSTalk):
        _translate = QtCore.QCoreApplication.translate
        OBSTalk.setWindowTitle(_translate("OBSTalk", "OBSTalk"))
        self.pushButton.setText(_translate("OBSTalk", "Verbinden"))
        self.pushButton_2.setText(_translate("OBSTalk", "Trennen"))
        self.label.setText(_translate("OBSTalk", "<html><head/><body><p><span style=\" color:#c10003;\">Nicht verbunden!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OBSTalk = QtWidgets.QMainWindow()
    ui = Ui_OBSTalk()
    ui.setupUi(OBSTalk)
    OBSTalk.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WeatherDialog(object):
    def setupUi(self, WeatherDialog):
        WeatherDialog.setObjectName("WeatherDialog")
        WeatherDialog.resize(682, 206)
        self.pushButton = QtWidgets.QPushButton(WeatherDialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 80, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(WeatherDialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 481, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(WeatherDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 30, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView = QtWidgets.QListView(WeatherDialog)
        self.listView.setGeometry(QtCore.QRect(40, 80, 481, 91))
        self.listView.setObjectName("listView")

        self.retranslateUi(WeatherDialog)
        self.pushButton.clicked.connect(WeatherDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WeatherDialog)

    def retranslateUi(self, WeatherDialog):
        _translate = QtCore.QCoreApplication.translate
        WeatherDialog.setWindowTitle(_translate("WeatherDialog", "Dialog"))
        self.pushButton.setText(_translate("WeatherDialog", "我知道了"))
        self.pushButton_2.setText(_translate("WeatherDialog", "查询"))

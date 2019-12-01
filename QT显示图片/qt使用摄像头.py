# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\-\QT显示图片\qt使用摄像头.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 463)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 751, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_sourceImage = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_sourceImage.setObjectName("lbl_sourceImage")
        self.horizontalLayout.addWidget(self.lbl_sourceImage)
        self.lbl_dealedImage = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dealedImage.setObjectName("lbl_dealedImage")
        self.horizontalLayout.addWidget(self.lbl_dealedImage)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(180, 390, 401, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_open = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_2.addWidget(self.btn_open)
        self.btn_close = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.btn_openGarry = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_openGarry.setObjectName("btn_openGarry")
        self.horizontalLayout_2.addWidget(self.btn_openGarry)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_sourceImage.setText(_translate("Form", ""))
        self.lbl_dealedImage.setText(_translate("Form", ""))
        self.btn_open.setText(_translate("Form", "打开摄像头"))
        self.btn_close.setText(_translate("Form", "关闭摄像头"))
        self.btn_openGarry.setText(_translate("Form", "打开灰度图"))

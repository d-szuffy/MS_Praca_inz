# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gear_v2 (1)xNHQDq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import demo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 610)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 35))
        self.frame.setMaximumSize(QSize(16777215, 35))
        self.frame.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 35))
        self.frame_7.setMaximumSize(QSize(150, 35))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1, 1, 150, 35))
        self.label.setMinimumSize(QSize(150, 35))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.main_header = QFrame(self.frame)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(0, 35))
        self.main_header.setMaximumSize(QSize(16777215, 35))
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.main_header)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(100, 35))
        self.frame_6.setMaximumSize(QSize(100, 35))
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(33, 33, 33);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(30, 136, 229);\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.frame_6)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/demo/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(24, 24))
        self.minimize_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.restore_btn = QPushButton(self.frame_6)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setMinimumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/demo/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_btn.setIcon(icon1)
        self.restore_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restore_btn)

        self.close_btn = QPushButton(self.frame_6)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/demo/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 136, 229);\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 136, 229);\n"
"border: none;\n"
"height: 40;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(24, 112, 189);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(24, 112, 189);\n"
"border-bottom: 3px solid rgb(255, 255, 255);\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.pushButton.setFont(font1)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_8)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 25))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.materialy_page = QWidget()
        self.materialy_page.setObjectName(u"materialy_page")
        self.verticalLayout_3 = QVBoxLayout(self.materialy_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.materialy_page)
        self.zalozenia_page = QWidget()
        self.zalozenia_page.setObjectName(u"zalozenia_page")
        self.stackedWidget.addWidget(self.zalozenia_page)
        self.wyniki_wstepne_page = QWidget()
        self.wyniki_wstepne_page.setObjectName(u"wyniki_wstepne_page")
        self.stackedWidget.addWidget(self.wyniki_wstepne_page)
        self.naprezenia_page = QWidget()
        self.naprezenia_page.setObjectName(u"naprezenia_page")
        self.stackedWidget.addWidget(self.naprezenia_page)
        self.srednice_page = QWidget()
        self.srednice_page.setObjectName(u"srednice_page")
        self.stackedWidget.addWidget(self.srednice_page)
        self.wyniki_page = QWidget()
        self.wyniki_page.setObjectName(u"wyniki_page")
        self.stackedWidget.addWidget(self.wyniki_page)
        self.excel_page = QWidget()
        self.excel_page.setObjectName(u"excel_page")
        self.stackedWidget.addWidget(self.excel_page)
        self.schemat_page = QWidget()
        self.schemat_page.setObjectName(u"schemat_page")
        self.stackedWidget.addWidget(self.schemat_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(16777215, 25))
        self.frame_3.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gear.py", None))
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MATERIA\u0141", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"ZA\u0141O\u017bENIA", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"WYNIKI WST\u0118PNE", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"NAPR\u0118\u017bENIA", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICE", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"WYNIKI", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"SCHEMAT", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gear_v2 (1)KcFmwM.ui'
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
        self.top_header = QFrame(self.centralwidget)
        self.top_header.setObjectName(u"top_header")
        self.top_header.setMinimumSize(QSize(0, 50))
        self.top_header.setMaximumSize(QSize(16777215, 50))
        self.top_header.setStyleSheet(u"background-color: rgb(33, 38, 55);")
        self.top_header.setFrameShape(QFrame.NoFrame)
        self.top_header.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.top_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_frame = QFrame(self.top_header)
        self.label_frame.setObjectName(u"label_frame")
        self.label_frame.setMinimumSize(QSize(0, 35))
        self.label_frame.setMaximumSize(QSize(150, 35))
        self.label_frame.setFrameShape(QFrame.StyledPanel)
        self.label_frame.setFrameShadow(QFrame.Raised)
        self.label_name = QLabel(self.label_frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(1, 1, 150, 35))
        self.label_name.setMinimumSize(QSize(150, 35))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")

        self.horizontalLayout_2.addWidget(self.label_frame)

        self.main_header = QFrame(self.top_header)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(0, 35))
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.main_header)

        self.top_right_btns = QFrame(self.top_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMinimumSize(QSize(100, 35))
        self.top_right_btns.setMaximumSize(QSize(100, 35))
        self.top_right_btns.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(33, 38, 55);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(51, 82, 148);\n"
"}")
        self.top_right_btns.setFrameShape(QFrame.NoFrame)
        self.top_right_btns.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.top_right_btns)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(35, 35))
        icon = QIcon()
        icon.addFile(u":/demo/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(24, 24))
        self.minimize_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.restore_btn = QPushButton(self.top_right_btns)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setMinimumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/demo/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_btn.setIcon(icon1)
        self.restore_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restore_btn)

        self.close_btn = QPushButton(self.top_right_btns)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/demo/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.top_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(242, 242, 246);")
        self.main_body.setFrameShape(QFrame.NoFrame)
        self.main_body.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.buttons_frame = QFrame(self.main_body)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(0, 40))
        self.buttons_frame.setMaximumSize(QSize(16777215, 40))
        self.buttons_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(242, 242, 246);\n"
"}\n"
"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 40;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(61, 101, 206);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(51, 82, 148);\n"
"border-bottom: 3px solid rgb(33, 38, 55);\n"
"}")
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.materials_btn = QPushButton(self.buttons_frame)
        self.materials_btn.setObjectName(u"materials_btn")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.materials_btn.setFont(font1)
        self.materials_btn.setCheckable(True)
        self.materials_btn.setChecked(False)
        self.materials_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.materials_btn)

        self.input_btn = QPushButton(self.buttons_frame)
        self.input_btn.setObjectName(u"input_btn")
        self.input_btn.setFont(font1)
        self.input_btn.setCheckable(True)
        self.input_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.input_btn)

        self.base_outcome_btn = QPushButton(self.buttons_frame)
        self.base_outcome_btn.setObjectName(u"base_outcome_btn")
        self.base_outcome_btn.setCheckable(True)
        self.base_outcome_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.base_outcome_btn)

        self.forces_btn = QPushButton(self.buttons_frame)
        self.forces_btn.setObjectName(u"forces_btn")
        self.forces_btn.setCheckable(True)
        self.forces_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.forces_btn)

        self.diameters_btn = QPushButton(self.buttons_frame)
        self.diameters_btn.setObjectName(u"diameters_btn")
        self.diameters_btn.setCheckable(True)
        self.diameters_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.diameters_btn)

        self.final_result_btn = QPushButton(self.buttons_frame)
        self.final_result_btn.setObjectName(u"final_result_btn")
        self.final_result_btn.setCheckable(True)
        self.final_result_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.final_result_btn)

        self.excel_btn = QPushButton(self.buttons_frame)
        self.excel_btn.setObjectName(u"excel_btn")
        self.excel_btn.setCheckable(True)
        self.excel_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.excel_btn)

        self.scheme_btn = QPushButton(self.buttons_frame)
        self.scheme_btn.setObjectName(u"scheme_btn")
        self.scheme_btn.setCheckable(True)
        self.scheme_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.scheme_btn)


        self.verticalLayout_2.addWidget(self.buttons_frame)

        self.stackedWidget = QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 25))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.materialy_page = QWidget()
        self.materialy_page.setObjectName(u"materialy_page")
        self.verticalLayout_3 = QVBoxLayout(self.materialy_page)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 0)
        self.row_frame_1 = QFrame(self.materialy_page)
        self.row_frame_1.setObjectName(u"row_frame_1")
        self.row_frame_1.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: none;\n"
"padding-left: 50px;\n"
"color: rgb(33, 38, 55);\n"
"}")
        self.row_frame_1.setFrameShape(QFrame.NoFrame)
        self.row_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.row_frame_1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.row_frame_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 25))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 98, 30))
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(250, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Symbol")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setTextFormat(Qt.PlainText)

        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 25))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(60, -1, -1, -1)
        self.comboBox = QComboBox(self.frame_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.comboBox.setFont(font3)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(76, 118, 232);\n"
"border-left: 1px solid rgb(242, 242, 246);\n"
"width:50px\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"width: 40px;\n"
"height: 40px;\n"
"}\n"
"QComboBox::drop-down::hover{\n"
"	background-color: rgb(61, 101, 206);\n"
"}\n"
"QComboBox QListView::item {\n"
"   background: qradialgradient(\n"
"   cx: 0.5, cy: -1.6, fx: 0.5, fy: 0,\n"
"   radius: 2,\n"
"   stop: 0 #C4C4C4,\n"
"   stop: 1 #DBDBDB );\n"
"   border-style: solid;\n"
"   border-width: 1px;\n"
"   border-color: rgb(0, 93, 168);\n"
"   border-radius: 20px;\n"
"}")
        self.comboBox.setPlaceholderText(u"WYBIERZ MATERIA\u0141")
        self.comboBox.setFrame(True)

        self.verticalLayout_8.addWidget(self.comboBox)


        self.horizontalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.row_frame_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(70, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_2.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.row_frame_1)

        self.row_frame_2 = QFrame(self.materialy_page)
        self.row_frame_2.setObjectName(u"row_frame_2")
        self.row_frame_2.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: none;\n"
"padding-left: 50px;\n"
"color: rgb(33, 38, 55);\n"
"}")
        self.row_frame_2.setFrameShape(QFrame.NoFrame)
        self.row_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.row_frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.row_frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(250, 30))
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.PlainText)

        self.verticalLayout_7.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.row_frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(70, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_5.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.frame_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 40))
        self.lineEdit_6.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_6.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout_7.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.row_frame_2)

        self.frame_3 = QFrame(self.materialy_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 40;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame_3)

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


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"GEAR.py", None))
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.materials_btn.setText(QCoreApplication.translate("MainWindow", u"MATERIA\u0141", None))
        self.input_btn.setText(QCoreApplication.translate("MainWindow", u"ZA\u0141O\u017bENIA", None))
        self.base_outcome_btn.setText(QCoreApplication.translate("MainWindow", u"WYNIKI WST\u0118PNE", None))
        self.forces_btn.setText(QCoreApplication.translate("MainWindow", u"NAPR\u0118\u017bENIA", None))
        self.diameters_btn.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICE", None))
        self.final_result_btn.setText(QCoreApplication.translate("MainWindow", u"WYNIKI", None))
        self.excel_btn.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.scheme_btn.setText(QCoreApplication.translate("MainWindow", u"SCHEMAT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WIERSZ DRUGI", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"asdf", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"xzxcv", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"asbabfba", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Nowy element", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"a", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"ba", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"b", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"ab", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"a", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"bab", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Nowy element", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"f", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"av", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"f", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"av", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"f", None))

        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TRZECIA DANA", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DRUGA DANA", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PIERWSZA DANA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WIERSZ DRUGI", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TRZECIA DANA", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DRUGA DANA", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PIERWSZA DANA", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"AKCEPTUJ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"WYCZY\u015a\u0106", None))
    # retranslateUi


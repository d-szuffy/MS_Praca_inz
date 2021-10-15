# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gear_v3VQKABw.ui'
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
        MainWindow.resize(922, 667)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_header = QFrame(self.centralwidget)
        self.top_header.setObjectName(u"top_header")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_header.sizePolicy().hasHeightForWidth())
        self.top_header.setSizePolicy(sizePolicy)
        self.top_header.setMinimumSize(QSize(0, 50))
        self.top_header.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        self.top_header.setFont(font)
        self.top_header.setStyleSheet(u"background-color: rgb(33, 38, 55);")
        self.top_header.setFrameShape(QFrame.NoFrame)
        self.top_header.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.top_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.top_header)
        self.main_header.setObjectName(u"main_header")
        sizePolicy.setHeightForWidth(self.main_header.sizePolicy().hasHeightForWidth())
        self.main_header.setSizePolicy(sizePolicy)
        self.main_header.setMinimumSize(QSize(0, 35))
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setFont(font)
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.main_header)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.main_header)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 10px;")

        self.horizontalLayout_7.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.main_header)

        self.top_right_btns = QFrame(self.top_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        sizePolicy.setHeightForWidth(self.top_right_btns.sizePolicy().hasHeightForWidth())
        self.top_right_btns.setSizePolicy(sizePolicy)
        self.top_right_btns.setMinimumSize(QSize(100, 35))
        self.top_right_btns.setMaximumSize(QSize(100, 35))
        self.top_right_btns.setFont(font)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy1)
        self.minimize_btn.setMinimumSize(QSize(35, 35))
        self.minimize_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/demo/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(24, 24))
        self.minimize_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.restore_btn = QPushButton(self.top_right_btns)
        self.restore_btn.setObjectName(u"restore_btn")
        sizePolicy1.setHeightForWidth(self.restore_btn.sizePolicy().hasHeightForWidth())
        self.restore_btn.setSizePolicy(sizePolicy1)
        self.restore_btn.setMinimumSize(QSize(35, 35))
        self.restore_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/demo/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_btn.setIcon(icon1)
        self.restore_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restore_btn)

        self.close_btn = QPushButton(self.top_right_btns)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setMinimumSize(QSize(35, 35))
        self.close_btn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/demo/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.top_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFont(font)
        self.main_body.setStyleSheet(u"background-color: rgb(242, 242, 246);")
        self.main_body.setFrameShape(QFrame.NoFrame)
        self.main_body.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.buttons_frame = QFrame(self.main_body)
        self.buttons_frame.setObjectName(u"buttons_frame")
        sizePolicy.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy)
        self.buttons_frame.setMinimumSize(QSize(0, 40))
        self.buttons_frame.setMaximumSize(QSize(16777215, 40))
        self.buttons_frame.setFont(font)
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
"}")
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.materials_btn = QPushButton(self.buttons_frame)
        self.materials_btn.setObjectName(u"materials_btn")
        sizePolicy1.setHeightForWidth(self.materials_btn.sizePolicy().hasHeightForWidth())
        self.materials_btn.setSizePolicy(sizePolicy1)
        self.materials_btn.setFont(font)
        self.materials_btn.setStyleSheet(u"background-color: rgb(51, 82, 148);\n"
"border-bottom: 3px solid rgb(33, 38, 55);\n"
"height: 40;")
        self.materials_btn.setCheckable(True)
        self.materials_btn.setChecked(False)
        self.materials_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.materials_btn)

        self.input_btn = QPushButton(self.buttons_frame)
        self.input_btn.setObjectName(u"input_btn")
        sizePolicy1.setHeightForWidth(self.input_btn.sizePolicy().hasHeightForWidth())
        self.input_btn.setSizePolicy(sizePolicy1)
        self.input_btn.setFont(font)
        self.input_btn.setCheckable(True)
        self.input_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.input_btn)

        self.base_outcome_btn = QPushButton(self.buttons_frame)
        self.base_outcome_btn.setObjectName(u"base_outcome_btn")
        self.base_outcome_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.base_outcome_btn.sizePolicy().hasHeightForWidth())
        self.base_outcome_btn.setSizePolicy(sizePolicy1)
        self.base_outcome_btn.setFont(font)
        self.base_outcome_btn.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.base_outcome_btn.setCheckable(True)
        self.base_outcome_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.base_outcome_btn)

        self.forces_btn = QPushButton(self.buttons_frame)
        self.forces_btn.setObjectName(u"forces_btn")
        self.forces_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.forces_btn.sizePolicy().hasHeightForWidth())
        self.forces_btn.setSizePolicy(sizePolicy1)
        self.forces_btn.setFont(font)
        self.forces_btn.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.forces_btn.setCheckable(True)
        self.forces_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.forces_btn)

        self.diameters_btn = QPushButton(self.buttons_frame)
        self.diameters_btn.setObjectName(u"diameters_btn")
        self.diameters_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.diameters_btn.sizePolicy().hasHeightForWidth())
        self.diameters_btn.setSizePolicy(sizePolicy1)
        self.diameters_btn.setFont(font)
        self.diameters_btn.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.diameters_btn.setCheckable(True)
        self.diameters_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.diameters_btn)

        self.excel_btn = QPushButton(self.buttons_frame)
        self.excel_btn.setObjectName(u"excel_btn")
        self.excel_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.excel_btn.sizePolicy().hasHeightForWidth())
        self.excel_btn.setSizePolicy(sizePolicy1)
        self.excel_btn.setFont(font)
        self.excel_btn.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.excel_btn.setCheckable(True)
        self.excel_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.excel_btn)

        self.scheme_btn = QPushButton(self.buttons_frame)
        self.scheme_btn.setObjectName(u"scheme_btn")
        self.scheme_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.scheme_btn.sizePolicy().hasHeightForWidth())
        self.scheme_btn.setSizePolicy(sizePolicy1)
        self.scheme_btn.setFont(font)
        self.scheme_btn.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.scheme_btn.setCheckable(True)
        self.scheme_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.scheme_btn)


        self.verticalLayout_2.addWidget(self.buttons_frame)

        self.stackedWidget = QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 25))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_input_data = QWidget()
        self.page_input_data.setObjectName(u"page_input_data")
        self.verticalLayout_3 = QVBoxLayout(self.page_input_data)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 0)
        self.row_frame_1 = QFrame(self.page_input_data)
        self.row_frame_1.setObjectName(u"row_frame_1")
        sizePolicy.setHeightForWidth(self.row_frame_1.sizePolicy().hasHeightForWidth())
        self.row_frame_1.setSizePolicy(sizePolicy)
        self.row_frame_1.setFont(font)
        self.row_frame_1.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: none;\n"
"padding-left: 3px;\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"\n"
"QComboBox{\n"
"padding-left: 3px;\n"
"margin-left: 10px;\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"padding: 1px 1px 1px 1px;\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(76, 118, 232);\n"
"border-left: 1px solid rgb(242, 242, 246);\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::drop-down::hover{\n"
"	background-color: rgb(61, 101, 206);\n"
"}\n"
"QListView::item {\n"
"   background: qradialgradient(\n"
"   cx: 0.5, cy: -1.6, fx: 0.5, fy: 0,\n"
"   radius: 2,\n"
"   stop: 0 #C4C4C4,\n"
"   stop: 1 #DBDBDB );\n"
"   border-style: solid;\n"
"   border-width: 1px;\n"
"   border-color: rgb(0, 93, 168);\n"
"   border"
                        "-radius: 20px;\n"
"}")
        self.row_frame_1.setFrameShape(QFrame.NoFrame)
        self.row_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.row_frame_1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_input_label = QFrame(self.row_frame_1)
        self.frame_input_label.setObjectName(u"frame_input_label")
        sizePolicy.setHeightForWidth(self.frame_input_label.sizePolicy().hasHeightForWidth())
        self.frame_input_label.setSizePolicy(sizePolicy)
        self.frame_input_label.setMaximumSize(QSize(16777215, 50))
        self.frame_input_label.setFont(font)
        self.frame_input_label.setFrameShape(QFrame.NoFrame)
        self.frame_input_label.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_input_label)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_input_data = QLabel(self.frame_input_label)
        self.label_input_data.setObjectName(u"label_input_data")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_input_data.sizePolicy().hasHeightForWidth())
        self.label_input_data.setSizePolicy(sizePolicy2)
        self.label_input_data.setMinimumSize(QSize(165, 30))
        self.label_input_data.setMaximumSize(QSize(165, 30))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_input_data.setFont(font1)
        self.label_input_data.setTextFormat(Qt.PlainText)

        self.horizontalLayout_6.addWidget(self.label_input_data)


        self.verticalLayout_4.addWidget(self.frame_input_label)

        self.frame_input_data = QFrame(self.row_frame_1)
        self.frame_input_data.setObjectName(u"frame_input_data")
        sizePolicy.setHeightForWidth(self.frame_input_data.sizePolicy().hasHeightForWidth())
        self.frame_input_data.setSizePolicy(sizePolicy)
        self.frame_input_data.setFont(font)
        self.frame_input_data.setFrameShape(QFrame.NoFrame)
        self.frame_input_data.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_input_data)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.frame_power = QFrame(self.frame_input_data)
        self.frame_power.setObjectName(u"frame_power")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_power.sizePolicy().hasHeightForWidth())
        self.frame_power.setSizePolicy(sizePolicy3)
        self.frame_power.setMinimumSize(QSize(0, 42))
        self.frame_power.setMaximumSize(QSize(16777215, 42))
        self.frame_power.setStyleSheet(u"")
        self.frame_power.setFrameShape(QFrame.StyledPanel)
        self.frame_power.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_power)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_power = QLabel(self.frame_power)
        self.label_power.setObjectName(u"label_power")
        sizePolicy2.setHeightForWidth(self.label_power.sizePolicy().hasHeightForWidth())
        self.label_power.setSizePolicy(sizePolicy2)
        self.label_power.setMinimumSize(QSize(370, 0))
        self.label_power.setMaximumSize(QSize(370, 16777215))
        self.label_power.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_power)

        self.lineEdit_power = QLineEdit(self.frame_power)
        self.lineEdit_power.setObjectName(u"lineEdit_power")
        sizePolicy1.setHeightForWidth(self.lineEdit_power.sizePolicy().hasHeightForWidth())
        self.lineEdit_power.setSizePolicy(sizePolicy1)
        self.lineEdit_power.setMinimumSize(QSize(0, 40))
        self.lineEdit_power.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_power.setFont(font)
        self.lineEdit_power.setStyleSheet(u"margin: 10px;")
        self.lineEdit_power.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_power.setDragEnabled(False)
        self.lineEdit_power.setClearButtonEnabled(True)

        self.horizontalLayout_21.addWidget(self.lineEdit_power)

        self.comboBox_power = QComboBox(self.frame_power)
        self.comboBox_power.addItem("")
        self.comboBox_power.addItem("")
        self.comboBox_power.addItem("")
        self.comboBox_power.setObjectName(u"comboBox_power")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_power.sizePolicy().hasHeightForWidth())
        self.comboBox_power.setSizePolicy(sizePolicy4)
        self.comboBox_power.setMinimumSize(QSize(100, 0))
        self.comboBox_power.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.comboBox_power.setFont(font2)
        self.comboBox_power.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"padding: 1px 1px 1px 1px;\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(76, 118, 232);\n"
"border-left: 1px solid rgb(242, 242, 246);\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::drop-down::hover{\n"
"	background-color: rgb(61, 101, 206);\n"
"}\n"
"QListView::item {\n"
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

        self.horizontalLayout_21.addWidget(self.comboBox_power)


        self.verticalLayout_5.addWidget(self.frame_power)

        self.frame_ratio = QFrame(self.frame_input_data)
        self.frame_ratio.setObjectName(u"frame_ratio")
        sizePolicy3.setHeightForWidth(self.frame_ratio.sizePolicy().hasHeightForWidth())
        self.frame_ratio.setSizePolicy(sizePolicy3)
        self.frame_ratio.setMaximumSize(QSize(16777215, 42))
        self.frame_ratio.setStyleSheet(u"")
        self.frame_ratio.setFrameShape(QFrame.StyledPanel)
        self.frame_ratio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_ratio)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_ratio = QLabel(self.frame_ratio)
        self.label_ratio.setObjectName(u"label_ratio")
        sizePolicy2.setHeightForWidth(self.label_ratio.sizePolicy().hasHeightForWidth())
        self.label_ratio.setSizePolicy(sizePolicy2)
        self.label_ratio.setMinimumSize(QSize(370, 0))
        self.label_ratio.setMaximumSize(QSize(370, 16777215))
        self.label_ratio.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_ratio)

        self.lineEdit_ratio = QLineEdit(self.frame_ratio)
        self.lineEdit_ratio.setObjectName(u"lineEdit_ratio")
        sizePolicy1.setHeightForWidth(self.lineEdit_ratio.sizePolicy().hasHeightForWidth())
        self.lineEdit_ratio.setSizePolicy(sizePolicy1)
        self.lineEdit_ratio.setMinimumSize(QSize(0, 40))
        self.lineEdit_ratio.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_ratio.setFont(font)
        self.lineEdit_ratio.setStyleSheet(u"margin: 10px;")
        self.lineEdit_ratio.setDragEnabled(False)
        self.lineEdit_ratio.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_ratio)


        self.verticalLayout_5.addWidget(self.frame_ratio)

        self.frame_velocity_in = QFrame(self.frame_input_data)
        self.frame_velocity_in.setObjectName(u"frame_velocity_in")
        sizePolicy3.setHeightForWidth(self.frame_velocity_in.sizePolicy().hasHeightForWidth())
        self.frame_velocity_in.setSizePolicy(sizePolicy3)
        self.frame_velocity_in.setStyleSheet(u"")
        self.frame_velocity_in.setFrameShape(QFrame.StyledPanel)
        self.frame_velocity_in.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_velocity_in)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_velocity_in = QLabel(self.frame_velocity_in)
        self.label_velocity_in.setObjectName(u"label_velocity_in")
        sizePolicy2.setHeightForWidth(self.label_velocity_in.sizePolicy().hasHeightForWidth())
        self.label_velocity_in.setSizePolicy(sizePolicy2)
        self.label_velocity_in.setMinimumSize(QSize(370, 0))
        self.label_velocity_in.setMaximumSize(QSize(370, 16777215))
        self.label_velocity_in.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_velocity_in)

        self.lineEdit_velocity_in = QLineEdit(self.frame_velocity_in)
        self.lineEdit_velocity_in.setObjectName(u"lineEdit_velocity_in")
        sizePolicy1.setHeightForWidth(self.lineEdit_velocity_in.sizePolicy().hasHeightForWidth())
        self.lineEdit_velocity_in.setSizePolicy(sizePolicy1)
        self.lineEdit_velocity_in.setMinimumSize(QSize(0, 40))
        self.lineEdit_velocity_in.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_velocity_in.setFont(font)
        self.lineEdit_velocity_in.setStyleSheet(u"margin: 10px;")
        self.lineEdit_velocity_in.setDragEnabled(False)
        self.lineEdit_velocity_in.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_velocity_in)

        self.comboBox_velocity_in = QComboBox(self.frame_velocity_in)
        self.comboBox_velocity_in.addItem("")
        self.comboBox_velocity_in.addItem("")
        self.comboBox_velocity_in.setObjectName(u"comboBox_velocity_in")
        sizePolicy4.setHeightForWidth(self.comboBox_velocity_in.sizePolicy().hasHeightForWidth())
        self.comboBox_velocity_in.setSizePolicy(sizePolicy4)
        self.comboBox_velocity_in.setMinimumSize(QSize(100, 0))
        self.comboBox_velocity_in.setMaximumSize(QSize(93, 16777215))
        self.comboBox_velocity_in.setFont(font2)

        self.horizontalLayout_17.addWidget(self.comboBox_velocity_in)


        self.verticalLayout_5.addWidget(self.frame_velocity_in)

        self.frame_velocity_out = QFrame(self.frame_input_data)
        self.frame_velocity_out.setObjectName(u"frame_velocity_out")
        sizePolicy3.setHeightForWidth(self.frame_velocity_out.sizePolicy().hasHeightForWidth())
        self.frame_velocity_out.setSizePolicy(sizePolicy3)
        self.frame_velocity_out.setStyleSheet(u"")
        self.frame_velocity_out.setFrameShape(QFrame.StyledPanel)
        self.frame_velocity_out.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_velocity_out)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_velocity_out = QLabel(self.frame_velocity_out)
        self.label_velocity_out.setObjectName(u"label_velocity_out")
        sizePolicy2.setHeightForWidth(self.label_velocity_out.sizePolicy().hasHeightForWidth())
        self.label_velocity_out.setSizePolicy(sizePolicy2)
        self.label_velocity_out.setMinimumSize(QSize(370, 0))
        self.label_velocity_out.setMaximumSize(QSize(370, 16777215))
        self.label_velocity_out.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_velocity_out)

        self.lineEdit_velocity_out = QLineEdit(self.frame_velocity_out)
        self.lineEdit_velocity_out.setObjectName(u"lineEdit_velocity_out")
        sizePolicy1.setHeightForWidth(self.lineEdit_velocity_out.sizePolicy().hasHeightForWidth())
        self.lineEdit_velocity_out.setSizePolicy(sizePolicy1)
        self.lineEdit_velocity_out.setMinimumSize(QSize(0, 40))
        self.lineEdit_velocity_out.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_velocity_out.setFont(font)
        self.lineEdit_velocity_out.setStyleSheet(u"margin: 10px;")
        self.lineEdit_velocity_out.setDragEnabled(False)
        self.lineEdit_velocity_out.setClearButtonEnabled(True)

        self.horizontalLayout_22.addWidget(self.lineEdit_velocity_out)

        self.comboBox_velocity_out = QComboBox(self.frame_velocity_out)
        self.comboBox_velocity_out.addItem("")
        self.comboBox_velocity_out.addItem("")
        self.comboBox_velocity_out.setObjectName(u"comboBox_velocity_out")
        sizePolicy4.setHeightForWidth(self.comboBox_velocity_out.sizePolicy().hasHeightForWidth())
        self.comboBox_velocity_out.setSizePolicy(sizePolicy4)
        self.comboBox_velocity_out.setMinimumSize(QSize(100, 0))
        self.comboBox_velocity_out.setMaximumSize(QSize(93, 16777215))
        self.comboBox_velocity_out.setFont(font2)

        self.horizontalLayout_22.addWidget(self.comboBox_velocity_out)


        self.verticalLayout_5.addWidget(self.frame_velocity_out)

        self.frame_driving_machine = QFrame(self.frame_input_data)
        self.frame_driving_machine.setObjectName(u"frame_driving_machine")
        sizePolicy3.setHeightForWidth(self.frame_driving_machine.sizePolicy().hasHeightForWidth())
        self.frame_driving_machine.setSizePolicy(sizePolicy3)
        self.frame_driving_machine.setStyleSheet(u"")
        self.frame_driving_machine.setFrameShape(QFrame.StyledPanel)
        self.frame_driving_machine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_driving_machine)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_driving_machine = QLabel(self.frame_driving_machine)
        self.label_driving_machine.setObjectName(u"label_driving_machine")
        sizePolicy2.setHeightForWidth(self.label_driving_machine.sizePolicy().hasHeightForWidth())
        self.label_driving_machine.setSizePolicy(sizePolicy2)
        self.label_driving_machine.setMinimumSize(QSize(370, 40))
        self.label_driving_machine.setMaximumSize(QSize(370, 16777215))
        self.label_driving_machine.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_driving_machine)

        self.comboBox_driving_machine = QComboBox(self.frame_driving_machine)
        self.comboBox_driving_machine.addItem("")
        self.comboBox_driving_machine.addItem("")
        self.comboBox_driving_machine.addItem("")
        self.comboBox_driving_machine.addItem("")
        self.comboBox_driving_machine.addItem("")
        self.comboBox_driving_machine.addItem("")
        self.comboBox_driving_machine.setObjectName(u"comboBox_driving_machine")
        sizePolicy1.setHeightForWidth(self.comboBox_driving_machine.sizePolicy().hasHeightForWidth())
        self.comboBox_driving_machine.setSizePolicy(sizePolicy1)
        self.comboBox_driving_machine.setFont(font2)
        self.comboBox_driving_machine.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.comboBox_driving_machine)


        self.verticalLayout_5.addWidget(self.frame_driving_machine)

        self.frame_driven_machine = QFrame(self.frame_input_data)
        self.frame_driven_machine.setObjectName(u"frame_driven_machine")
        sizePolicy3.setHeightForWidth(self.frame_driven_machine.sizePolicy().hasHeightForWidth())
        self.frame_driven_machine.setSizePolicy(sizePolicy3)
        self.frame_driven_machine.setStyleSheet(u"")
        self.frame_driven_machine.setFrameShape(QFrame.StyledPanel)
        self.frame_driven_machine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_driven_machine)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_driven_machine = QLabel(self.frame_driven_machine)
        self.label_driven_machine.setObjectName(u"label_driven_machine")
        sizePolicy2.setHeightForWidth(self.label_driven_machine.sizePolicy().hasHeightForWidth())
        self.label_driven_machine.setSizePolicy(sizePolicy2)
        self.label_driven_machine.setMinimumSize(QSize(370, 40))
        self.label_driven_machine.setMaximumSize(QSize(370, 16777215))
        self.label_driven_machine.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_driven_machine)

        self.comboBox_driven_machine = QComboBox(self.frame_driven_machine)
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.addItem("")
        self.comboBox_driven_machine.setObjectName(u"comboBox_driven_machine")
        sizePolicy1.setHeightForWidth(self.comboBox_driven_machine.sizePolicy().hasHeightForWidth())
        self.comboBox_driven_machine.setSizePolicy(sizePolicy1)
        self.comboBox_driven_machine.setFont(font2)
        self.comboBox_driven_machine.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.comboBox_driven_machine)


        self.verticalLayout_5.addWidget(self.frame_driven_machine)

        self.frame_durability = QFrame(self.frame_input_data)
        self.frame_durability.setObjectName(u"frame_durability")
        sizePolicy3.setHeightForWidth(self.frame_durability.sizePolicy().hasHeightForWidth())
        self.frame_durability.setSizePolicy(sizePolicy3)
        self.frame_durability.setStyleSheet(u"")
        self.frame_durability.setFrameShape(QFrame.StyledPanel)
        self.frame_durability.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_durability)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_durability = QLabel(self.frame_durability)
        self.label_durability.setObjectName(u"label_durability")
        sizePolicy2.setHeightForWidth(self.label_durability.sizePolicy().hasHeightForWidth())
        self.label_durability.setSizePolicy(sizePolicy2)
        self.label_durability.setMinimumSize(QSize(370, 0))
        self.label_durability.setMaximumSize(QSize(370, 16777215))
        self.label_durability.setFont(font)

        self.horizontalLayout_25.addWidget(self.label_durability)

        self.lineEdit_durability = QLineEdit(self.frame_durability)
        self.lineEdit_durability.setObjectName(u"lineEdit_durability")
        sizePolicy1.setHeightForWidth(self.lineEdit_durability.sizePolicy().hasHeightForWidth())
        self.lineEdit_durability.setSizePolicy(sizePolicy1)
        self.lineEdit_durability.setMinimumSize(QSize(0, 40))
        self.lineEdit_durability.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_durability.setFont(font)
        self.lineEdit_durability.setStyleSheet(u"margin: 10px;")
        self.lineEdit_durability.setDragEnabled(False)
        self.lineEdit_durability.setClearButtonEnabled(True)

        self.horizontalLayout_25.addWidget(self.lineEdit_durability)

        self.comboBox_durability = QComboBox(self.frame_durability)
        self.comboBox_durability.addItem("")
        self.comboBox_durability.addItem("")
        self.comboBox_durability.addItem("")
        self.comboBox_durability.setObjectName(u"comboBox_durability")
        sizePolicy4.setHeightForWidth(self.comboBox_durability.sizePolicy().hasHeightForWidth())
        self.comboBox_durability.setSizePolicy(sizePolicy4)
        self.comboBox_durability.setMinimumSize(QSize(100, 0))
        self.comboBox_durability.setMaximumSize(QSize(100, 16777215))
        self.comboBox_durability.setFont(font2)

        self.horizontalLayout_25.addWidget(self.comboBox_durability)


        self.verticalLayout_5.addWidget(self.frame_durability)

        self.frame_wheelbase = QFrame(self.frame_input_data)
        self.frame_wheelbase.setObjectName(u"frame_wheelbase")
        sizePolicy3.setHeightForWidth(self.frame_wheelbase.sizePolicy().hasHeightForWidth())
        self.frame_wheelbase.setSizePolicy(sizePolicy3)
        self.frame_wheelbase.setStyleSheet(u"")
        self.frame_wheelbase.setFrameShape(QFrame.StyledPanel)
        self.frame_wheelbase.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_wheelbase)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_wheelbase = QLabel(self.frame_wheelbase)
        self.label_wheelbase.setObjectName(u"label_wheelbase")
        sizePolicy2.setHeightForWidth(self.label_wheelbase.sizePolicy().hasHeightForWidth())
        self.label_wheelbase.setSizePolicy(sizePolicy2)
        self.label_wheelbase.setMinimumSize(QSize(370, 0))
        self.label_wheelbase.setMaximumSize(QSize(370, 16777215))
        self.label_wheelbase.setFont(font)

        self.horizontalLayout_27.addWidget(self.label_wheelbase)

        self.lineEdit_wheelbase = QLineEdit(self.frame_wheelbase)
        self.lineEdit_wheelbase.setObjectName(u"lineEdit_wheelbase")
        sizePolicy1.setHeightForWidth(self.lineEdit_wheelbase.sizePolicy().hasHeightForWidth())
        self.lineEdit_wheelbase.setSizePolicy(sizePolicy1)
        self.lineEdit_wheelbase.setMinimumSize(QSize(0, 40))
        self.lineEdit_wheelbase.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_wheelbase.setFont(font)
        self.lineEdit_wheelbase.setStyleSheet(u"margin: 10px;")
        self.lineEdit_wheelbase.setDragEnabled(False)
        self.lineEdit_wheelbase.setClearButtonEnabled(True)

        self.horizontalLayout_27.addWidget(self.lineEdit_wheelbase)

        self.comboBox_wheelbase = QComboBox(self.frame_wheelbase)
        self.comboBox_wheelbase.addItem("")
        self.comboBox_wheelbase.addItem("")
        self.comboBox_wheelbase.addItem("")
        self.comboBox_wheelbase.setObjectName(u"comboBox_wheelbase")
        sizePolicy4.setHeightForWidth(self.comboBox_wheelbase.sizePolicy().hasHeightForWidth())
        self.comboBox_wheelbase.setSizePolicy(sizePolicy4)
        self.comboBox_wheelbase.setMinimumSize(QSize(100, 0))
        self.comboBox_wheelbase.setMaximumSize(QSize(100, 16777215))
        self.comboBox_wheelbase.setFont(font2)

        self.horizontalLayout_27.addWidget(self.comboBox_wheelbase)


        self.verticalLayout_5.addWidget(self.frame_wheelbase)


        self.verticalLayout_4.addWidget(self.frame_input_data)


        self.verticalLayout_3.addWidget(self.row_frame_1)

        self.bottom_frame = QFrame(self.page_input_data)
        self.bottom_frame.setObjectName(u"bottom_frame")
        sizePolicy.setHeightForWidth(self.bottom_frame.sizePolicy().hasHeightForWidth())
        self.bottom_frame.setSizePolicy(sizePolicy)
        self.bottom_frame.setMaximumSize(QSize(16777215, 50))
        self.bottom_frame.setFont(font)
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.buttons_empty_frame = QFrame(self.bottom_frame)
        self.buttons_empty_frame.setObjectName(u"buttons_empty_frame")
        sizePolicy.setHeightForWidth(self.buttons_empty_frame.sizePolicy().hasHeightForWidth())
        self.buttons_empty_frame.setSizePolicy(sizePolicy)
        self.buttons_empty_frame.setFont(font)
        self.buttons_empty_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_empty_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.buttons_empty_frame)

        self.buttons_frame_input = QFrame(self.bottom_frame)
        self.buttons_frame_input.setObjectName(u"buttons_frame_input")
        sizePolicy.setHeightForWidth(self.buttons_frame_input.sizePolicy().hasHeightForWidth())
        self.buttons_frame_input.setSizePolicy(sizePolicy)
        self.buttons_frame_input.setFont(font)
        self.buttons_frame_input.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 40;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")
        self.buttons_frame_input.setFrameShape(QFrame.NoFrame)
        self.buttons_frame_input.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.buttons_frame_input)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.calculate_btn = QPushButton(self.buttons_frame_input)
        self.calculate_btn.setObjectName(u"calculate_btn")
        sizePolicy1.setHeightForWidth(self.calculate_btn.sizePolicy().hasHeightForWidth())
        self.calculate_btn.setSizePolicy(sizePolicy1)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setCheckable(False)
        self.calculate_btn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.calculate_btn)

        self.clear_btn = QPushButton(self.buttons_frame_input)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy1.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy1)
        self.clear_btn.setFont(font)

        self.horizontalLayout_5.addWidget(self.clear_btn)


        self.horizontalLayout_4.addWidget(self.buttons_frame_input)


        self.verticalLayout_3.addWidget(self.bottom_frame)

        self.stackedWidget.addWidget(self.page_input_data)
        self.zalozenia_page = QWidget()
        self.zalozenia_page.setObjectName(u"zalozenia_page")
        self.verticalLayout_8 = QVBoxLayout(self.zalozenia_page)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 0)
        self.row_frame_2 = QFrame(self.zalozenia_page)
        self.row_frame_2.setObjectName(u"row_frame_2")
        sizePolicy.setHeightForWidth(self.row_frame_2.sizePolicy().hasHeightForWidth())
        self.row_frame_2.setSizePolicy(sizePolicy)
        self.row_frame_2.setFont(font)
        self.row_frame_2.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: none;\n"
"padding-left: 3px;\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"\n"
"QComboBox{\n"
"padding-left: 3px;\n"
"margin-left: 10px;\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"padding: 1px 1px 1px 1px;\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(76, 118, 232);\n"
"border-left: 1px solid rgb(242, 242, 246);\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::drop-down::hover{\n"
"	background-color: rgb(61, 101, 206);\n"
"}\n"
"QListView::item {\n"
"   background: qradialgradient(\n"
"   cx: 0.5, cy: -1.6, fx: 0.5, fy: 0,\n"
"   radius: 2,\n"
"   stop: 0 #C4C4C4,\n"
"   stop: 1 #DBDBDB );\n"
"   border-style: solid;\n"
"   border-width: 1px;\n"
"   border-color: rgb(0, 93, 168);\n"
"   border"
                        "-radius: 20px;\n"
"}")
        self.row_frame_2.setFrameShape(QFrame.NoFrame)
        self.row_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.row_frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_preconditions = QFrame(self.row_frame_2)
        self.frame_preconditions.setObjectName(u"frame_preconditions")
        sizePolicy.setHeightForWidth(self.frame_preconditions.sizePolicy().hasHeightForWidth())
        self.frame_preconditions.setSizePolicy(sizePolicy)
        self.frame_preconditions.setMaximumSize(QSize(16777215, 50))
        self.frame_preconditions.setFont(font)
        self.frame_preconditions.setFrameShape(QFrame.NoFrame)
        self.frame_preconditions.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_preconditions)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_preconditions = QLabel(self.frame_preconditions)
        self.label_preconditions.setObjectName(u"label_preconditions")
        sizePolicy2.setHeightForWidth(self.label_preconditions.sizePolicy().hasHeightForWidth())
        self.label_preconditions.setSizePolicy(sizePolicy2)
        self.label_preconditions.setMinimumSize(QSize(100, 30))
        self.label_preconditions.setMaximumSize(QSize(100, 30))
        self.label_preconditions.setFont(font1)
        self.label_preconditions.setTextFormat(Qt.PlainText)

        self.horizontalLayout_8.addWidget(self.label_preconditions, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_preconditions)

        self.frame_input_data_2 = QFrame(self.row_frame_2)
        self.frame_input_data_2.setObjectName(u"frame_input_data_2")
        sizePolicy.setHeightForWidth(self.frame_input_data_2.sizePolicy().hasHeightForWidth())
        self.frame_input_data_2.setSizePolicy(sizePolicy)
        self.frame_input_data_2.setFont(font)
        self.frame_input_data_2.setFrameShape(QFrame.NoFrame)
        self.frame_input_data_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame_input_data_2)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.frame_radio_buttons = QFrame(self.frame_input_data_2)
        self.frame_radio_buttons.setObjectName(u"frame_radio_buttons")
        sizePolicy3.setHeightForWidth(self.frame_radio_buttons.sizePolicy().hasHeightForWidth())
        self.frame_radio_buttons.setSizePolicy(sizePolicy3)
        self.frame_radio_buttons.setMinimumSize(QSize(0, 42))
        self.frame_radio_buttons.setMaximumSize(QSize(16777215, 42))
        self.frame_radio_buttons.setStyleSheet(u"")
        self.frame_radio_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_radio_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_radio_buttons)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.radio_btn_soft_wheels = QRadioButton(self.frame_radio_buttons)
        self.radio_btn_soft_wheels.setObjectName(u"radio_btn_soft_wheels")
        self.radio_btn_soft_wheels.setEnabled(True)
        self.radio_btn_soft_wheels.setFont(font)
        self.radio_btn_soft_wheels.setChecked(True)

        self.horizontalLayout_35.addWidget(self.radio_btn_soft_wheels)

        self.radio_btn_hard_wheels = QRadioButton(self.frame_radio_buttons)
        self.radio_btn_hard_wheels.setObjectName(u"radio_btn_hard_wheels")
        self.radio_btn_hard_wheels.setFont(font)

        self.horizontalLayout_35.addWidget(self.radio_btn_hard_wheels)


        self.verticalLayout_7.addWidget(self.frame_radio_buttons)

        self.frame_pinion_material = QFrame(self.frame_input_data_2)
        self.frame_pinion_material.setObjectName(u"frame_pinion_material")
        sizePolicy3.setHeightForWidth(self.frame_pinion_material.sizePolicy().hasHeightForWidth())
        self.frame_pinion_material.setSizePolicy(sizePolicy3)
        self.frame_pinion_material.setMinimumSize(QSize(0, 42))
        self.frame_pinion_material.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_material.setStyleSheet(u"")
        self.frame_pinion_material.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_material.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_pinion_material)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_material = QLabel(self.frame_pinion_material)
        self.label_pinion_material.setObjectName(u"label_pinion_material")
        sizePolicy2.setHeightForWidth(self.label_pinion_material.sizePolicy().hasHeightForWidth())
        self.label_pinion_material.setSizePolicy(sizePolicy2)
        self.label_pinion_material.setMinimumSize(QSize(370, 0))
        self.label_pinion_material.setMaximumSize(QSize(370, 16777215))
        self.label_pinion_material.setFont(font)

        self.horizontalLayout_28.addWidget(self.label_pinion_material)

        self.comboBox_pinion_material = QComboBox(self.frame_pinion_material)
        self.comboBox_pinion_material.setObjectName(u"comboBox_pinion_material")
        sizePolicy1.setHeightForWidth(self.comboBox_pinion_material.sizePolicy().hasHeightForWidth())
        self.comboBox_pinion_material.setSizePolicy(sizePolicy1)
        self.comboBox_pinion_material.setMinimumSize(QSize(0, 0))
        self.comboBox_pinion_material.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_pinion_material.setFont(font2)
        self.comboBox_pinion_material.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"padding: 1px 1px 1px 1px;\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(76, 118, 232);\n"
"border-left: 1px solid rgb(242, 242, 246);\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::drop-down::hover{\n"
"	background-color: rgb(61, 101, 206);\n"
"}\n"
"QListView::item {\n"
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

        self.horizontalLayout_28.addWidget(self.comboBox_pinion_material)


        self.verticalLayout_7.addWidget(self.frame_pinion_material)

        self.frame_wheel_material = QFrame(self.frame_input_data_2)
        self.frame_wheel_material.setObjectName(u"frame_wheel_material")
        sizePolicy3.setHeightForWidth(self.frame_wheel_material.sizePolicy().hasHeightForWidth())
        self.frame_wheel_material.setSizePolicy(sizePolicy3)
        self.frame_wheel_material.setMaximumSize(QSize(16777215, 42))
        self.frame_wheel_material.setStyleSheet(u"")
        self.frame_wheel_material.setFrameShape(QFrame.StyledPanel)
        self.frame_wheel_material.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_wheel_material)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_wheel_material = QLabel(self.frame_wheel_material)
        self.label_wheel_material.setObjectName(u"label_wheel_material")
        sizePolicy2.setHeightForWidth(self.label_wheel_material.sizePolicy().hasHeightForWidth())
        self.label_wheel_material.setSizePolicy(sizePolicy2)
        self.label_wheel_material.setMinimumSize(QSize(370, 0))
        self.label_wheel_material.setMaximumSize(QSize(370, 16777215))
        self.label_wheel_material.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_wheel_material)

        self.comboBox_wheel_material = QComboBox(self.frame_wheel_material)
        self.comboBox_wheel_material.setObjectName(u"comboBox_wheel_material")
        sizePolicy1.setHeightForWidth(self.comboBox_wheel_material.sizePolicy().hasHeightForWidth())
        self.comboBox_wheel_material.setSizePolicy(sizePolicy1)
        self.comboBox_wheel_material.setMinimumSize(QSize(0, 0))
        self.comboBox_wheel_material.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_wheel_material.setFont(font2)

        self.horizontalLayout_20.addWidget(self.comboBox_wheel_material)


        self.verticalLayout_7.addWidget(self.frame_wheel_material)

        self.frame_accuracy_class = QFrame(self.frame_input_data_2)
        self.frame_accuracy_class.setObjectName(u"frame_accuracy_class")
        sizePolicy3.setHeightForWidth(self.frame_accuracy_class.sizePolicy().hasHeightForWidth())
        self.frame_accuracy_class.setSizePolicy(sizePolicy3)
        self.frame_accuracy_class.setStyleSheet(u"")
        self.frame_accuracy_class.setFrameShape(QFrame.StyledPanel)
        self.frame_accuracy_class.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_accuracy_class)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_accuracy_class = QLabel(self.frame_accuracy_class)
        self.label_accuracy_class.setObjectName(u"label_accuracy_class")
        sizePolicy2.setHeightForWidth(self.label_accuracy_class.sizePolicy().hasHeightForWidth())
        self.label_accuracy_class.setSizePolicy(sizePolicy2)
        self.label_accuracy_class.setMinimumSize(QSize(370, 40))
        self.label_accuracy_class.setMaximumSize(QSize(370, 16777215))
        self.label_accuracy_class.setFont(font)

        self.horizontalLayout_29.addWidget(self.label_accuracy_class)

        self.comboBox_accuracy_class = QComboBox(self.frame_accuracy_class)
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.addItem("")
        self.comboBox_accuracy_class.setObjectName(u"comboBox_accuracy_class")
        sizePolicy1.setHeightForWidth(self.comboBox_accuracy_class.sizePolicy().hasHeightForWidth())
        self.comboBox_accuracy_class.setSizePolicy(sizePolicy1)
        self.comboBox_accuracy_class.setMinimumSize(QSize(0, 0))
        self.comboBox_accuracy_class.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_accuracy_class.setFont(font2)

        self.horizontalLayout_29.addWidget(self.comboBox_accuracy_class)


        self.verticalLayout_7.addWidget(self.frame_accuracy_class)

        self.frame_pressure_angle = QFrame(self.frame_input_data_2)
        self.frame_pressure_angle.setObjectName(u"frame_pressure_angle")
        sizePolicy3.setHeightForWidth(self.frame_pressure_angle.sizePolicy().hasHeightForWidth())
        self.frame_pressure_angle.setSizePolicy(sizePolicy3)
        self.frame_pressure_angle.setStyleSheet(u"")
        self.frame_pressure_angle.setFrameShape(QFrame.StyledPanel)
        self.frame_pressure_angle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_pressure_angle)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_pressure_angle = QLabel(self.frame_pressure_angle)
        self.label_pressure_angle.setObjectName(u"label_pressure_angle")
        sizePolicy2.setHeightForWidth(self.label_pressure_angle.sizePolicy().hasHeightForWidth())
        self.label_pressure_angle.setSizePolicy(sizePolicy2)
        self.label_pressure_angle.setMinimumSize(QSize(370, 0))
        self.label_pressure_angle.setMaximumSize(QSize(370, 16777215))
        self.label_pressure_angle.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_pressure_angle)

        self.lineEdit_pressure_angle = QLineEdit(self.frame_pressure_angle)
        self.lineEdit_pressure_angle.setObjectName(u"lineEdit_pressure_angle")
        sizePolicy1.setHeightForWidth(self.lineEdit_pressure_angle.sizePolicy().hasHeightForWidth())
        self.lineEdit_pressure_angle.setSizePolicy(sizePolicy1)
        self.lineEdit_pressure_angle.setMinimumSize(QSize(0, 40))
        self.lineEdit_pressure_angle.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pressure_angle.setFont(font)
        self.lineEdit_pressure_angle.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pressure_angle.setDragEnabled(False)
        self.lineEdit_pressure_angle.setClearButtonEnabled(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_pressure_angle)


        self.verticalLayout_7.addWidget(self.frame_pressure_angle)

        self.frame_helix_angle = QFrame(self.frame_input_data_2)
        self.frame_helix_angle.setObjectName(u"frame_helix_angle")
        sizePolicy3.setHeightForWidth(self.frame_helix_angle.sizePolicy().hasHeightForWidth())
        self.frame_helix_angle.setSizePolicy(sizePolicy3)
        self.frame_helix_angle.setStyleSheet(u"")
        self.frame_helix_angle.setFrameShape(QFrame.StyledPanel)
        self.frame_helix_angle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_helix_angle)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_helix_angle = QLabel(self.frame_helix_angle)
        self.label_helix_angle.setObjectName(u"label_helix_angle")
        sizePolicy2.setHeightForWidth(self.label_helix_angle.sizePolicy().hasHeightForWidth())
        self.label_helix_angle.setSizePolicy(sizePolicy2)
        self.label_helix_angle.setMinimumSize(QSize(370, 40))
        self.label_helix_angle.setMaximumSize(QSize(370, 16777215))
        self.label_helix_angle.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_helix_angle)

        self.comboBox_helix_angle = QComboBox(self.frame_helix_angle)
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.addItem("")
        self.comboBox_helix_angle.setObjectName(u"comboBox_helix_angle")
        sizePolicy1.setHeightForWidth(self.comboBox_helix_angle.sizePolicy().hasHeightForWidth())
        self.comboBox_helix_angle.setSizePolicy(sizePolicy1)
        self.comboBox_helix_angle.setFont(font2)
        self.comboBox_helix_angle.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.comboBox_helix_angle)


        self.verticalLayout_7.addWidget(self.frame_helix_angle)

        self.frame_teeth_number = QFrame(self.frame_input_data_2)
        self.frame_teeth_number.setObjectName(u"frame_teeth_number")
        sizePolicy3.setHeightForWidth(self.frame_teeth_number.sizePolicy().hasHeightForWidth())
        self.frame_teeth_number.setSizePolicy(sizePolicy3)
        self.frame_teeth_number.setStyleSheet(u"")
        self.frame_teeth_number.setFrameShape(QFrame.StyledPanel)
        self.frame_teeth_number.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_teeth_number)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_teeth_number = QLabel(self.frame_teeth_number)
        self.label_teeth_number.setObjectName(u"label_teeth_number")
        sizePolicy2.setHeightForWidth(self.label_teeth_number.sizePolicy().hasHeightForWidth())
        self.label_teeth_number.setSizePolicy(sizePolicy2)
        self.label_teeth_number.setMinimumSize(QSize(370, 40))
        self.label_teeth_number.setMaximumSize(QSize(370, 16777215))
        self.label_teeth_number.setFont(font)

        self.horizontalLayout_33.addWidget(self.label_teeth_number)

        self.comboBox_teeth_number = QComboBox(self.frame_teeth_number)
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.addItem("")
        self.comboBox_teeth_number.setObjectName(u"comboBox_teeth_number")
        sizePolicy1.setHeightForWidth(self.comboBox_teeth_number.sizePolicy().hasHeightForWidth())
        self.comboBox_teeth_number.setSizePolicy(sizePolicy1)
        self.comboBox_teeth_number.setMinimumSize(QSize(0, 0))
        self.comboBox_teeth_number.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_teeth_number.setFont(font2)

        self.horizontalLayout_33.addWidget(self.comboBox_teeth_number)


        self.verticalLayout_7.addWidget(self.frame_teeth_number)


        self.verticalLayout_6.addWidget(self.frame_input_data_2)


        self.verticalLayout_8.addWidget(self.row_frame_2)

        self.preconditions_bottom_frame = QFrame(self.zalozenia_page)
        self.preconditions_bottom_frame.setObjectName(u"preconditions_bottom_frame")
        self.preconditions_bottom_frame.setMaximumSize(QSize(16777215, 50))
        self.preconditions_bottom_frame.setFrameShape(QFrame.NoFrame)
        self.preconditions_bottom_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.preconditions_bottom_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.preconditions_left_bottom_frame = QFrame(self.preconditions_bottom_frame)
        self.preconditions_left_bottom_frame.setObjectName(u"preconditions_left_bottom_frame")
        sizePolicy.setHeightForWidth(self.preconditions_left_bottom_frame.sizePolicy().hasHeightForWidth())
        self.preconditions_left_bottom_frame.setSizePolicy(sizePolicy)
        self.preconditions_left_bottom_frame.setMaximumSize(QSize(16777215, 50))
        self.preconditions_left_bottom_frame.setFrameShape(QFrame.NoFrame)
        self.preconditions_left_bottom_frame.setFrameShadow(QFrame.Plain)
        self.preconditions_left_bottom_frame.setMidLineWidth(0)

        self.horizontalLayout_9.addWidget(self.preconditions_left_bottom_frame)

        self.preconditions_btns_frame = QFrame(self.preconditions_bottom_frame)
        self.preconditions_btns_frame.setObjectName(u"preconditions_btns_frame")
        self.preconditions_btns_frame.setMaximumSize(QSize(16777215, 50))
        self.preconditions_btns_frame.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 40;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")
        self.preconditions_btns_frame.setFrameShape(QFrame.NoFrame)
        self.preconditions_btns_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.preconditions_btns_frame)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.preconditions_calculate_btn = QPushButton(self.preconditions_btns_frame)
        self.preconditions_calculate_btn.setObjectName(u"preconditions_calculate_btn")
        sizePolicy1.setHeightForWidth(self.preconditions_calculate_btn.sizePolicy().hasHeightForWidth())
        self.preconditions_calculate_btn.setSizePolicy(sizePolicy1)
        self.preconditions_calculate_btn.setMaximumSize(QSize(16777215, 16777215))
        self.preconditions_calculate_btn.setFont(font)

        self.horizontalLayout_10.addWidget(self.preconditions_calculate_btn)

        self.preconditions_clear_btn = QPushButton(self.preconditions_btns_frame)
        self.preconditions_clear_btn.setObjectName(u"preconditions_clear_btn")
        sizePolicy1.setHeightForWidth(self.preconditions_clear_btn.sizePolicy().hasHeightForWidth())
        self.preconditions_clear_btn.setSizePolicy(sizePolicy1)
        self.preconditions_clear_btn.setMaximumSize(QSize(16777215, 16777215))
        self.preconditions_clear_btn.setFont(font)

        self.horizontalLayout_10.addWidget(self.preconditions_clear_btn)


        self.horizontalLayout_9.addWidget(self.preconditions_btns_frame)


        self.verticalLayout_8.addWidget(self.preconditions_bottom_frame)

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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KALKULATOR PRZEK\u0141ADNI WALCOWYCH", None))
        self.minimize_btn.setText("")
        self.restore_btn.setText("")
        self.close_btn.setText("")
        self.materials_btn.setText(QCoreApplication.translate("MainWindow", u"DANE WEJ\u015aCIOWE", None))
        self.input_btn.setText(QCoreApplication.translate("MainWindow", u"ZA\u0141O\u017bENIA", None))
        self.base_outcome_btn.setText(QCoreApplication.translate("MainWindow", u"WYNIKI WST\u0118PNE", None))
        self.forces_btn.setText(QCoreApplication.translate("MainWindow", u"NAPR\u0118\u017bENIA", None))
        self.diameters_btn.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICE", None))
        self.excel_btn.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.scheme_btn.setText(QCoreApplication.translate("MainWindow", u"SCHEMAT", None))
        self.label_input_data.setText(QCoreApplication.translate("MainWindow", u"DANE WEJ\u015aCIOWE", None))
        self.label_power.setText(QCoreApplication.translate("MainWindow", u"MOC NOMINALNA", None))
        self.lineEdit_power.setPlaceholderText("")
        self.comboBox_power.setItemText(0, QCoreApplication.translate("MainWindow", u"W", None))
        self.comboBox_power.setItemText(1, QCoreApplication.translate("MainWindow", u"kW", None))
        self.comboBox_power.setItemText(2, QCoreApplication.translate("MainWindow", u"MW", None))

        self.label_ratio.setText(QCoreApplication.translate("MainWindow", u"PRZE\u0141O\u017bENIE CA\u0141KOWITE", None))
        self.lineEdit_ratio.setPlaceholderText("")
        self.label_velocity_in.setText(QCoreApplication.translate("MainWindow", u"PR\u0118DKO\u015a\u0106 OBROTOWA NA WALE WEJ\u015aCIOWYM", None))
        self.lineEdit_velocity_in.setPlaceholderText("")
        self.comboBox_velocity_in.setItemText(0, QCoreApplication.translate("MainWindow", u"obr/min", None))
        self.comboBox_velocity_in.setItemText(1, QCoreApplication.translate("MainWindow", u"rad/s", None))

        self.label_velocity_out.setText(QCoreApplication.translate("MainWindow", u"PR\u0118DKO\u015a\u0106 OBROTOWA NA WALE WYJ\u015aCIOWYM", None))
        self.lineEdit_velocity_out.setPlaceholderText("")
        self.comboBox_velocity_out.setItemText(0, QCoreApplication.translate("MainWindow", u"obr/min", None))
        self.comboBox_velocity_out.setItemText(1, QCoreApplication.translate("MainWindow", u"rad/s", None))

        self.label_driving_machine.setText(QCoreApplication.translate("MainWindow", u"MASZYNA NAP\u0118DZAJ\u0104CA", None))
        self.comboBox_driving_machine.setItemText(0, QCoreApplication.translate("MainWindow", u"Silnik elektryczny", None))
        self.comboBox_driving_machine.setItemText(1, QCoreApplication.translate("MainWindow", u"Turbina parowa", None))
        self.comboBox_driving_machine.setItemText(2, QCoreApplication.translate("MainWindow", u"Turbina gazowa", None))
        self.comboBox_driving_machine.setItemText(3, QCoreApplication.translate("MainWindow", u"Silnik t\u0142okowy o liczbie cylindr\u00f3w wi\u0119kszej ni\u017c dwa", None))
        self.comboBox_driving_machine.setItemText(4, QCoreApplication.translate("MainWindow", u"Silnik hydrauliczny", None))
        self.comboBox_driving_machine.setItemText(5, QCoreApplication.translate("MainWindow", u"Silnik t\u0142okowy jedno- lub dwucylindrowy", None))

        self.label_driven_machine.setText(QCoreApplication.translate("MainWindow", u"MASZYNA NAP\u0118DZANA", None))
        self.comboBox_driven_machine.setItemText(0, QCoreApplication.translate("MainWindow", u"Podno\u015bnik, winda (r\u00f3wnomiernie obci\u0105\u017cony)", None))
        self.comboBox_driven_machine.setItemText(1, QCoreApplication.translate("MainWindow", u"M\u0142yn do cementu", None))
        self.comboBox_driven_machine.setItemText(2, QCoreApplication.translate("MainWindow", u"Podno\u015bnik, winda (nier\u00f3wnomiernie obci\u0105\u017cony)", None))
        self.comboBox_driven_machine.setItemText(3, QCoreApplication.translate("MainWindow", u"Przeci\u0105garka do drutu", None))
        self.comboBox_driven_machine.setItemText(4, QCoreApplication.translate("MainWindow", u"Koparka wieloczerpakowa \u0142a\u0144cuchowa", None))
        self.comboBox_driven_machine.setItemText(5, QCoreApplication.translate("MainWindow", u"Pr\u0105dnica (opr\u00f3cz pr\u0105dnicy spawalniczej)", None))
        self.comboBox_driven_machine.setItemText(6, QCoreApplication.translate("MainWindow", u"Koparka z ko\u0142em czerpakowym", None))
        self.comboBox_driven_machine.setItemText(7, QCoreApplication.translate("MainWindow", u"Pr\u0105dnica spawalnicza", None))
        self.comboBox_driven_machine.setItemText(8, QCoreApplication.translate("MainWindow", u"Koparka z g\u0142owic\u0105 tn\u0105c\u0105", None))
        self.comboBox_driven_machine.setItemText(9, QCoreApplication.translate("MainWindow", u"Walce do gumy", None))
        self.comboBox_driven_machine.setItemText(10, QCoreApplication.translate("MainWindow", u"Kruszarka", None))
        self.comboBox_driven_machine.setItemText(11, QCoreApplication.translate("MainWindow", u"Ku\u017aniarka", None))
        self.comboBox_driven_machine.setItemText(12, QCoreApplication.translate("MainWindow", u"Piec obrotowy", None))
        self.comboBox_driven_machine.setItemText(13, QCoreApplication.translate("MainWindow", u"Kolej linowa", None))
        self.comboBox_driven_machine.setItemText(14, QCoreApplication.translate("MainWindow", u"Przeno\u015bnik ta\u015bmowy (r\u00f3wnomiernie obci\u0105\u017cony)", None))
        self.comboBox_driven_machine.setItemText(15, QCoreApplication.translate("MainWindow", u"Obrabiarka do drewna", None))
        self.comboBox_driven_machine.setItemText(16, QCoreApplication.translate("MainWindow", u"Przeno\u015bnik ta\u015bmowy (nier\u00f3wnomiernie obci\u0105\u017cony)", None))
        self.comboBox_driven_machine.setItemText(17, QCoreApplication.translate("MainWindow", u"Spr\u0119\u017carka t\u0142okowa jednocylindrowa", None))
        self.comboBox_driven_machine.setItemText(18, QCoreApplication.translate("MainWindow", u"Ko\u0142owr\u00f3t wyci\u0105gowy", None))
        self.comboBox_driven_machine.setItemText(19, QCoreApplication.translate("MainWindow", u"Spr\u0119\u017carka t\u0142okowa wielocylindrowa", None))
        self.comboBox_driven_machine.setItemText(20, QCoreApplication.translate("MainWindow", u"\u017buraw", None))
        self.comboBox_driven_machine.setItemText(21, QCoreApplication.translate("MainWindow", u"Spr\u0119\u017carka osiowa", None))
        self.comboBox_driven_machine.setItemText(22, QCoreApplication.translate("MainWindow", u"Mieszarka do betonu", None))
        self.comboBox_driven_machine.setItemText(23, QCoreApplication.translate("MainWindow", u"Konwertor", None))
        self.comboBox_driven_machine.setItemText(24, QCoreApplication.translate("MainWindow", u"Maszyna papiernicza (obci\u0105\u017cona r\u00f3wnomiernie)", None))
        self.comboBox_driven_machine.setItemText(25, QCoreApplication.translate("MainWindow", u"Pompa t\u0142okowa trzy- i wi\u0119cej cylindrowa", None))
        self.comboBox_driven_machine.setItemText(26, QCoreApplication.translate("MainWindow", u"Maszyna papiernicza (obci\u0105\u017cona nier\u00f3wnomiernie)", None))
        self.comboBox_driven_machine.setItemText(27, QCoreApplication.translate("MainWindow", u"Pompa od\u015brodkowa", None))
        self.comboBox_driven_machine.setItemText(28, QCoreApplication.translate("MainWindow", u"Prasa do brykiet\u00f3w", None))
        self.comboBox_driven_machine.setItemText(29, QCoreApplication.translate("MainWindow", u"Pompa wyporowa", None))
        self.comboBox_driven_machine.setItemText(30, QCoreApplication.translate("MainWindow", u"Prasa korbowa, mimo\u015brodowa, ku\u017anicza", None))
        self.comboBox_driven_machine.setItemText(31, QCoreApplication.translate("MainWindow", u"Maszyna sterowa", None))
        self.comboBox_driven_machine.setItemText(32, QCoreApplication.translate("MainWindow", u"Prasa do cegie\u0142", None))
        self.comboBox_driven_machine.setItemText(33, QCoreApplication.translate("MainWindow", u"Mieszalnik do lekkich cieczy", None))
        self.comboBox_driven_machine.setItemText(34, QCoreApplication.translate("MainWindow", u"\u015aruba okr\u0119towa", None))
        self.comboBox_driven_machine.setItemText(35, QCoreApplication.translate("MainWindow", u"Mieszalnik do cieczy lepkich i cia\u0142 sta\u0142ych", None))
        self.comboBox_driven_machine.setItemText(36, QCoreApplication.translate("MainWindow", u"Pompa pog\u0142\u0119biarki", None))
        self.comboBox_driven_machine.setItemText(37, QCoreApplication.translate("MainWindow", u"Maszyny tkackie", None))
        self.comboBox_driven_machine.setItemText(38, QCoreApplication.translate("MainWindow", u"Pompa t\u0142okowa 1- lub 2-cylindrowa", None))
        self.comboBox_driven_machine.setItemText(39, QCoreApplication.translate("MainWindow", u"Wentylator du\u017cy (np. kopalniany)", None))
        self.comboBox_driven_machine.setItemText(40, QCoreApplication.translate("MainWindow", u"P\u0142uczarka", None))
        self.comboBox_driven_machine.setItemText(41, QCoreApplication.translate("MainWindow", u"Wentylator ma\u0142y", None))
        self.comboBox_driven_machine.setItemText(42, QCoreApplication.translate("MainWindow", u"Obrabiarka o ruchu obrotowym", None))
        self.comboBox_driven_machine.setItemText(43, QCoreApplication.translate("MainWindow", u"Walcarka do wlewk\u00f3w", None))
        self.comboBox_driven_machine.setItemText(44, QCoreApplication.translate("MainWindow", u"Obrabiarka o ruchu posuwisto-zwrotnym", None))
        self.comboBox_driven_machine.setItemText(45, QCoreApplication.translate("MainWindow", u"Walcarka do ta\u015bmy lub drutu", None))
        self.comboBox_driven_machine.setItemText(46, QCoreApplication.translate("MainWindow", u"Wci\u0105garka", None))
        self.comboBox_driven_machine.setItemText(47, QCoreApplication.translate("MainWindow", u"Walcarka do ci\u0119cia no\u017cycami", None))

        self.label_durability.setText(QCoreApplication.translate("MainWindow", u"WYMAGANA TRWA\u0141O\u015a\u0106 CZASOWA", None))
        self.lineEdit_durability.setPlaceholderText("")
        self.comboBox_durability.setItemText(0, QCoreApplication.translate("MainWindow", u"s", None))
        self.comboBox_durability.setItemText(1, QCoreApplication.translate("MainWindow", u"min.", None))
        self.comboBox_durability.setItemText(2, QCoreApplication.translate("MainWindow", u"h", None))

        self.label_wheelbase.setText(QCoreApplication.translate("MainWindow", u"ODLEG\u0141O\u015a\u0106 OSI PRZEK\u0141ADNI", None))
        self.lineEdit_wheelbase.setPlaceholderText("")
        self.comboBox_wheelbase.setItemText(0, QCoreApplication.translate("MainWindow", u"mm", None))
        self.comboBox_wheelbase.setItemText(1, QCoreApplication.translate("MainWindow", u"cm", None))
        self.comboBox_wheelbase.setItemText(2, QCoreApplication.translate("MainWindow", u"m", None))

        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"OBLICZ", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"WYCZY\u015a\u0106", None))
        self.label_preconditions.setText(QCoreApplication.translate("MainWindow", u"ZA\u0141O\u017bENIA", None))
        self.radio_btn_soft_wheels.setText(QCoreApplication.translate("MainWindow", u"KO\u0141A MI\u0118KKIE", None))
        self.radio_btn_hard_wheels.setText(QCoreApplication.translate("MainWindow", u"KO\u0141A TWARDE", None))
        self.label_pinion_material.setText(QCoreApplication.translate("MainWindow", u"MATERIA\u0141 Z\u0118BNIKA", None))
        self.label_wheel_material.setText(QCoreApplication.translate("MainWindow", u"MATERIA\u0141 KO\u0141A", None))
        self.label_accuracy_class.setText(QCoreApplication.translate("MainWindow", u"KLASA DOK\u0141ADNO\u015aCI WYKONANIA K\u00d3\u0141 ", None))
        self.comboBox_accuracy_class.setItemText(0, QCoreApplication.translate("MainWindow", u"IT1", None))
        self.comboBox_accuracy_class.setItemText(1, QCoreApplication.translate("MainWindow", u"IT2", None))
        self.comboBox_accuracy_class.setItemText(2, QCoreApplication.translate("MainWindow", u"IT3", None))
        self.comboBox_accuracy_class.setItemText(3, QCoreApplication.translate("MainWindow", u"IT4", None))
        self.comboBox_accuracy_class.setItemText(4, QCoreApplication.translate("MainWindow", u"IT5", None))
        self.comboBox_accuracy_class.setItemText(5, QCoreApplication.translate("MainWindow", u"IT6", None))
        self.comboBox_accuracy_class.setItemText(6, QCoreApplication.translate("MainWindow", u"IT7", None))
        self.comboBox_accuracy_class.setItemText(7, QCoreApplication.translate("MainWindow", u"IT8", None))
        self.comboBox_accuracy_class.setItemText(8, QCoreApplication.translate("MainWindow", u"IT9", None))
        self.comboBox_accuracy_class.setItemText(9, QCoreApplication.translate("MainWindow", u"IT10", None))
        self.comboBox_accuracy_class.setItemText(10, QCoreApplication.translate("MainWindow", u"IT11", None))
        self.comboBox_accuracy_class.setItemText(11, QCoreApplication.translate("MainWindow", u"IT12", None))

        self.label_pressure_angle.setText(QCoreApplication.translate("MainWindow", u"NORMALNY K\u0104T PRZYPORU", None))
        self.lineEdit_pressure_angle.setPlaceholderText("")
        self.label_helix_angle.setText(QCoreApplication.translate("MainWindow", u"K\u0104T POCHYLENIA LINII \u015aRUBOWEJ Z\u0118BA", None))
        self.comboBox_helix_angle.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_helix_angle.setItemText(1, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_helix_angle.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_helix_angle.setItemText(3, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_helix_angle.setItemText(4, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_helix_angle.setItemText(5, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_helix_angle.setItemText(6, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_helix_angle.setItemText(7, QCoreApplication.translate("MainWindow", u"15", None))

        self.label_teeth_number.setText(QCoreApplication.translate("MainWindow", u"LICZBA Z\u0118B\u00d3W Z\u0118BNIKA", None))
        self.comboBox_teeth_number.setItemText(0, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_teeth_number.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_teeth_number.setItemText(2, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_teeth_number.setItemText(3, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_teeth_number.setItemText(4, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_teeth_number.setItemText(5, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_teeth_number.setItemText(6, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_teeth_number.setItemText(7, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_teeth_number.setItemText(8, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_teeth_number.setItemText(9, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_teeth_number.setItemText(10, QCoreApplication.translate("MainWindow", u"25", None))

        self.preconditions_calculate_btn.setText(QCoreApplication.translate("MainWindow", u"OBLICZ", None))
        self.preconditions_clear_btn.setText(QCoreApplication.translate("MainWindow", u"WYCZY\u015a\u0106", None))
    # retranslateUi


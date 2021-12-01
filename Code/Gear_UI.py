from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from data.correction_factors_diag import MplWidget

import demo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 665)
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
        self.main_body.setAcceptDrops(False)
        self.main_body.setLayoutDirection(Qt.LeftToRight)
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

        self.factors_btn = QPushButton(self.buttons_frame)
        self.factors_btn.setObjectName(u"factors_btn")
        self.factors_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.factors_btn.sizePolicy().hasHeightForWidth())
        self.factors_btn.setSizePolicy(sizePolicy1)
        self.factors_btn.setFont(font)
        self.factors_btn.setStyleSheet(u"background-color: rgb(180, 180, 180);")
        self.factors_btn.setCheckable(True)
        self.factors_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.factors_btn)

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
        self.page_input_data_main_frame = QFrame(self.page_input_data)
        self.page_input_data_main_frame.setObjectName(u"page_input_data_main_frame")
        sizePolicy.setHeightForWidth(self.page_input_data_main_frame.sizePolicy().hasHeightForWidth())
        self.page_input_data_main_frame.setSizePolicy(sizePolicy)
        self.page_input_data_main_frame.setFont(font)
        self.page_input_data_main_frame.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: 1px solid rgb(180,180,180);\n"
"padding-left: 3px;\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"padding: 1px 1px 1px 1px;\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"margin-right: 2px;\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"background-color: rgb(76, 118, 232);\n"
"border-radius: 10px;\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::down-arrow::hover{\n"
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
"   border-color: rgb(0, 93, 16"
                        "8);\n"
"   border-radius: 20px;\n"
"}")
        self.page_input_data_main_frame.setFrameShape(QFrame.NoFrame)
        self.page_input_data_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.page_input_data_main_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_input_label = QFrame(self.page_input_data_main_frame)
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

        self.frame_input_data = QFrame(self.page_input_data_main_frame)
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
        self.comboBox_power.setStyleSheet(u"")

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
        self.lineEdit_ratio.setStyleSheet(u"margin: 10px 0px 10px 10px;")
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
        self.comboBox_driving_machine.setStyleSheet(u"margin-left: 10px;")

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
        self.comboBox_driven_machine.setStyleSheet(u"margin-left: 10px;")

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


        self.verticalLayout_3.addWidget(self.page_input_data_main_frame)

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
        self.page_preconditions = QWidget()
        self.page_preconditions.setObjectName(u"page_preconditions")
        self.verticalLayout_8 = QVBoxLayout(self.page_preconditions)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 0)
        self.page_preconditions_main_frame = QFrame(self.page_preconditions)
        self.page_preconditions_main_frame.setObjectName(u"page_preconditions_main_frame")
        sizePolicy.setHeightForWidth(self.page_preconditions_main_frame.sizePolicy().hasHeightForWidth())
        self.page_preconditions_main_frame.setSizePolicy(sizePolicy)
        self.page_preconditions_main_frame.setFont(font)
        self.page_preconditions_main_frame.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: 1px solid rgb(180,180,180);\n"
"padding-left: 3px;\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(33, 38, 55);\n"
"border: 1px solid rgb(242, 242, 246);\n"
"padding: 1px 1px 1px 1px;\n"
"margin-left: 10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"margin-right: 2px;\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"background-color: rgb(76, 118, 232);\n"
"border-radius: 10px;\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::down-arrow::hover{\n"
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
"   bord"
                        "er-color: rgb(0, 93, 168);\n"
"   border-radius: 20px;\n"
"}")
        self.page_preconditions_main_frame.setFrameShape(QFrame.NoFrame)
        self.page_preconditions_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.page_preconditions_main_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_preconditions = QFrame(self.page_preconditions_main_frame)
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

        self.frame_input_data_2 = QFrame(self.page_preconditions_main_frame)
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
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"margin-right: 2px;\n"
"width:20px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"image: url(:/demo/icons/cil-arrow-circle-bottom.png);\n"
"background-color: rgb(76, 118, 232);\n"
"border-radius: 10px;\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox::down-arrow::hover{\n"
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
        self.label_pressure_angle.setMinimumSize(QSize(370, 40))
        self.label_pressure_angle.setMaximumSize(QSize(370, 16777215))
        self.label_pressure_angle.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_pressure_angle)

        self.lineEdit_pressure_angle = QLineEdit(self.frame_pressure_angle)
        self.lineEdit_pressure_angle.setObjectName(u"lineEdit_pressure_angle")
        sizePolicy1.setHeightForWidth(self.lineEdit_pressure_angle.sizePolicy().hasHeightForWidth())
        self.lineEdit_pressure_angle.setSizePolicy(sizePolicy1)
        self.lineEdit_pressure_angle.setMinimumSize(QSize(0, 40))
        self.lineEdit_pressure_angle.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_pressure_angle.setFont(font)
        self.lineEdit_pressure_angle.setStyleSheet(u"margin: 10px 0px 10px 10px;")
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


        self.verticalLayout_8.addWidget(self.page_preconditions_main_frame)

        self.preconditions_bottom_frame = QFrame(self.page_preconditions)
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

        self.stackedWidget.addWidget(self.page_preconditions)
        self.page_preliminary_results = QWidget()
        self.page_preliminary_results.setObjectName(u"page_preliminary_results")
        self.verticalLayout_11 = QVBoxLayout(self.page_preliminary_results)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 0)
        self.page_preliminary_results_main_frame = QFrame(self.page_preliminary_results)
        self.page_preliminary_results_main_frame.setObjectName(u"page_preliminary_results_main_frame")
        sizePolicy.setHeightForWidth(self.page_preliminary_results_main_frame.sizePolicy().hasHeightForWidth())
        self.page_preliminary_results_main_frame.setSizePolicy(sizePolicy)
        self.page_preliminary_results_main_frame.setFont(font)
        self.page_preliminary_results_main_frame.setStyleSheet(u"QLabel{\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: 1px solid rgb(180,180,180);padding-left: 3px;\n"
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
"   border-color: rgb(0, 93, 16"
                        "8);\n"
"   border-radius: 20px;\n"
"}")
        self.page_preliminary_results_main_frame.setFrameShape(QFrame.NoFrame)
        self.page_preliminary_results_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.page_preliminary_results_main_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_preconditions_2 = QFrame(self.page_preliminary_results_main_frame)
        self.frame_preconditions_2.setObjectName(u"frame_preconditions_2")
        sizePolicy.setHeightForWidth(self.frame_preconditions_2.sizePolicy().hasHeightForWidth())
        self.frame_preconditions_2.setSizePolicy(sizePolicy)
        self.frame_preconditions_2.setMaximumSize(QSize(16777215, 50))
        self.frame_preconditions_2.setFont(font)
        self.frame_preconditions_2.setFrameShape(QFrame.NoFrame)
        self.frame_preconditions_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_preconditions_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_preconditions_2 = QLabel(self.frame_preconditions_2)
        self.label_preconditions_2.setObjectName(u"label_preconditions_2")
        sizePolicy2.setHeightForWidth(self.label_preconditions_2.sizePolicy().hasHeightForWidth())
        self.label_preconditions_2.setSizePolicy(sizePolicy2)
        self.label_preconditions_2.setMinimumSize(QSize(260, 30))
        self.label_preconditions_2.setMaximumSize(QSize(260, 30))
        self.label_preconditions_2.setFont(font1)
        self.label_preconditions_2.setTextFormat(Qt.PlainText)

        self.horizontalLayout_11.addWidget(self.label_preconditions_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frame_preconditions_2)

        self.frame_input_data_3 = QFrame(self.page_preliminary_results_main_frame)
        self.frame_input_data_3.setObjectName(u"frame_input_data_3")
        sizePolicy.setHeightForWidth(self.frame_input_data_3.sizePolicy().hasHeightForWidth())
        self.frame_input_data_3.setSizePolicy(sizePolicy)
        self.frame_input_data_3.setFont(font)
        self.frame_input_data_3.setFrameShape(QFrame.NoFrame)
        self.frame_input_data_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_input_data_3)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(10, 0, 0, 0)
        self.frame_pinion_torque = QFrame(self.frame_input_data_3)
        self.frame_pinion_torque.setObjectName(u"frame_pinion_torque")
        sizePolicy3.setHeightForWidth(self.frame_pinion_torque.sizePolicy().hasHeightForWidth())
        self.frame_pinion_torque.setSizePolicy(sizePolicy3)
        self.frame_pinion_torque.setMinimumSize(QSize(0, 42))
        self.frame_pinion_torque.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_torque.setStyleSheet(u"")
        self.frame_pinion_torque.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_torque.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_pinion_torque)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_toqrue = QLabel(self.frame_pinion_torque)
        self.label_pinion_toqrue.setObjectName(u"label_pinion_toqrue")
        sizePolicy2.setHeightForWidth(self.label_pinion_toqrue.sizePolicy().hasHeightForWidth())
        self.label_pinion_toqrue.setSizePolicy(sizePolicy2)
        self.label_pinion_toqrue.setMinimumSize(QSize(400, 0))
        self.label_pinion_toqrue.setMaximumSize(QSize(400, 16777215))
        self.label_pinion_toqrue.setFont(font)

        self.horizontalLayout_36.addWidget(self.label_pinion_toqrue)

        self.lineEdit_pinion_torque = QLineEdit(self.frame_pinion_torque)
        self.lineEdit_pinion_torque.setObjectName(u"lineEdit_pinion_torque")
        sizePolicy1.setHeightForWidth(self.lineEdit_pinion_torque.sizePolicy().hasHeightForWidth())
        self.lineEdit_pinion_torque.setSizePolicy(sizePolicy1)
        self.lineEdit_pinion_torque.setMinimumSize(QSize(0, 40))
        self.lineEdit_pinion_torque.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pinion_torque.setFont(font)
        self.lineEdit_pinion_torque.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pinion_torque.setDragEnabled(False)
        self.lineEdit_pinion_torque.setClearButtonEnabled(True)

        self.horizontalLayout_36.addWidget(self.lineEdit_pinion_torque)


        self.verticalLayout_10.addWidget(self.frame_pinion_torque)

        self.frame_calculated_normal_module = QFrame(self.frame_input_data_3)
        self.frame_calculated_normal_module.setObjectName(u"frame_calculated_normal_module")
        sizePolicy3.setHeightForWidth(self.frame_calculated_normal_module.sizePolicy().hasHeightForWidth())
        self.frame_calculated_normal_module.setSizePolicy(sizePolicy3)
        self.frame_calculated_normal_module.setMinimumSize(QSize(0, 42))
        self.frame_calculated_normal_module.setMaximumSize(QSize(16777215, 42))
        self.frame_calculated_normal_module.setStyleSheet(u"")
        self.frame_calculated_normal_module.setFrameShape(QFrame.StyledPanel)
        self.frame_calculated_normal_module.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_calculated_normal_module)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_calculated_normal_module = QLabel(self.frame_calculated_normal_module)
        self.label_calculated_normal_module.setObjectName(u"label_calculated_normal_module")
        sizePolicy2.setHeightForWidth(self.label_calculated_normal_module.sizePolicy().hasHeightForWidth())
        self.label_calculated_normal_module.setSizePolicy(sizePolicy2)
        self.label_calculated_normal_module.setMinimumSize(QSize(400, 0))
        self.label_calculated_normal_module.setMaximumSize(QSize(400, 16777215))
        self.label_calculated_normal_module.setFont(font)

        self.horizontalLayout_32.addWidget(self.label_calculated_normal_module)

        self.lineEdit_calculated_normal_module = QLineEdit(self.frame_calculated_normal_module)
        self.lineEdit_calculated_normal_module.setObjectName(u"lineEdit_calculated_normal_module")
        sizePolicy1.setHeightForWidth(self.lineEdit_calculated_normal_module.sizePolicy().hasHeightForWidth())
        self.lineEdit_calculated_normal_module.setSizePolicy(sizePolicy1)
        self.lineEdit_calculated_normal_module.setMinimumSize(QSize(0, 40))
        self.lineEdit_calculated_normal_module.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_calculated_normal_module.setFont(font)
        self.lineEdit_calculated_normal_module.setStyleSheet(u"margin: 10px;")
        self.lineEdit_calculated_normal_module.setDragEnabled(False)
        self.lineEdit_calculated_normal_module.setClearButtonEnabled(True)

        self.horizontalLayout_32.addWidget(self.lineEdit_calculated_normal_module)


        self.verticalLayout_10.addWidget(self.frame_calculated_normal_module)

        self.frame_normal_module = QFrame(self.frame_input_data_3)
        self.frame_normal_module.setObjectName(u"frame_normal_module")
        sizePolicy3.setHeightForWidth(self.frame_normal_module.sizePolicy().hasHeightForWidth())
        self.frame_normal_module.setSizePolicy(sizePolicy3)
        self.frame_normal_module.setMaximumSize(QSize(16777215, 42))
        self.frame_normal_module.setStyleSheet(u"")
        self.frame_normal_module.setFrameShape(QFrame.StyledPanel)
        self.frame_normal_module.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_normal_module)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_normal_module = QLabel(self.frame_normal_module)
        self.label_normal_module.setObjectName(u"label_normal_module")
        sizePolicy2.setHeightForWidth(self.label_normal_module.sizePolicy().hasHeightForWidth())
        self.label_normal_module.setSizePolicy(sizePolicy2)
        self.label_normal_module.setMinimumSize(QSize(400, 40))
        self.label_normal_module.setMaximumSize(QSize(400, 16777215))
        self.label_normal_module.setFont(font)

        self.horizontalLayout_26.addWidget(self.label_normal_module)

        self.comboBox_normal_module = QComboBox(self.frame_normal_module)
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.addItem("")
        self.comboBox_normal_module.setObjectName(u"comboBox_normal_module")
        sizePolicy1.setHeightForWidth(self.comboBox_normal_module.sizePolicy().hasHeightForWidth())
        self.comboBox_normal_module.setSizePolicy(sizePolicy1)
        self.comboBox_normal_module.setFont(font2)

        self.horizontalLayout_26.addWidget(self.comboBox_normal_module)

        self.normal_module_confirm_btn = QPushButton(self.frame_normal_module)
        self.normal_module_confirm_btn.setObjectName(u"normal_module_confirm_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.normal_module_confirm_btn.sizePolicy().hasHeightForWidth())
        self.normal_module_confirm_btn.setSizePolicy(sizePolicy5)
        self.normal_module_confirm_btn.setMinimumSize(QSize(0, 24))
        self.normal_module_confirm_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 20;\n"
"margin-right: 10px;\n"
"margin-left: 5px;\n"
"padding: 0 5 0 5;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.normal_module_confirm_btn)


        self.verticalLayout_10.addWidget(self.frame_normal_module)

        self.frame_bottom_ratio_border = QFrame(self.frame_input_data_3)
        self.frame_bottom_ratio_border.setObjectName(u"frame_bottom_ratio_border")
        sizePolicy3.setHeightForWidth(self.frame_bottom_ratio_border.sizePolicy().hasHeightForWidth())
        self.frame_bottom_ratio_border.setSizePolicy(sizePolicy3)
        self.frame_bottom_ratio_border.setStyleSheet(u"")
        self.frame_bottom_ratio_border.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom_ratio_border.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_bottom_ratio_border)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_bottome_ratio_border = QLabel(self.frame_bottom_ratio_border)
        self.label_bottome_ratio_border.setObjectName(u"label_bottome_ratio_border")
        sizePolicy2.setHeightForWidth(self.label_bottome_ratio_border.sizePolicy().hasHeightForWidth())
        self.label_bottome_ratio_border.setSizePolicy(sizePolicy2)
        self.label_bottome_ratio_border.setMinimumSize(QSize(400, 40))
        self.label_bottome_ratio_border.setMaximumSize(QSize(400, 16777215))
        self.label_bottome_ratio_border.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_bottome_ratio_border)

        self.lineEdit_bottom_ratio_border = QLineEdit(self.frame_bottom_ratio_border)
        self.lineEdit_bottom_ratio_border.setObjectName(u"lineEdit_bottom_ratio_border")
        self.lineEdit_bottom_ratio_border.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_bottom_ratio_border.sizePolicy().hasHeightForWidth())
        self.lineEdit_bottom_ratio_border.setSizePolicy(sizePolicy1)
        self.lineEdit_bottom_ratio_border.setMinimumSize(QSize(0, 40))
        self.lineEdit_bottom_ratio_border.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_bottom_ratio_border.setFont(font)
        self.lineEdit_bottom_ratio_border.setStyleSheet(u"margin: 10px;")
        self.lineEdit_bottom_ratio_border.setDragEnabled(False)
        self.lineEdit_bottom_ratio_border.setClearButtonEnabled(True)

        self.horizontalLayout_34.addWidget(self.lineEdit_bottom_ratio_border)


        self.verticalLayout_10.addWidget(self.frame_bottom_ratio_border)

        self.frame_upper_ratio_border = QFrame(self.frame_input_data_3)
        self.frame_upper_ratio_border.setObjectName(u"frame_upper_ratio_border")
        sizePolicy3.setHeightForWidth(self.frame_upper_ratio_border.sizePolicy().hasHeightForWidth())
        self.frame_upper_ratio_border.setSizePolicy(sizePolicy3)
        self.frame_upper_ratio_border.setStyleSheet(u"")
        self.frame_upper_ratio_border.setFrameShape(QFrame.StyledPanel)
        self.frame_upper_ratio_border.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_upper_ratio_border)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_upper_ratio_border = QLabel(self.frame_upper_ratio_border)
        self.label_upper_ratio_border.setObjectName(u"label_upper_ratio_border")
        sizePolicy2.setHeightForWidth(self.label_upper_ratio_border.sizePolicy().hasHeightForWidth())
        self.label_upper_ratio_border.setSizePolicy(sizePolicy2)
        self.label_upper_ratio_border.setMinimumSize(QSize(400, 0))
        self.label_upper_ratio_border.setMaximumSize(QSize(400, 16777215))
        self.label_upper_ratio_border.setFont(font)

        self.horizontalLayout_37.addWidget(self.label_upper_ratio_border)

        self.lineEdit_upper_ratio_border = QLineEdit(self.frame_upper_ratio_border)
        self.lineEdit_upper_ratio_border.setObjectName(u"lineEdit_upper_ratio_border")
        self.lineEdit_upper_ratio_border.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_upper_ratio_border.sizePolicy().hasHeightForWidth())
        self.lineEdit_upper_ratio_border.setSizePolicy(sizePolicy1)
        self.lineEdit_upper_ratio_border.setMinimumSize(QSize(0, 40))
        self.lineEdit_upper_ratio_border.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_upper_ratio_border.setFont(font)
        self.lineEdit_upper_ratio_border.setStyleSheet(u"margin: 10px;")
        self.lineEdit_upper_ratio_border.setDragEnabled(False)
        self.lineEdit_upper_ratio_border.setClearButtonEnabled(True)

        self.horizontalLayout_37.addWidget(self.lineEdit_upper_ratio_border)


        self.verticalLayout_10.addWidget(self.frame_upper_ratio_border)

        self.frame_calculated_tooth_number = QFrame(self.frame_input_data_3)
        self.frame_calculated_tooth_number.setObjectName(u"frame_calculated_tooth_number")
        sizePolicy3.setHeightForWidth(self.frame_calculated_tooth_number.sizePolicy().hasHeightForWidth())
        self.frame_calculated_tooth_number.setSizePolicy(sizePolicy3)
        self.frame_calculated_tooth_number.setStyleSheet(u"")
        self.frame_calculated_tooth_number.setFrameShape(QFrame.StyledPanel)
        self.frame_calculated_tooth_number.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_calculated_tooth_number)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_calculated_tooth_number = QLabel(self.frame_calculated_tooth_number)
        self.label_calculated_tooth_number.setObjectName(u"label_calculated_tooth_number")
        sizePolicy2.setHeightForWidth(self.label_calculated_tooth_number.sizePolicy().hasHeightForWidth())
        self.label_calculated_tooth_number.setSizePolicy(sizePolicy2)
        self.label_calculated_tooth_number.setMinimumSize(QSize(400, 40))
        self.label_calculated_tooth_number.setMaximumSize(QSize(400, 16777215))
        self.label_calculated_tooth_number.setFont(font)

        self.horizontalLayout_38.addWidget(self.label_calculated_tooth_number)

        self.lineEdit_calculated_tooth_number = QLineEdit(self.frame_calculated_tooth_number)
        self.lineEdit_calculated_tooth_number.setObjectName(u"lineEdit_calculated_tooth_number")
        self.lineEdit_calculated_tooth_number.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_calculated_tooth_number.sizePolicy().hasHeightForWidth())
        self.lineEdit_calculated_tooth_number.setSizePolicy(sizePolicy1)
        self.lineEdit_calculated_tooth_number.setMinimumSize(QSize(0, 40))
        self.lineEdit_calculated_tooth_number.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_calculated_tooth_number.setFont(font)
        self.lineEdit_calculated_tooth_number.setStyleSheet(u"margin: 10px;")
        self.lineEdit_calculated_tooth_number.setDragEnabled(False)
        self.lineEdit_calculated_tooth_number.setClearButtonEnabled(True)

        self.horizontalLayout_38.addWidget(self.lineEdit_calculated_tooth_number)


        self.verticalLayout_10.addWidget(self.frame_calculated_tooth_number)

        self.frame_2md_wheel_tooth_number = QFrame(self.frame_input_data_3)
        self.frame_2md_wheel_tooth_number.setObjectName(u"frame_2md_wheel_tooth_number")
        sizePolicy3.setHeightForWidth(self.frame_2md_wheel_tooth_number.sizePolicy().hasHeightForWidth())
        self.frame_2md_wheel_tooth_number.setSizePolicy(sizePolicy3)
        self.frame_2md_wheel_tooth_number.setStyleSheet(u"")
        self.frame_2md_wheel_tooth_number.setFrameShape(QFrame.StyledPanel)
        self.frame_2md_wheel_tooth_number.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_2md_wheel_tooth_number)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_2nd_wheel_tooth_number = QLabel(self.frame_2md_wheel_tooth_number)
        self.label_2nd_wheel_tooth_number.setObjectName(u"label_2nd_wheel_tooth_number")
        sizePolicy2.setHeightForWidth(self.label_2nd_wheel_tooth_number.sizePolicy().hasHeightForWidth())
        self.label_2nd_wheel_tooth_number.setSizePolicy(sizePolicy2)
        self.label_2nd_wheel_tooth_number.setMinimumSize(QSize(400, 40))
        self.label_2nd_wheel_tooth_number.setMaximumSize(QSize(400, 16777215))
        self.label_2nd_wheel_tooth_number.setFont(font)

        self.horizontalLayout_39.addWidget(self.label_2nd_wheel_tooth_number)

        self.lineEdit_2nd_wheel_tooth_number = QLineEdit(self.frame_2md_wheel_tooth_number)
        self.lineEdit_2nd_wheel_tooth_number.setObjectName(u"lineEdit_2nd_wheel_tooth_number")
        self.lineEdit_2nd_wheel_tooth_number.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_2nd_wheel_tooth_number.sizePolicy().hasHeightForWidth())
        self.lineEdit_2nd_wheel_tooth_number.setSizePolicy(sizePolicy6)
        self.lineEdit_2nd_wheel_tooth_number.setMinimumSize(QSize(0, 40))
        self.lineEdit_2nd_wheel_tooth_number.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_2nd_wheel_tooth_number.setFont(font)
        self.lineEdit_2nd_wheel_tooth_number.setStyleSheet(u"margin: 10px;")
        self.lineEdit_2nd_wheel_tooth_number.setDragEnabled(False)
        self.lineEdit_2nd_wheel_tooth_number.setClearButtonEnabled(True)

        self.horizontalLayout_39.addWidget(self.lineEdit_2nd_wheel_tooth_number)

        self.second_wheel_tooth_number_confirm_btn = QPushButton(self.frame_2md_wheel_tooth_number)
        self.second_wheel_tooth_number_confirm_btn.setObjectName(u"second_wheel_tooth_number_confirm_btn")
        self.second_wheel_tooth_number_confirm_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 20;\n"
"margin-right: 10px;\n"
"padding: 0 5 0 5;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")

        self.horizontalLayout_39.addWidget(self.second_wheel_tooth_number_confirm_btn)


        self.verticalLayout_10.addWidget(self.frame_2md_wheel_tooth_number)

        self.frame_real_ratio = QFrame(self.frame_input_data_3)
        self.frame_real_ratio.setObjectName(u"frame_real_ratio")
        sizePolicy3.setHeightForWidth(self.frame_real_ratio.sizePolicy().hasHeightForWidth())
        self.frame_real_ratio.setSizePolicy(sizePolicy3)
        self.frame_real_ratio.setStyleSheet(u"")
        self.frame_real_ratio.setFrameShape(QFrame.StyledPanel)
        self.frame_real_ratio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_real_ratio)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_real_ratio = QLabel(self.frame_real_ratio)
        self.label_real_ratio.setObjectName(u"label_real_ratio")
        sizePolicy2.setHeightForWidth(self.label_real_ratio.sizePolicy().hasHeightForWidth())
        self.label_real_ratio.setSizePolicy(sizePolicy2)
        self.label_real_ratio.setMinimumSize(QSize(400, 40))
        self.label_real_ratio.setMaximumSize(QSize(400, 16777215))
        self.label_real_ratio.setFont(font)

        self.horizontalLayout_40.addWidget(self.label_real_ratio)

        self.lineEdit_real_ratio = QLineEdit(self.frame_real_ratio)
        self.lineEdit_real_ratio.setObjectName(u"lineEdit_real_ratio")
        self.lineEdit_real_ratio.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_real_ratio.sizePolicy().hasHeightForWidth())
        self.lineEdit_real_ratio.setSizePolicy(sizePolicy1)
        self.lineEdit_real_ratio.setMinimumSize(QSize(0, 40))
        self.lineEdit_real_ratio.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_real_ratio.setFont(font)
        self.lineEdit_real_ratio.setStyleSheet(u"margin: 10px;")
        self.lineEdit_real_ratio.setDragEnabled(False)
        self.lineEdit_real_ratio.setClearButtonEnabled(True)

        self.horizontalLayout_40.addWidget(self.lineEdit_real_ratio)


        self.verticalLayout_10.addWidget(self.frame_real_ratio)


        self.verticalLayout_9.addWidget(self.frame_input_data_3)


        self.verticalLayout_11.addWidget(self.page_preliminary_results_main_frame)

        self.stackedWidget.addWidget(self.page_preliminary_results)
        self.page_corection_factors = QWidget()
        self.page_corection_factors.setObjectName(u"page_corection_factors")
        self.verticalLayout_12 = QVBoxLayout(self.page_corection_factors)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.correction_factors_header_frame = QFrame(self.page_corection_factors)
        self.correction_factors_header_frame.setObjectName(u"correction_factors_header_frame")
        sizePolicy.setHeightForWidth(self.correction_factors_header_frame.sizePolicy().hasHeightForWidth())
        self.correction_factors_header_frame.setSizePolicy(sizePolicy)
        self.correction_factors_header_frame.setMaximumSize(QSize(16777215, 50))
        self.correction_factors_header_frame.setFont(font)
        self.correction_factors_header_frame.setFrameShape(QFrame.NoFrame)
        self.correction_factors_header_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.correction_factors_header_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.correction_factors_header_label = QLabel(self.correction_factors_header_frame)
        self.correction_factors_header_label.setObjectName(u"correction_factors_header_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.correction_factors_header_label.sizePolicy().hasHeightForWidth())
        self.correction_factors_header_label.setSizePolicy(sizePolicy7)
        self.correction_factors_header_label.setMinimumSize(QSize(260, 30))
        self.correction_factors_header_label.setMaximumSize(QSize(260, 30))
        self.correction_factors_header_label.setFont(font1)
        self.correction_factors_header_label.setTextFormat(Qt.PlainText)

        self.horizontalLayout_12.addWidget(self.correction_factors_header_label, 0, Qt.AlignHCenter)

        self.bring_back_defaults_btn = QPushButton(self.correction_factors_header_frame)
        self.bring_back_defaults_btn.setObjectName(u"bring_back_defaults_btn")
        self.bring_back_defaults_btn.setMaximumSize(QSize(150, 50))
        self.bring_back_defaults_btn.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 40;\n"
"margin: 10px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.bring_back_defaults_btn)


        self.verticalLayout_12.addWidget(self.correction_factors_header_frame)

        self.correction_factors_main_frame = QFrame(self.page_corection_factors)
        self.correction_factors_main_frame.setObjectName(u"correction_factors_main_frame")
        self.correction_factors_main_frame.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: 1px solid rgb(180,180,180);\n"
"padding-left: 3px;\n"
"color: rgb(33, 38, 55);\n"
"}\n"
"")
        self.correction_factors_main_frame.setFrameShape(QFrame.NoFrame)
        self.correction_factors_main_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.correction_factors_main_frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.graph_data_frame = QFrame(self.correction_factors_main_frame)
        self.graph_data_frame.setObjectName(u"graph_data_frame")
        sizePolicy3.setHeightForWidth(self.graph_data_frame.sizePolicy().hasHeightForWidth())
        self.graph_data_frame.setSizePolicy(sizePolicy3)
        self.graph_data_frame.setMinimumSize(QSize(0, 42))
        self.graph_data_frame.setMaximumSize(QSize(16777215, 42))
        self.graph_data_frame.setStyleSheet(u"QLabel{\n"
"padding-left: 5px;\n"
"}\n"
"QLineEdit{\n"
"margiin: 10px;\n"
"}\n"
"")
        self.graph_data_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_data_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.graph_data_frame)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(10, 0, 10, 0)
        self.factors_sum_frame = QLabel(self.graph_data_frame)
        self.factors_sum_frame.setObjectName(u"factors_sum_frame")
        sizePolicy4.setHeightForWidth(self.factors_sum_frame.sizePolicy().hasHeightForWidth())
        self.factors_sum_frame.setSizePolicy(sizePolicy4)
        self.factors_sum_frame.setMinimumSize(QSize(130, 0))
        self.factors_sum_frame.setMaximumSize(QSize(130, 16777215))
        self.factors_sum_frame.setFont(font)

        self.horizontalLayout_41.addWidget(self.factors_sum_frame)

        self.factors_sum_line_edit = QLineEdit(self.graph_data_frame)
        self.factors_sum_line_edit.setObjectName(u"factors_sum_line_edit")
        sizePolicy1.setHeightForWidth(self.factors_sum_line_edit.sizePolicy().hasHeightForWidth())
        self.factors_sum_line_edit.setSizePolicy(sizePolicy1)
        self.factors_sum_line_edit.setMinimumSize(QSize(0, 40))
        self.factors_sum_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.factors_sum_line_edit.setFont(font)
        self.factors_sum_line_edit.setStyleSheet(u"margin: 10px;\n"
"margin-right: 25px;")
        self.factors_sum_line_edit.setDragEnabled(False)
        self.factors_sum_line_edit.setClearButtonEnabled(True)

        self.horizontalLayout_41.addWidget(self.factors_sum_line_edit)

        self.tooth_number_sum_frame = QLabel(self.graph_data_frame)
        self.tooth_number_sum_frame.setObjectName(u"tooth_number_sum_frame")
        sizePolicy2.setHeightForWidth(self.tooth_number_sum_frame.sizePolicy().hasHeightForWidth())
        self.tooth_number_sum_frame.setSizePolicy(sizePolicy2)
        self.tooth_number_sum_frame.setMinimumSize(QSize(130, 0))
        self.tooth_number_sum_frame.setMaximumSize(QSize(130, 16777215))
        self.tooth_number_sum_frame.setFont(font)

        self.horizontalLayout_41.addWidget(self.tooth_number_sum_frame)

        self.tooth_number_sum_line_edit = QLineEdit(self.graph_data_frame)
        self.tooth_number_sum_line_edit.setObjectName(u"tooth_number_sum_line_edit")
        sizePolicy1.setHeightForWidth(self.tooth_number_sum_line_edit.sizePolicy().hasHeightForWidth())
        self.tooth_number_sum_line_edit.setSizePolicy(sizePolicy1)
        self.tooth_number_sum_line_edit.setMinimumSize(QSize(0, 40))
        self.tooth_number_sum_line_edit.setMaximumSize(QSize(16777215, 16777215))
        self.tooth_number_sum_line_edit.setFont(font)
        self.tooth_number_sum_line_edit.setStyleSheet(u"margin: 10px;")
        self.tooth_number_sum_line_edit.setDragEnabled(False)
        self.tooth_number_sum_line_edit.setClearButtonEnabled(True)

        self.horizontalLayout_41.addWidget(self.tooth_number_sum_line_edit)


        self.verticalLayout_13.addWidget(self.graph_data_frame)

        self.graph_frame = QFrame(self.correction_factors_main_frame)
        self.graph_frame.setObjectName(u"graph_frame")
        self.graph_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.graph_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.graph_generate_button = QPushButton(self.graph_frame)
        self.graph_generate_button.setObjectName(u"graph_generate_button")
        sizePolicy7.setHeightForWidth(self.graph_generate_button.sizePolicy().hasHeightForWidth())
        self.graph_generate_button.setSizePolicy(sizePolicy7)
        self.graph_generate_button.setMinimumSize(QSize(100, 0))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.graph_generate_button.setFont(font3)
        self.graph_generate_button.setAcceptDrops(True)
        self.graph_generate_button.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"height: 40;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.graph_generate_button)

        self.MplWidget = MplWidget(self.graph_frame)
        self.MplWidget.setObjectName(u"MplWidget")
        font4 = QFont()
        font4.setFamily(u"MS Serif")
        font4.setBold(False)
        font4.setWeight(50)
        self.MplWidget.setFont(font4)
        #self.MplWidget.setFrameShape(QFrame.StyledPanel)
        #self.MplWidget.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.MplWidget)


        self.verticalLayout_13.addWidget(self.graph_frame)


        self.verticalLayout_12.addWidget(self.correction_factors_main_frame)

        self.stackedWidget.addWidget(self.page_corection_factors)
        self.page_outcomes = QWidget()
        self.page_outcomes.setObjectName(u"page_outcomes")
        self.verticalLayout_14 = QVBoxLayout(self.page_outcomes)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame = QFrame(self.page_outcomes)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_preconditions_3 = QFrame(self.frame)
        self.frame_preconditions_3.setObjectName(u"frame_preconditions_3")
        sizePolicy.setHeightForWidth(self.frame_preconditions_3.sizePolicy().hasHeightForWidth())
        self.frame_preconditions_3.setSizePolicy(sizePolicy)
        self.frame_preconditions_3.setMaximumSize(QSize(16777215, 50))
        self.frame_preconditions_3.setFont(font)
        self.frame_preconditions_3.setFrameShape(QFrame.NoFrame)
        self.frame_preconditions_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_preconditions_3)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_preconditions_3 = QLabel(self.frame_preconditions_3)
        self.label_preconditions_3.setObjectName(u"label_preconditions_3")
        sizePolicy2.setHeightForWidth(self.label_preconditions_3.sizePolicy().hasHeightForWidth())
        self.label_preconditions_3.setSizePolicy(sizePolicy2)
        self.label_preconditions_3.setMinimumSize(QSize(50, 30))
        self.label_preconditions_3.setMaximumSize(QSize(75, 30))
        self.label_preconditions_3.setFont(font1)
        self.label_preconditions_3.setFrameShape(QFrame.NoFrame)
        self.label_preconditions_3.setTextFormat(Qt.PlainText)

        self.horizontalLayout_14.addWidget(self.label_preconditions_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.frame_preconditions_3)


        self.verticalLayout_14.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.page_outcomes)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical\n"
"    {\n"
"		background-color: rgb(76, 118, 232);\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"QScrollBar::handle:vertical\n"
"    {\n"
"		background-color: rgb(51, 82, 148);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"QScrollBar::handle:vertical:hover\n"
"    {\n"
"        background-color: rgb(41, 72, 138);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
""
                        "        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 786, 1212))
        self.scrollAreaWidgetContents.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(242, 242, 246);\n"
"border: 1px solid rgb(180,180,180);padding-left: 3px;\n"
"color: rgb(33, 38, 55);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_wheelbase_zero = QFrame(self.scrollAreaWidgetContents)
        self.frame_wheelbase_zero.setObjectName(u"frame_wheelbase_zero")
        sizePolicy3.setHeightForWidth(self.frame_wheelbase_zero.sizePolicy().hasHeightForWidth())
        self.frame_wheelbase_zero.setSizePolicy(sizePolicy3)
        self.frame_wheelbase_zero.setMinimumSize(QSize(0, 42))
        self.frame_wheelbase_zero.setMaximumSize(QSize(16777215, 42))
        self.frame_wheelbase_zero.setStyleSheet(u"")
        self.frame_wheelbase_zero.setFrameShape(QFrame.StyledPanel)
        self.frame_wheelbase_zero.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_wheelbase_zero)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_wheelbase_zero = QLabel(self.frame_wheelbase_zero)
        self.label_wheelbase_zero.setObjectName(u"label_wheelbase_zero")
        sizePolicy2.setHeightForWidth(self.label_wheelbase_zero.sizePolicy().hasHeightForWidth())
        self.label_wheelbase_zero.setSizePolicy(sizePolicy2)
        self.label_wheelbase_zero.setMinimumSize(QSize(400, 0))
        self.label_wheelbase_zero.setMaximumSize(QSize(400, 16777215))
        self.label_wheelbase_zero.setFont(font)

        self.horizontalLayout_54.addWidget(self.label_wheelbase_zero)

        self.lineEdit_wheelbase_zero = QLineEdit(self.frame_wheelbase_zero)
        self.lineEdit_wheelbase_zero.setObjectName(u"lineEdit_wheelbase_zero")
        self.lineEdit_wheelbase_zero.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_wheelbase_zero.sizePolicy().hasHeightForWidth())
        self.lineEdit_wheelbase_zero.setSizePolicy(sizePolicy1)
        self.lineEdit_wheelbase_zero.setMinimumSize(QSize(0, 40))
        self.lineEdit_wheelbase_zero.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_wheelbase_zero.setFont(font)
        self.lineEdit_wheelbase_zero.setStyleSheet(u"margin: 10px;")
        self.lineEdit_wheelbase_zero.setDragEnabled(False)
        self.lineEdit_wheelbase_zero.setClearButtonEnabled(True)

        self.horizontalLayout_54.addWidget(self.lineEdit_wheelbase_zero)


        self.verticalLayout_15.addWidget(self.frame_wheelbase_zero)

        self.frame_estimated_correction_factors_sum = QFrame(self.scrollAreaWidgetContents)
        self.frame_estimated_correction_factors_sum.setObjectName(u"frame_estimated_correction_factors_sum")
        sizePolicy3.setHeightForWidth(self.frame_estimated_correction_factors_sum.sizePolicy().hasHeightForWidth())
        self.frame_estimated_correction_factors_sum.setSizePolicy(sizePolicy3)
        self.frame_estimated_correction_factors_sum.setMinimumSize(QSize(0, 42))
        self.frame_estimated_correction_factors_sum.setMaximumSize(QSize(16777215, 42))
        self.frame_estimated_correction_factors_sum.setStyleSheet(u"")
        self.frame_estimated_correction_factors_sum.setFrameShape(QFrame.StyledPanel)
        self.frame_estimated_correction_factors_sum.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_estimated_correction_factors_sum)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_estimated_correction_factors_sum = QLabel(self.frame_estimated_correction_factors_sum)
        self.label_estimated_correction_factors_sum.setObjectName(u"label_estimated_correction_factors_sum")
        sizePolicy2.setHeightForWidth(self.label_estimated_correction_factors_sum.sizePolicy().hasHeightForWidth())
        self.label_estimated_correction_factors_sum.setSizePolicy(sizePolicy2)
        self.label_estimated_correction_factors_sum.setMinimumSize(QSize(400, 0))
        self.label_estimated_correction_factors_sum.setMaximumSize(QSize(400, 16777215))
        self.label_estimated_correction_factors_sum.setFont(font)

        self.horizontalLayout_53.addWidget(self.label_estimated_correction_factors_sum)

        self.lineEdit_estimated_correction_factors_sum = QLineEdit(self.frame_estimated_correction_factors_sum)
        self.lineEdit_estimated_correction_factors_sum.setObjectName(u"lineEdit_estimated_correction_factors_sum")
        self.lineEdit_estimated_correction_factors_sum.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_estimated_correction_factors_sum.sizePolicy().hasHeightForWidth())
        self.lineEdit_estimated_correction_factors_sum.setSizePolicy(sizePolicy1)
        self.lineEdit_estimated_correction_factors_sum.setMinimumSize(QSize(0, 40))
        self.lineEdit_estimated_correction_factors_sum.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_estimated_correction_factors_sum.setFont(font)
        self.lineEdit_estimated_correction_factors_sum.setStyleSheet(u"margin: 10px;")
        self.lineEdit_estimated_correction_factors_sum.setDragEnabled(False)
        self.lineEdit_estimated_correction_factors_sum.setClearButtonEnabled(True)

        self.horizontalLayout_53.addWidget(self.lineEdit_estimated_correction_factors_sum)


        self.verticalLayout_15.addWidget(self.frame_estimated_correction_factors_sum)

        self.frame_alfa_t = QFrame(self.scrollAreaWidgetContents)
        self.frame_alfa_t.setObjectName(u"frame_alfa_t")
        sizePolicy3.setHeightForWidth(self.frame_alfa_t.sizePolicy().hasHeightForWidth())
        self.frame_alfa_t.setSizePolicy(sizePolicy3)
        self.frame_alfa_t.setMinimumSize(QSize(0, 42))
        self.frame_alfa_t.setMaximumSize(QSize(16777215, 42))
        self.frame_alfa_t.setStyleSheet(u"")
        self.frame_alfa_t.setFrameShape(QFrame.StyledPanel)
        self.frame_alfa_t.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_alfa_t)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_alfa_t = QLabel(self.frame_alfa_t)
        self.label_alfa_t.setObjectName(u"label_alfa_t")
        sizePolicy2.setHeightForWidth(self.label_alfa_t.sizePolicy().hasHeightForWidth())
        self.label_alfa_t.setSizePolicy(sizePolicy2)
        self.label_alfa_t.setMinimumSize(QSize(400, 0))
        self.label_alfa_t.setMaximumSize(QSize(400, 16777215))
        self.label_alfa_t.setFont(font)

        self.horizontalLayout_52.addWidget(self.label_alfa_t)

        self.lineEdit_alfa_t = QLineEdit(self.frame_alfa_t)
        self.lineEdit_alfa_t.setObjectName(u"lineEdit_alfa_t")
        self.lineEdit_alfa_t.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_alfa_t.sizePolicy().hasHeightForWidth())
        self.lineEdit_alfa_t.setSizePolicy(sizePolicy1)
        self.lineEdit_alfa_t.setMinimumSize(QSize(0, 40))
        self.lineEdit_alfa_t.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_alfa_t.setFont(font)
        self.lineEdit_alfa_t.setStyleSheet(u"margin: 10px;")
        self.lineEdit_alfa_t.setDragEnabled(False)
        self.lineEdit_alfa_t.setClearButtonEnabled(True)

        self.horizontalLayout_52.addWidget(self.lineEdit_alfa_t)


        self.verticalLayout_15.addWidget(self.frame_alfa_t)

        self.frame_alfa_tw = QFrame(self.scrollAreaWidgetContents)
        self.frame_alfa_tw.setObjectName(u"frame_alfa_tw")
        sizePolicy3.setHeightForWidth(self.frame_alfa_tw.sizePolicy().hasHeightForWidth())
        self.frame_alfa_tw.setSizePolicy(sizePolicy3)
        self.frame_alfa_tw.setMinimumSize(QSize(0, 42))
        self.frame_alfa_tw.setMaximumSize(QSize(16777215, 42))
        self.frame_alfa_tw.setStyleSheet(u"")
        self.frame_alfa_tw.setFrameShape(QFrame.StyledPanel)
        self.frame_alfa_tw.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_alfa_tw)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_alfa_tw = QLabel(self.frame_alfa_tw)
        self.label_alfa_tw.setObjectName(u"label_alfa_tw")
        sizePolicy2.setHeightForWidth(self.label_alfa_tw.sizePolicy().hasHeightForWidth())
        self.label_alfa_tw.setSizePolicy(sizePolicy2)
        self.label_alfa_tw.setMinimumSize(QSize(400, 0))
        self.label_alfa_tw.setMaximumSize(QSize(400, 16777215))
        self.label_alfa_tw.setFont(font)

        self.horizontalLayout_51.addWidget(self.label_alfa_tw)

        self.lineEdit_alfa_tw = QLineEdit(self.frame_alfa_tw)
        self.lineEdit_alfa_tw.setObjectName(u"lineEdit_alfa_tw")
        self.lineEdit_alfa_tw.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_alfa_tw.sizePolicy().hasHeightForWidth())
        self.lineEdit_alfa_tw.setSizePolicy(sizePolicy1)
        self.lineEdit_alfa_tw.setMinimumSize(QSize(0, 40))
        self.lineEdit_alfa_tw.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_alfa_tw.setFont(font)
        self.lineEdit_alfa_tw.setStyleSheet(u"margin: 10px;")
        self.lineEdit_alfa_tw.setDragEnabled(False)
        self.lineEdit_alfa_tw.setClearButtonEnabled(True)

        self.horizontalLayout_51.addWidget(self.lineEdit_alfa_tw)


        self.verticalLayout_15.addWidget(self.frame_alfa_tw)

        self.frame_inv_alfa_tw = QFrame(self.scrollAreaWidgetContents)
        self.frame_inv_alfa_tw.setObjectName(u"frame_inv_alfa_tw")
        sizePolicy3.setHeightForWidth(self.frame_inv_alfa_tw.sizePolicy().hasHeightForWidth())
        self.frame_inv_alfa_tw.setSizePolicy(sizePolicy3)
        self.frame_inv_alfa_tw.setMinimumSize(QSize(0, 42))
        self.frame_inv_alfa_tw.setMaximumSize(QSize(16777215, 42))
        self.frame_inv_alfa_tw.setStyleSheet(u"")
        self.frame_inv_alfa_tw.setFrameShape(QFrame.StyledPanel)
        self.frame_inv_alfa_tw.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_inv_alfa_tw)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_inv_alfa_tw = QLabel(self.frame_inv_alfa_tw)
        self.label_inv_alfa_tw.setObjectName(u"label_inv_alfa_tw")
        sizePolicy2.setHeightForWidth(self.label_inv_alfa_tw.sizePolicy().hasHeightForWidth())
        self.label_inv_alfa_tw.setSizePolicy(sizePolicy2)
        self.label_inv_alfa_tw.setMinimumSize(QSize(400, 0))
        self.label_inv_alfa_tw.setMaximumSize(QSize(400, 16777215))
        self.label_inv_alfa_tw.setFont(font)

        self.horizontalLayout_50.addWidget(self.label_inv_alfa_tw)

        self.lineEdit_inv_alfa_tw = QLineEdit(self.frame_inv_alfa_tw)
        self.lineEdit_inv_alfa_tw.setObjectName(u"lineEdit_inv_alfa_tw")
        self.lineEdit_inv_alfa_tw.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_inv_alfa_tw.sizePolicy().hasHeightForWidth())
        self.lineEdit_inv_alfa_tw.setSizePolicy(sizePolicy1)
        self.lineEdit_inv_alfa_tw.setMinimumSize(QSize(0, 40))
        self.lineEdit_inv_alfa_tw.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_inv_alfa_tw.setFont(font)
        self.lineEdit_inv_alfa_tw.setStyleSheet(u"margin: 10px;")
        self.lineEdit_inv_alfa_tw.setDragEnabled(False)
        self.lineEdit_inv_alfa_tw.setClearButtonEnabled(True)

        self.horizontalLayout_50.addWidget(self.lineEdit_inv_alfa_tw)


        self.verticalLayout_15.addWidget(self.frame_inv_alfa_tw)

        self.frame_inv_alfa_t = QFrame(self.scrollAreaWidgetContents)
        self.frame_inv_alfa_t.setObjectName(u"frame_inv_alfa_t")
        sizePolicy3.setHeightForWidth(self.frame_inv_alfa_t.sizePolicy().hasHeightForWidth())
        self.frame_inv_alfa_t.setSizePolicy(sizePolicy3)
        self.frame_inv_alfa_t.setMinimumSize(QSize(0, 42))
        self.frame_inv_alfa_t.setMaximumSize(QSize(16777215, 42))
        self.frame_inv_alfa_t.setStyleSheet(u"")
        self.frame_inv_alfa_t.setFrameShape(QFrame.StyledPanel)
        self.frame_inv_alfa_t.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_inv_alfa_t)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_inv_alfa_t = QLabel(self.frame_inv_alfa_t)
        self.label_inv_alfa_t.setObjectName(u"label_inv_alfa_t")
        sizePolicy2.setHeightForWidth(self.label_inv_alfa_t.sizePolicy().hasHeightForWidth())
        self.label_inv_alfa_t.setSizePolicy(sizePolicy2)
        self.label_inv_alfa_t.setMinimumSize(QSize(400, 0))
        self.label_inv_alfa_t.setMaximumSize(QSize(400, 16777215))
        self.label_inv_alfa_t.setFont(font)

        self.horizontalLayout_47.addWidget(self.label_inv_alfa_t)

        self.lineEdit_inv_alfa_t = QLineEdit(self.frame_inv_alfa_t)
        self.lineEdit_inv_alfa_t.setObjectName(u"lineEdit_inv_alfa_t")
        self.lineEdit_inv_alfa_t.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_inv_alfa_t.sizePolicy().hasHeightForWidth())
        self.lineEdit_inv_alfa_t.setSizePolicy(sizePolicy1)
        self.lineEdit_inv_alfa_t.setMinimumSize(QSize(0, 40))
        self.lineEdit_inv_alfa_t.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_inv_alfa_t.setFont(font)
        self.lineEdit_inv_alfa_t.setStyleSheet(u"margin: 10px;")
        self.lineEdit_inv_alfa_t.setDragEnabled(False)
        self.lineEdit_inv_alfa_t.setClearButtonEnabled(True)

        self.horizontalLayout_47.addWidget(self.lineEdit_inv_alfa_t)


        self.verticalLayout_15.addWidget(self.frame_inv_alfa_t)

        self.frame_correction_factors_sum = QFrame(self.scrollAreaWidgetContents)
        self.frame_correction_factors_sum.setObjectName(u"frame_correction_factors_sum")
        sizePolicy3.setHeightForWidth(self.frame_correction_factors_sum.sizePolicy().hasHeightForWidth())
        self.frame_correction_factors_sum.setSizePolicy(sizePolicy3)
        self.frame_correction_factors_sum.setMinimumSize(QSize(0, 42))
        self.frame_correction_factors_sum.setMaximumSize(QSize(16777215, 42))
        self.frame_correction_factors_sum.setStyleSheet(u"")
        self.frame_correction_factors_sum.setFrameShape(QFrame.StyledPanel)
        self.frame_correction_factors_sum.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_correction_factors_sum)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_correction_factors_sum = QLabel(self.frame_correction_factors_sum)
        self.label_correction_factors_sum.setObjectName(u"label_correction_factors_sum")
        sizePolicy2.setHeightForWidth(self.label_correction_factors_sum.sizePolicy().hasHeightForWidth())
        self.label_correction_factors_sum.setSizePolicy(sizePolicy2)
        self.label_correction_factors_sum.setMinimumSize(QSize(400, 0))
        self.label_correction_factors_sum.setMaximumSize(QSize(400, 16777215))
        self.label_correction_factors_sum.setFont(font)

        self.horizontalLayout_46.addWidget(self.label_correction_factors_sum)

        self.lineEdit_correction_factors_sum = QLineEdit(self.frame_correction_factors_sum)
        self.lineEdit_correction_factors_sum.setObjectName(u"lineEdit_correction_factors_sum")
        self.lineEdit_correction_factors_sum.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_correction_factors_sum.sizePolicy().hasHeightForWidth())
        self.lineEdit_correction_factors_sum.setSizePolicy(sizePolicy1)
        self.lineEdit_correction_factors_sum.setMinimumSize(QSize(0, 40))
        self.lineEdit_correction_factors_sum.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_correction_factors_sum.setFont(font)
        self.lineEdit_correction_factors_sum.setStyleSheet(u"margin: 10px;")
        self.lineEdit_correction_factors_sum.setDragEnabled(False)
        self.lineEdit_correction_factors_sum.setClearButtonEnabled(True)

        self.horizontalLayout_46.addWidget(self.lineEdit_correction_factors_sum)


        self.verticalLayout_15.addWidget(self.frame_correction_factors_sum)

        self.frame_beta_b_helix_angle = QFrame(self.scrollAreaWidgetContents)
        self.frame_beta_b_helix_angle.setObjectName(u"frame_beta_b_helix_angle")
        sizePolicy3.setHeightForWidth(self.frame_beta_b_helix_angle.sizePolicy().hasHeightForWidth())
        self.frame_beta_b_helix_angle.setSizePolicy(sizePolicy3)
        self.frame_beta_b_helix_angle.setMinimumSize(QSize(0, 42))
        self.frame_beta_b_helix_angle.setMaximumSize(QSize(16777215, 42))
        self.frame_beta_b_helix_angle.setStyleSheet(u"")
        self.frame_beta_b_helix_angle.setFrameShape(QFrame.StyledPanel)
        self.frame_beta_b_helix_angle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_beta_b_helix_angle)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_beta_b_helix_angle = QLabel(self.frame_beta_b_helix_angle)
        self.label_beta_b_helix_angle.setObjectName(u"label_beta_b_helix_angle")
        sizePolicy2.setHeightForWidth(self.label_beta_b_helix_angle.sizePolicy().hasHeightForWidth())
        self.label_beta_b_helix_angle.setSizePolicy(sizePolicy2)
        self.label_beta_b_helix_angle.setMinimumSize(QSize(400, 0))
        self.label_beta_b_helix_angle.setMaximumSize(QSize(400, 16777215))
        self.label_beta_b_helix_angle.setFont(font)

        self.horizontalLayout_45.addWidget(self.label_beta_b_helix_angle)

        self.lineEdit_beta_b_helix_angle = QLineEdit(self.frame_beta_b_helix_angle)
        self.lineEdit_beta_b_helix_angle.setObjectName(u"lineEdit_beta_b_helix_angle")
        self.lineEdit_beta_b_helix_angle.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_beta_b_helix_angle.sizePolicy().hasHeightForWidth())
        self.lineEdit_beta_b_helix_angle.setSizePolicy(sizePolicy1)
        self.lineEdit_beta_b_helix_angle.setMinimumSize(QSize(0, 40))
        self.lineEdit_beta_b_helix_angle.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_beta_b_helix_angle.setFont(font)
        self.lineEdit_beta_b_helix_angle.setStyleSheet(u"margin: 10px;")
        self.lineEdit_beta_b_helix_angle.setDragEnabled(False)
        self.lineEdit_beta_b_helix_angle.setClearButtonEnabled(True)

        self.horizontalLayout_45.addWidget(self.lineEdit_beta_b_helix_angle)


        self.verticalLayout_15.addWidget(self.frame_beta_b_helix_angle)

        self.frame_pinion_tooth_number_placeholder = QFrame(self.scrollAreaWidgetContents)
        self.frame_pinion_tooth_number_placeholder.setObjectName(u"frame_pinion_tooth_number_placeholder")
        sizePolicy3.setHeightForWidth(self.frame_pinion_tooth_number_placeholder.sizePolicy().hasHeightForWidth())
        self.frame_pinion_tooth_number_placeholder.setSizePolicy(sizePolicy3)
        self.frame_pinion_tooth_number_placeholder.setMinimumSize(QSize(0, 42))
        self.frame_pinion_tooth_number_placeholder.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_tooth_number_placeholder.setStyleSheet(u"")
        self.frame_pinion_tooth_number_placeholder.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_tooth_number_placeholder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_pinion_tooth_number_placeholder)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_tooth_number_placeholder = QLabel(self.frame_pinion_tooth_number_placeholder)
        self.label_pinion_tooth_number_placeholder.setObjectName(u"label_pinion_tooth_number_placeholder")
        sizePolicy2.setHeightForWidth(self.label_pinion_tooth_number_placeholder.sizePolicy().hasHeightForWidth())
        self.label_pinion_tooth_number_placeholder.setSizePolicy(sizePolicy2)
        self.label_pinion_tooth_number_placeholder.setMinimumSize(QSize(400, 0))
        self.label_pinion_tooth_number_placeholder.setMaximumSize(QSize(400, 16777215))
        self.label_pinion_tooth_number_placeholder.setFont(font)

        self.horizontalLayout_44.addWidget(self.label_pinion_tooth_number_placeholder)

        self.lineEdit_pinion_tooth_number_placeholder = QLineEdit(self.frame_pinion_tooth_number_placeholder)
        self.lineEdit_pinion_tooth_number_placeholder.setObjectName(u"lineEdit_pinion_tooth_number_placeholder")
        self.lineEdit_pinion_tooth_number_placeholder.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_pinion_tooth_number_placeholder.sizePolicy().hasHeightForWidth())
        self.lineEdit_pinion_tooth_number_placeholder.setSizePolicy(sizePolicy1)
        self.lineEdit_pinion_tooth_number_placeholder.setMinimumSize(QSize(0, 40))
        self.lineEdit_pinion_tooth_number_placeholder.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pinion_tooth_number_placeholder.setFont(font)
        self.lineEdit_pinion_tooth_number_placeholder.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pinion_tooth_number_placeholder.setDragEnabled(False)
        self.lineEdit_pinion_tooth_number_placeholder.setClearButtonEnabled(True)

        self.horizontalLayout_44.addWidget(self.lineEdit_pinion_tooth_number_placeholder)


        self.verticalLayout_15.addWidget(self.frame_pinion_tooth_number_placeholder)

        self.frame_second_wheel_tooth_number_placeholder = QFrame(self.scrollAreaWidgetContents)
        self.frame_second_wheel_tooth_number_placeholder.setObjectName(u"frame_second_wheel_tooth_number_placeholder")
        sizePolicy3.setHeightForWidth(self.frame_second_wheel_tooth_number_placeholder.sizePolicy().hasHeightForWidth())
        self.frame_second_wheel_tooth_number_placeholder.setSizePolicy(sizePolicy3)
        self.frame_second_wheel_tooth_number_placeholder.setMinimumSize(QSize(0, 42))
        self.frame_second_wheel_tooth_number_placeholder.setMaximumSize(QSize(16777215, 42))
        self.frame_second_wheel_tooth_number_placeholder.setStyleSheet(u"")
        self.frame_second_wheel_tooth_number_placeholder.setFrameShape(QFrame.StyledPanel)
        self.frame_second_wheel_tooth_number_placeholder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_second_wheel_tooth_number_placeholder)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_second_wheel_tooth_number_placeholder = QLabel(self.frame_second_wheel_tooth_number_placeholder)
        self.label_second_wheel_tooth_number_placeholder.setObjectName(u"label_second_wheel_tooth_number_placeholder")
        sizePolicy2.setHeightForWidth(self.label_second_wheel_tooth_number_placeholder.sizePolicy().hasHeightForWidth())
        self.label_second_wheel_tooth_number_placeholder.setSizePolicy(sizePolicy2)
        self.label_second_wheel_tooth_number_placeholder.setMinimumSize(QSize(400, 0))
        self.label_second_wheel_tooth_number_placeholder.setMaximumSize(QSize(400, 16777215))
        self.label_second_wheel_tooth_number_placeholder.setFont(font)

        self.horizontalLayout_43.addWidget(self.label_second_wheel_tooth_number_placeholder)

        self.lineEdit_second_wheel_tooth_number_placeholder = QLineEdit(self.frame_second_wheel_tooth_number_placeholder)
        self.lineEdit_second_wheel_tooth_number_placeholder.setObjectName(u"lineEdit_second_wheel_tooth_number_placeholder")
        self.lineEdit_second_wheel_tooth_number_placeholder.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_second_wheel_tooth_number_placeholder.sizePolicy().hasHeightForWidth())
        self.lineEdit_second_wheel_tooth_number_placeholder.setSizePolicy(sizePolicy1)
        self.lineEdit_second_wheel_tooth_number_placeholder.setMinimumSize(QSize(0, 40))
        self.lineEdit_second_wheel_tooth_number_placeholder.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_second_wheel_tooth_number_placeholder.setFont(font)
        self.lineEdit_second_wheel_tooth_number_placeholder.setStyleSheet(u"margin: 10px;")
        self.lineEdit_second_wheel_tooth_number_placeholder.setDragEnabled(False)
        self.lineEdit_second_wheel_tooth_number_placeholder.setClearButtonEnabled(True)

        self.horizontalLayout_43.addWidget(self.lineEdit_second_wheel_tooth_number_placeholder)


        self.verticalLayout_15.addWidget(self.frame_second_wheel_tooth_number_placeholder)

        self.frame_pinion_correction_factor = QFrame(self.scrollAreaWidgetContents)
        self.frame_pinion_correction_factor.setObjectName(u"frame_pinion_correction_factor")
        sizePolicy3.setHeightForWidth(self.frame_pinion_correction_factor.sizePolicy().hasHeightForWidth())
        self.frame_pinion_correction_factor.setSizePolicy(sizePolicy3)
        self.frame_pinion_correction_factor.setMinimumSize(QSize(0, 42))
        self.frame_pinion_correction_factor.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_correction_factor.setStyleSheet(u"")
        self.frame_pinion_correction_factor.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_correction_factor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_pinion_correction_factor)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_correction_factor = QLabel(self.frame_pinion_correction_factor)
        self.label_pinion_correction_factor.setObjectName(u"label_pinion_correction_factor")
        sizePolicy2.setHeightForWidth(self.label_pinion_correction_factor.sizePolicy().hasHeightForWidth())
        self.label_pinion_correction_factor.setSizePolicy(sizePolicy2)
        self.label_pinion_correction_factor.setMinimumSize(QSize(400, 0))
        self.label_pinion_correction_factor.setMaximumSize(QSize(400, 16777215))
        self.label_pinion_correction_factor.setFont(font)

        self.horizontalLayout_61.addWidget(self.label_pinion_correction_factor)

        self.lineEdit_pinion_correction_factor = QLineEdit(self.frame_pinion_correction_factor)
        self.lineEdit_pinion_correction_factor.setObjectName(u"lineEdit_pinion_correction_factor")
        self.lineEdit_pinion_correction_factor.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_pinion_correction_factor.sizePolicy().hasHeightForWidth())
        self.lineEdit_pinion_correction_factor.setSizePolicy(sizePolicy1)
        self.lineEdit_pinion_correction_factor.setMinimumSize(QSize(0, 40))
        self.lineEdit_pinion_correction_factor.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pinion_correction_factor.setFont(font)
        self.lineEdit_pinion_correction_factor.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pinion_correction_factor.setDragEnabled(False)
        self.lineEdit_pinion_correction_factor.setClearButtonEnabled(True)

        self.horizontalLayout_61.addWidget(self.lineEdit_pinion_correction_factor)


        self.verticalLayout_15.addWidget(self.frame_pinion_correction_factor)

        self.frame_second_wheel_correction_factor = QFrame(self.scrollAreaWidgetContents)
        self.frame_second_wheel_correction_factor.setObjectName(u"frame_second_wheel_correction_factor")
        sizePolicy3.setHeightForWidth(self.frame_second_wheel_correction_factor.sizePolicy().hasHeightForWidth())
        self.frame_second_wheel_correction_factor.setSizePolicy(sizePolicy3)
        self.frame_second_wheel_correction_factor.setMinimumSize(QSize(0, 42))
        self.frame_second_wheel_correction_factor.setMaximumSize(QSize(16777215, 42))
        self.frame_second_wheel_correction_factor.setStyleSheet(u"")
        self.frame_second_wheel_correction_factor.setFrameShape(QFrame.StyledPanel)
        self.frame_second_wheel_correction_factor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_second_wheel_correction_factor)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_second_wheel_correction_factor = QLabel(self.frame_second_wheel_correction_factor)
        self.label_second_wheel_correction_factor.setObjectName(u"label_second_wheel_correction_factor")
        sizePolicy2.setHeightForWidth(self.label_second_wheel_correction_factor.sizePolicy().hasHeightForWidth())
        self.label_second_wheel_correction_factor.setSizePolicy(sizePolicy2)
        self.label_second_wheel_correction_factor.setMinimumSize(QSize(400, 0))
        self.label_second_wheel_correction_factor.setMaximumSize(QSize(400, 16777215))
        self.label_second_wheel_correction_factor.setFont(font)

        self.horizontalLayout_60.addWidget(self.label_second_wheel_correction_factor)

        self.lineEdit_second_wheel_correction_factor = QLineEdit(self.frame_second_wheel_correction_factor)
        self.lineEdit_second_wheel_correction_factor.setObjectName(u"lineEdit_second_wheel_correction_factor")
        self.lineEdit_second_wheel_correction_factor.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_second_wheel_correction_factor.sizePolicy().hasHeightForWidth())
        self.lineEdit_second_wheel_correction_factor.setSizePolicy(sizePolicy1)
        self.lineEdit_second_wheel_correction_factor.setMinimumSize(QSize(0, 40))
        self.lineEdit_second_wheel_correction_factor.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_second_wheel_correction_factor.setFont(font)
        self.lineEdit_second_wheel_correction_factor.setStyleSheet(u"margin: 10px;")
        self.lineEdit_second_wheel_correction_factor.setDragEnabled(False)
        self.lineEdit_second_wheel_correction_factor.setClearButtonEnabled(True)

        self.horizontalLayout_60.addWidget(self.lineEdit_second_wheel_correction_factor)


        self.verticalLayout_15.addWidget(self.frame_second_wheel_correction_factor)

        self.frame_pinion_rolling_diameter = QFrame(self.scrollAreaWidgetContents)
        self.frame_pinion_rolling_diameter.setObjectName(u"frame_pinion_rolling_diameter")
        sizePolicy3.setHeightForWidth(self.frame_pinion_rolling_diameter.sizePolicy().hasHeightForWidth())
        self.frame_pinion_rolling_diameter.setSizePolicy(sizePolicy3)
        self.frame_pinion_rolling_diameter.setMinimumSize(QSize(0, 42))
        self.frame_pinion_rolling_diameter.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_rolling_diameter.setStyleSheet(u"")
        self.frame_pinion_rolling_diameter.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_rolling_diameter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_pinion_rolling_diameter)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_rolling_diameter = QLabel(self.frame_pinion_rolling_diameter)
        self.label_pinion_rolling_diameter.setObjectName(u"label_pinion_rolling_diameter")
        sizePolicy2.setHeightForWidth(self.label_pinion_rolling_diameter.sizePolicy().hasHeightForWidth())
        self.label_pinion_rolling_diameter.setSizePolicy(sizePolicy2)
        self.label_pinion_rolling_diameter.setMinimumSize(QSize(400, 0))
        self.label_pinion_rolling_diameter.setMaximumSize(QSize(400, 16777215))
        self.label_pinion_rolling_diameter.setFont(font)

        self.horizontalLayout_59.addWidget(self.label_pinion_rolling_diameter)

        self.lineEdit_pinion_rolling_diameter = QLineEdit(self.frame_pinion_rolling_diameter)
        self.lineEdit_pinion_rolling_diameter.setObjectName(u"lineEdit_pinion_rolling_diameter")
        self.lineEdit_pinion_rolling_diameter.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_pinion_rolling_diameter.sizePolicy().hasHeightForWidth())
        self.lineEdit_pinion_rolling_diameter.setSizePolicy(sizePolicy1)
        self.lineEdit_pinion_rolling_diameter.setMinimumSize(QSize(0, 40))
        self.lineEdit_pinion_rolling_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pinion_rolling_diameter.setFont(font)
        self.lineEdit_pinion_rolling_diameter.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pinion_rolling_diameter.setDragEnabled(False)
        self.lineEdit_pinion_rolling_diameter.setClearButtonEnabled(True)

        self.horizontalLayout_59.addWidget(self.lineEdit_pinion_rolling_diameter)


        self.verticalLayout_15.addWidget(self.frame_pinion_rolling_diameter)

        self.frame_second_wheel_rolling_diameter = QFrame(self.scrollAreaWidgetContents)
        self.frame_second_wheel_rolling_diameter.setObjectName(u"frame_second_wheel_rolling_diameter")
        sizePolicy3.setHeightForWidth(self.frame_second_wheel_rolling_diameter.sizePolicy().hasHeightForWidth())
        self.frame_second_wheel_rolling_diameter.setSizePolicy(sizePolicy3)
        self.frame_second_wheel_rolling_diameter.setMinimumSize(QSize(0, 42))
        self.frame_second_wheel_rolling_diameter.setMaximumSize(QSize(16777215, 42))
        self.frame_second_wheel_rolling_diameter.setStyleSheet(u"")
        self.frame_second_wheel_rolling_diameter.setFrameShape(QFrame.StyledPanel)
        self.frame_second_wheel_rolling_diameter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_second_wheel_rolling_diameter)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_second_wheel_rolling_diameter = QLabel(self.frame_second_wheel_rolling_diameter)
        self.label_second_wheel_rolling_diameter.setObjectName(u"label_second_wheel_rolling_diameter")
        sizePolicy2.setHeightForWidth(self.label_second_wheel_rolling_diameter.sizePolicy().hasHeightForWidth())
        self.label_second_wheel_rolling_diameter.setSizePolicy(sizePolicy2)
        self.label_second_wheel_rolling_diameter.setMinimumSize(QSize(400, 0))
        self.label_second_wheel_rolling_diameter.setMaximumSize(QSize(400, 16777215))
        self.label_second_wheel_rolling_diameter.setFont(font)

        self.horizontalLayout_58.addWidget(self.label_second_wheel_rolling_diameter)

        self.lineEdit_second_wheel_rolling_diameter = QLineEdit(self.frame_second_wheel_rolling_diameter)
        self.lineEdit_second_wheel_rolling_diameter.setObjectName(u"lineEdit_second_wheel_rolling_diameter")
        self.lineEdit_second_wheel_rolling_diameter.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_second_wheel_rolling_diameter.sizePolicy().hasHeightForWidth())
        self.lineEdit_second_wheel_rolling_diameter.setSizePolicy(sizePolicy1)
        self.lineEdit_second_wheel_rolling_diameter.setMinimumSize(QSize(0, 40))
        self.lineEdit_second_wheel_rolling_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_second_wheel_rolling_diameter.setFont(font)
        self.lineEdit_second_wheel_rolling_diameter.setStyleSheet(u"margin: 10px;")
        self.lineEdit_second_wheel_rolling_diameter.setDragEnabled(False)
        self.lineEdit_second_wheel_rolling_diameter.setClearButtonEnabled(True)

        self.horizontalLayout_58.addWidget(self.lineEdit_second_wheel_rolling_diameter)


        self.verticalLayout_15.addWidget(self.frame_second_wheel_rolling_diameter)

        self.frame_wheelbase_aparent = QFrame(self.scrollAreaWidgetContents)
        self.frame_wheelbase_aparent.setObjectName(u"frame_wheelbase_aparent")
        sizePolicy3.setHeightForWidth(self.frame_wheelbase_aparent.sizePolicy().hasHeightForWidth())
        self.frame_wheelbase_aparent.setSizePolicy(sizePolicy3)
        self.frame_wheelbase_aparent.setMinimumSize(QSize(0, 42))
        self.frame_wheelbase_aparent.setMaximumSize(QSize(16777215, 42))
        self.frame_wheelbase_aparent.setStyleSheet(u"")
        self.frame_wheelbase_aparent.setFrameShape(QFrame.StyledPanel)
        self.frame_wheelbase_aparent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_wheelbase_aparent)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_wheelbase_aparent = QLabel(self.frame_wheelbase_aparent)
        self.label_wheelbase_aparent.setObjectName(u"label_wheelbase_aparent")
        sizePolicy2.setHeightForWidth(self.label_wheelbase_aparent.sizePolicy().hasHeightForWidth())
        self.label_wheelbase_aparent.setSizePolicy(sizePolicy2)
        self.label_wheelbase_aparent.setMinimumSize(QSize(400, 0))
        self.label_wheelbase_aparent.setMaximumSize(QSize(400, 16777215))
        self.label_wheelbase_aparent.setFont(font)

        self.horizontalLayout_57.addWidget(self.label_wheelbase_aparent)

        self.lineEdit_wheelbase_aparent = QLineEdit(self.frame_wheelbase_aparent)
        self.lineEdit_wheelbase_aparent.setObjectName(u"lineEdit_wheelbase_aparent")
        self.lineEdit_wheelbase_aparent.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_wheelbase_aparent.sizePolicy().hasHeightForWidth())
        self.lineEdit_wheelbase_aparent.setSizePolicy(sizePolicy1)
        self.lineEdit_wheelbase_aparent.setMinimumSize(QSize(0, 40))
        self.lineEdit_wheelbase_aparent.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_wheelbase_aparent.setFont(font)
        self.lineEdit_wheelbase_aparent.setStyleSheet(u"margin: 10px;")
        self.lineEdit_wheelbase_aparent.setDragEnabled(False)
        self.lineEdit_wheelbase_aparent.setClearButtonEnabled(True)

        self.horizontalLayout_57.addWidget(self.lineEdit_wheelbase_aparent)


        self.verticalLayout_15.addWidget(self.frame_wheelbase_aparent)

        self.frame_slip_factor = QFrame(self.scrollAreaWidgetContents)
        self.frame_slip_factor.setObjectName(u"frame_slip_factor")
        sizePolicy3.setHeightForWidth(self.frame_slip_factor.sizePolicy().hasHeightForWidth())
        self.frame_slip_factor.setSizePolicy(sizePolicy3)
        self.frame_slip_factor.setMinimumSize(QSize(0, 42))
        self.frame_slip_factor.setMaximumSize(QSize(16777215, 42))
        self.frame_slip_factor.setStyleSheet(u"")
        self.frame_slip_factor.setFrameShape(QFrame.StyledPanel)
        self.frame_slip_factor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_slip_factor)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_slip_factor = QLabel(self.frame_slip_factor)
        self.label_slip_factor.setObjectName(u"label_slip_factor")
        sizePolicy2.setHeightForWidth(self.label_slip_factor.sizePolicy().hasHeightForWidth())
        self.label_slip_factor.setSizePolicy(sizePolicy2)
        self.label_slip_factor.setMinimumSize(QSize(400, 0))
        self.label_slip_factor.setMaximumSize(QSize(400, 16777215))
        self.label_slip_factor.setFont(font)

        self.horizontalLayout_56.addWidget(self.label_slip_factor)

        self.lineEdit_slip_factor = QLineEdit(self.frame_slip_factor)
        self.lineEdit_slip_factor.setObjectName(u"lineEdit_slip_factor")
        self.lineEdit_slip_factor.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_slip_factor.sizePolicy().hasHeightForWidth())
        self.lineEdit_slip_factor.setSizePolicy(sizePolicy1)
        self.lineEdit_slip_factor.setMinimumSize(QSize(0, 40))
        self.lineEdit_slip_factor.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_slip_factor.setFont(font)
        self.lineEdit_slip_factor.setStyleSheet(u"margin: 10px;")
        self.lineEdit_slip_factor.setDragEnabled(False)
        self.lineEdit_slip_factor.setClearButtonEnabled(True)

        self.horizontalLayout_56.addWidget(self.lineEdit_slip_factor)


        self.verticalLayout_15.addWidget(self.frame_slip_factor)

        self.frame_pinion_pitch_diameter = QFrame(self.scrollAreaWidgetContents)
        self.frame_pinion_pitch_diameter.setObjectName(u"frame_pinion_pitch_diameter")
        sizePolicy3.setHeightForWidth(self.frame_pinion_pitch_diameter.sizePolicy().hasHeightForWidth())
        self.frame_pinion_pitch_diameter.setSizePolicy(sizePolicy3)
        self.frame_pinion_pitch_diameter.setMinimumSize(QSize(0, 42))
        self.frame_pinion_pitch_diameter.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_pitch_diameter.setStyleSheet(u"")
        self.frame_pinion_pitch_diameter.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_pitch_diameter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_pinion_pitch_diameter)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_pitch_diameter = QLabel(self.frame_pinion_pitch_diameter)
        self.label_pinion_pitch_diameter.setObjectName(u"label_pinion_pitch_diameter")
        sizePolicy2.setHeightForWidth(self.label_pinion_pitch_diameter.sizePolicy().hasHeightForWidth())
        self.label_pinion_pitch_diameter.setSizePolicy(sizePolicy2)
        self.label_pinion_pitch_diameter.setMinimumSize(QSize(400, 0))
        self.label_pinion_pitch_diameter.setMaximumSize(QSize(400, 16777215))
        self.label_pinion_pitch_diameter.setFont(font)

        self.horizontalLayout_55.addWidget(self.label_pinion_pitch_diameter)

        self.lineEdit_pinion_pitch_diameter = QLineEdit(self.frame_pinion_pitch_diameter)
        self.lineEdit_pinion_pitch_diameter.setObjectName(u"lineEdit_pinion_pitch_diameter")
        self.lineEdit_pinion_pitch_diameter.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_pinion_pitch_diameter.sizePolicy().hasHeightForWidth())
        self.lineEdit_pinion_pitch_diameter.setSizePolicy(sizePolicy1)
        self.lineEdit_pinion_pitch_diameter.setMinimumSize(QSize(0, 40))
        self.lineEdit_pinion_pitch_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pinion_pitch_diameter.setFont(font)
        self.lineEdit_pinion_pitch_diameter.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pinion_pitch_diameter.setDragEnabled(False)
        self.lineEdit_pinion_pitch_diameter.setClearButtonEnabled(True)

        self.horizontalLayout_55.addWidget(self.lineEdit_pinion_pitch_diameter)


        self.verticalLayout_15.addWidget(self.frame_pinion_pitch_diameter)

        self.frame_second_wheel_pitch_diameter = QFrame(self.scrollAreaWidgetContents)
        self.frame_second_wheel_pitch_diameter.setObjectName(u"frame_second_wheel_pitch_diameter")
        sizePolicy3.setHeightForWidth(self.frame_second_wheel_pitch_diameter.sizePolicy().hasHeightForWidth())
        self.frame_second_wheel_pitch_diameter.setSizePolicy(sizePolicy3)
        self.frame_second_wheel_pitch_diameter.setMinimumSize(QSize(0, 42))
        self.frame_second_wheel_pitch_diameter.setMaximumSize(QSize(16777215, 42))
        self.frame_second_wheel_pitch_diameter.setStyleSheet(u"")
        self.frame_second_wheel_pitch_diameter.setFrameShape(QFrame.StyledPanel)
        self.frame_second_wheel_pitch_diameter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_second_wheel_pitch_diameter)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_second_wheel_pitch_diameter = QLabel(self.frame_second_wheel_pitch_diameter)
        self.label_second_wheel_pitch_diameter.setObjectName(u"label_second_wheel_pitch_diameter")
        sizePolicy2.setHeightForWidth(self.label_second_wheel_pitch_diameter.sizePolicy().hasHeightForWidth())
        self.label_second_wheel_pitch_diameter.setSizePolicy(sizePolicy2)
        self.label_second_wheel_pitch_diameter.setMinimumSize(QSize(400, 0))
        self.label_second_wheel_pitch_diameter.setMaximumSize(QSize(400, 16777215))
        self.label_second_wheel_pitch_diameter.setFont(font)

        self.horizontalLayout_68.addWidget(self.label_second_wheel_pitch_diameter)

        self.lineEdit_second_wheel_pitch_diameter = QLineEdit(self.frame_second_wheel_pitch_diameter)
        self.lineEdit_second_wheel_pitch_diameter.setObjectName(u"lineEdit_second_wheel_pitch_diameter")
        self.lineEdit_second_wheel_pitch_diameter.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_second_wheel_pitch_diameter.sizePolicy().hasHeightForWidth())
        self.lineEdit_second_wheel_pitch_diameter.setSizePolicy(sizePolicy1)
        self.lineEdit_second_wheel_pitch_diameter.setMinimumSize(QSize(0, 40))
        self.lineEdit_second_wheel_pitch_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_second_wheel_pitch_diameter.setFont(font)
        self.lineEdit_second_wheel_pitch_diameter.setStyleSheet(u"margin: 10px;")
        self.lineEdit_second_wheel_pitch_diameter.setDragEnabled(False)
        self.lineEdit_second_wheel_pitch_diameter.setClearButtonEnabled(True)

        self.horizontalLayout_68.addWidget(self.lineEdit_second_wheel_pitch_diameter)


        self.verticalLayout_15.addWidget(self.frame_second_wheel_pitch_diameter)

        self.frame_frontal_module = QFrame(self.scrollAreaWidgetContents)
        self.frame_frontal_module.setObjectName(u"frame_frontal_module")
        sizePolicy3.setHeightForWidth(self.frame_frontal_module.sizePolicy().hasHeightForWidth())
        self.frame_frontal_module.setSizePolicy(sizePolicy3)
        self.frame_frontal_module.setMinimumSize(QSize(0, 42))
        self.frame_frontal_module.setMaximumSize(QSize(16777215, 42))
        self.frame_frontal_module.setStyleSheet(u"")
        self.frame_frontal_module.setFrameShape(QFrame.StyledPanel)
        self.frame_frontal_module.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_frontal_module)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_frontal_module = QLabel(self.frame_frontal_module)
        self.label_frontal_module.setObjectName(u"label_frontal_module")
        sizePolicy2.setHeightForWidth(self.label_frontal_module.sizePolicy().hasHeightForWidth())
        self.label_frontal_module.setSizePolicy(sizePolicy2)
        self.label_frontal_module.setMinimumSize(QSize(400, 0))
        self.label_frontal_module.setMaximumSize(QSize(400, 16777215))
        self.label_frontal_module.setFont(font)

        self.horizontalLayout_67.addWidget(self.label_frontal_module)

        self.lineEdit_frontal_module = QLineEdit(self.frame_frontal_module)
        self.lineEdit_frontal_module.setObjectName(u"lineEdit_frontal_module")
        self.lineEdit_frontal_module.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_frontal_module.sizePolicy().hasHeightForWidth())
        self.lineEdit_frontal_module.setSizePolicy(sizePolicy1)
        self.lineEdit_frontal_module.setMinimumSize(QSize(0, 40))
        self.lineEdit_frontal_module.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_frontal_module.setFont(font)
        self.lineEdit_frontal_module.setStyleSheet(u"margin: 10px;")
        self.lineEdit_frontal_module.setDragEnabled(False)
        self.lineEdit_frontal_module.setClearButtonEnabled(True)

        self.horizontalLayout_67.addWidget(self.lineEdit_frontal_module)


        self.verticalLayout_15.addWidget(self.frame_frontal_module)

        self.frame_pinion_torque_outcome = QFrame(self.scrollAreaWidgetContents)
        self.frame_pinion_torque_outcome.setObjectName(u"frame_pinion_torque_outcome")
        sizePolicy3.setHeightForWidth(self.frame_pinion_torque_outcome.sizePolicy().hasHeightForWidth())
        self.frame_pinion_torque_outcome.setSizePolicy(sizePolicy3)
        self.frame_pinion_torque_outcome.setMinimumSize(QSize(0, 42))
        self.frame_pinion_torque_outcome.setMaximumSize(QSize(16777215, 42))
        self.frame_pinion_torque_outcome.setStyleSheet(u"")
        self.frame_pinion_torque_outcome.setFrameShape(QFrame.StyledPanel)
        self.frame_pinion_torque_outcome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_pinion_torque_outcome)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_pinion_toqrue_outcome = QLabel(self.frame_pinion_torque_outcome)
        self.label_pinion_toqrue_outcome.setObjectName(u"label_pinion_toqrue_outcome")
        sizePolicy2.setHeightForWidth(self.label_pinion_toqrue_outcome.sizePolicy().hasHeightForWidth())
        self.label_pinion_toqrue_outcome.setSizePolicy(sizePolicy2)
        self.label_pinion_toqrue_outcome.setMinimumSize(QSize(400, 0))
        self.label_pinion_toqrue_outcome.setMaximumSize(QSize(400, 16777215))
        self.label_pinion_toqrue_outcome.setFont(font)

        self.horizontalLayout_66.addWidget(self.label_pinion_toqrue_outcome)

        self.lineEdit_pinion_torque_outcome = QLineEdit(self.frame_pinion_torque_outcome)
        self.lineEdit_pinion_torque_outcome.setObjectName(u"lineEdit_pinion_torque_outcome")
        self.lineEdit_pinion_torque_outcome.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_pinion_torque_outcome.sizePolicy().hasHeightForWidth())
        self.lineEdit_pinion_torque_outcome.setSizePolicy(sizePolicy1)
        self.lineEdit_pinion_torque_outcome.setMinimumSize(QSize(0, 40))
        self.lineEdit_pinion_torque_outcome.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_pinion_torque_outcome.setFont(font)
        self.lineEdit_pinion_torque_outcome.setStyleSheet(u"margin: 10px;")
        self.lineEdit_pinion_torque_outcome.setDragEnabled(False)
        self.lineEdit_pinion_torque_outcome.setClearButtonEnabled(True)

        self.horizontalLayout_66.addWidget(self.lineEdit_pinion_torque_outcome)


        self.verticalLayout_15.addWidget(self.frame_pinion_torque_outcome)

        self.frame_force_tangential = QFrame(self.scrollAreaWidgetContents)
        self.frame_force_tangential.setObjectName(u"frame_force_tangential")
        sizePolicy3.setHeightForWidth(self.frame_force_tangential.sizePolicy().hasHeightForWidth())
        self.frame_force_tangential.setSizePolicy(sizePolicy3)
        self.frame_force_tangential.setMinimumSize(QSize(0, 42))
        self.frame_force_tangential.setMaximumSize(QSize(16777215, 42))
        self.frame_force_tangential.setStyleSheet(u"")
        self.frame_force_tangential.setFrameShape(QFrame.StyledPanel)
        self.frame_force_tangential.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_force_tangential)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_force_tangential = QLabel(self.frame_force_tangential)
        self.label_force_tangential.setObjectName(u"label_force_tangential")
        sizePolicy2.setHeightForWidth(self.label_force_tangential.sizePolicy().hasHeightForWidth())
        self.label_force_tangential.setSizePolicy(sizePolicy2)
        self.label_force_tangential.setMinimumSize(QSize(400, 0))
        self.label_force_tangential.setMaximumSize(QSize(400, 16777215))
        self.label_force_tangential.setFont(font)

        self.horizontalLayout_65.addWidget(self.label_force_tangential)

        self.lineEdit_force_tangential = QLineEdit(self.frame_force_tangential)
        self.lineEdit_force_tangential.setObjectName(u"lineEdit_force_tangential")
        self.lineEdit_force_tangential.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_force_tangential.sizePolicy().hasHeightForWidth())
        self.lineEdit_force_tangential.setSizePolicy(sizePolicy1)
        self.lineEdit_force_tangential.setMinimumSize(QSize(0, 40))
        self.lineEdit_force_tangential.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_force_tangential.setFont(font)
        self.lineEdit_force_tangential.setStyleSheet(u"margin: 10px;")
        self.lineEdit_force_tangential.setDragEnabled(False)
        self.lineEdit_force_tangential.setClearButtonEnabled(True)

        self.horizontalLayout_65.addWidget(self.lineEdit_force_tangential)


        self.verticalLayout_15.addWidget(self.frame_force_tangential)

        self.frame_force_longitudinal = QFrame(self.scrollAreaWidgetContents)
        self.frame_force_longitudinal.setObjectName(u"frame_force_longitudinal")
        sizePolicy3.setHeightForWidth(self.frame_force_longitudinal.sizePolicy().hasHeightForWidth())
        self.frame_force_longitudinal.setSizePolicy(sizePolicy3)
        self.frame_force_longitudinal.setMinimumSize(QSize(0, 42))
        self.frame_force_longitudinal.setMaximumSize(QSize(16777215, 42))
        self.frame_force_longitudinal.setStyleSheet(u"")
        self.frame_force_longitudinal.setFrameShape(QFrame.StyledPanel)
        self.frame_force_longitudinal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_force_longitudinal)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_force_longitudinal = QLabel(self.frame_force_longitudinal)
        self.label_force_longitudinal.setObjectName(u"label_force_longitudinal")
        sizePolicy2.setHeightForWidth(self.label_force_longitudinal.sizePolicy().hasHeightForWidth())
        self.label_force_longitudinal.setSizePolicy(sizePolicy2)
        self.label_force_longitudinal.setMinimumSize(QSize(400, 0))
        self.label_force_longitudinal.setMaximumSize(QSize(400, 16777215))
        self.label_force_longitudinal.setFont(font)

        self.horizontalLayout_64.addWidget(self.label_force_longitudinal)

        self.lineEdit_force_longitudinal = QLineEdit(self.frame_force_longitudinal)
        self.lineEdit_force_longitudinal.setObjectName(u"lineEdit_force_longitudinal")
        self.lineEdit_force_longitudinal.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_force_longitudinal.sizePolicy().hasHeightForWidth())
        self.lineEdit_force_longitudinal.setSizePolicy(sizePolicy1)
        self.lineEdit_force_longitudinal.setMinimumSize(QSize(0, 40))
        self.lineEdit_force_longitudinal.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_force_longitudinal.setFont(font)
        self.lineEdit_force_longitudinal.setStyleSheet(u"margin: 10px;")
        self.lineEdit_force_longitudinal.setDragEnabled(False)
        self.lineEdit_force_longitudinal.setClearButtonEnabled(True)

        self.horizontalLayout_64.addWidget(self.lineEdit_force_longitudinal)


        self.verticalLayout_15.addWidget(self.frame_force_longitudinal)

        self.frame_force_radial = QFrame(self.scrollAreaWidgetContents)
        self.frame_force_radial.setObjectName(u"frame_force_radial")
        sizePolicy3.setHeightForWidth(self.frame_force_radial.sizePolicy().hasHeightForWidth())
        self.frame_force_radial.setSizePolicy(sizePolicy3)
        self.frame_force_radial.setMinimumSize(QSize(0, 42))
        self.frame_force_radial.setMaximumSize(QSize(16777215, 42))
        self.frame_force_radial.setStyleSheet(u"")
        self.frame_force_radial.setFrameShape(QFrame.StyledPanel)
        self.frame_force_radial.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_force_radial)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_force_radial = QLabel(self.frame_force_radial)
        self.label_force_radial.setObjectName(u"label_force_radial")
        sizePolicy2.setHeightForWidth(self.label_force_radial.sizePolicy().hasHeightForWidth())
        self.label_force_radial.setSizePolicy(sizePolicy2)
        self.label_force_radial.setMinimumSize(QSize(400, 0))
        self.label_force_radial.setMaximumSize(QSize(400, 16777215))
        self.label_force_radial.setFont(font)

        self.horizontalLayout_63.addWidget(self.label_force_radial)

        self.lineEdit_force_radial = QLineEdit(self.frame_force_radial)
        self.lineEdit_force_radial.setObjectName(u"lineEdit_force_radial")
        self.lineEdit_force_radial.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_force_radial.sizePolicy().hasHeightForWidth())
        self.lineEdit_force_radial.setSizePolicy(sizePolicy1)
        self.lineEdit_force_radial.setMinimumSize(QSize(0, 40))
        self.lineEdit_force_radial.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_force_radial.setFont(font)
        self.lineEdit_force_radial.setStyleSheet(u"margin: 10px;")
        self.lineEdit_force_radial.setDragEnabled(False)
        self.lineEdit_force_radial.setClearButtonEnabled(True)

        self.horizontalLayout_63.addWidget(self.lineEdit_force_radial)


        self.verticalLayout_15.addWidget(self.frame_force_radial)

        self.frame_second_wheel_width = QFrame(self.scrollAreaWidgetContents)
        self.frame_second_wheel_width.setObjectName(u"frame_second_wheel_width")
        sizePolicy3.setHeightForWidth(self.frame_second_wheel_width.sizePolicy().hasHeightForWidth())
        self.frame_second_wheel_width.setSizePolicy(sizePolicy3)
        self.frame_second_wheel_width.setMinimumSize(QSize(0, 42))
        self.frame_second_wheel_width.setMaximumSize(QSize(16777215, 42))
        self.frame_second_wheel_width.setStyleSheet(u"")
        self.frame_second_wheel_width.setFrameShape(QFrame.StyledPanel)
        self.frame_second_wheel_width.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_second_wheel_width)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_second_wheel_width = QLabel(self.frame_second_wheel_width)
        self.label_second_wheel_width.setObjectName(u"label_second_wheel_width")
        sizePolicy2.setHeightForWidth(self.label_second_wheel_width.sizePolicy().hasHeightForWidth())
        self.label_second_wheel_width.setSizePolicy(sizePolicy2)
        self.label_second_wheel_width.setMinimumSize(QSize(400, 0))
        self.label_second_wheel_width.setMaximumSize(QSize(400, 16777215))
        self.label_second_wheel_width.setFont(font)

        self.horizontalLayout_69.addWidget(self.label_second_wheel_width)

        self.lineEdit_second_wheel_width = QLineEdit(self.frame_second_wheel_width)
        self.lineEdit_second_wheel_width.setObjectName(u"lineEdit_second_wheel_width")
        self.lineEdit_second_wheel_width.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_second_wheel_width.sizePolicy().hasHeightForWidth())
        self.lineEdit_second_wheel_width.setSizePolicy(sizePolicy1)
        self.lineEdit_second_wheel_width.setMinimumSize(QSize(0, 40))
        self.lineEdit_second_wheel_width.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_second_wheel_width.setFont(font)
        self.lineEdit_second_wheel_width.setStyleSheet(u"margin: 10px;")
        self.lineEdit_second_wheel_width.setDragEnabled(False)
        self.lineEdit_second_wheel_width.setClearButtonEnabled(True)

        self.horizontalLayout_69.addWidget(self.lineEdit_second_wheel_width)


        self.verticalLayout_15.addWidget(self.frame_second_wheel_width)

        self.frame_stepping_presure_number = QFrame(self.scrollAreaWidgetContents)
        self.frame_stepping_presure_number.setObjectName(u"frame_stepping_presure_number")
        sizePolicy3.setHeightForWidth(self.frame_stepping_presure_number.sizePolicy().hasHeightForWidth())
        self.frame_stepping_presure_number.setSizePolicy(sizePolicy3)
        self.frame_stepping_presure_number.setMinimumSize(QSize(0, 42))
        self.frame_stepping_presure_number.setMaximumSize(QSize(16777215, 42))
        self.frame_stepping_presure_number.setStyleSheet(u"")
        self.frame_stepping_presure_number.setFrameShape(QFrame.StyledPanel)
        self.frame_stepping_presure_number.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_stepping_presure_number)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_stepping_pressure_number = QLabel(self.frame_stepping_presure_number)
        self.label_stepping_pressure_number.setObjectName(u"label_stepping_pressure_number")
        sizePolicy2.setHeightForWidth(self.label_stepping_pressure_number.sizePolicy().hasHeightForWidth())
        self.label_stepping_pressure_number.setSizePolicy(sizePolicy2)
        self.label_stepping_pressure_number.setMinimumSize(QSize(400, 0))
        self.label_stepping_pressure_number.setMaximumSize(QSize(400, 16777215))
        self.label_stepping_pressure_number.setFont(font)

        self.horizontalLayout_42.addWidget(self.label_stepping_pressure_number)

        self.lineEdit_stepping_pressure_number = QLineEdit(self.frame_stepping_presure_number)
        self.lineEdit_stepping_pressure_number.setObjectName(u"lineEdit_stepping_pressure_number")
        self.lineEdit_stepping_pressure_number.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lineEdit_stepping_pressure_number.sizePolicy().hasHeightForWidth())
        self.lineEdit_stepping_pressure_number.setSizePolicy(sizePolicy1)
        self.lineEdit_stepping_pressure_number.setMinimumSize(QSize(0, 40))
        self.lineEdit_stepping_pressure_number.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_stepping_pressure_number.setFont(font)
        self.lineEdit_stepping_pressure_number.setStyleSheet(u"margin: 10px;")
        self.lineEdit_stepping_pressure_number.setDragEnabled(False)
        self.lineEdit_stepping_pressure_number.setClearButtonEnabled(True)

        self.horizontalLayout_42.addWidget(self.lineEdit_stepping_pressure_number)


        self.verticalLayout_15.addWidget(self.frame_stepping_presure_number)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_outcomes)
        self.page_excel = QWidget()
        self.page_excel.setObjectName(u"page_excel")
        self.gridLayout = QGridLayout(self.page_excel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 177, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(302, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(301, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 177, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.page_excel)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(180, 75))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(242, 242, 246);\n"
"background-color: rgb(76, 118, 232);\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(51, 82, 148);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_excel)
        self.page_scheme = QWidget()
        self.page_scheme.setObjectName(u"page_scheme")
        self.stackedWidget.addWidget(self.page_scheme)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


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
        self.factors_btn.setText(QCoreApplication.translate("MainWindow", u"WSP. KOREKCJI", None))
        self.diameters_btn.setText(QCoreApplication.translate("MainWindow", u"WYNIKI", None))
        self.excel_btn.setText(QCoreApplication.translate("MainWindow", u"RAPORT PDF", None))
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

        self.label_pressure_angle.setText(QCoreApplication.translate("MainWindow", u"NORMALNY K\u0104T PRZYPORU [\u00b0]", None))
        self.lineEdit_pressure_angle.setPlaceholderText("")
        self.label_helix_angle.setText(QCoreApplication.translate("MainWindow", u"K\u0104T POCHYLENIA LINII \u015aRUBOWEJ Z\u0118BA [\u00b0]", None))
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
        self.label_preconditions_2.setText(QCoreApplication.translate("MainWindow", u"PARAMETRY GEOMETRYCZNE", None))
        self.label_pinion_toqrue.setText(QCoreApplication.translate("MainWindow", u"MOMENT OBCI\u0104\u017bAJ\u0104CY Z\u0118BNIK", None))
        self.lineEdit_pinion_torque.setPlaceholderText("")
        self.label_calculated_normal_module.setText(QCoreApplication.translate("MainWindow", u"OBLICZENIOWY MODU\u0141 NORMALNY", None))
        self.lineEdit_calculated_normal_module.setPlaceholderText("")
        self.label_normal_module.setText(QCoreApplication.translate("MainWindow", u"MODU\u0141 NORMALNY", None))
        self.comboBox_normal_module.setItemText(0, QCoreApplication.translate("MainWindow", u"1.00", None))
        self.comboBox_normal_module.setItemText(1, QCoreApplication.translate("MainWindow", u"1.12", None))
        self.comboBox_normal_module.setItemText(2, QCoreApplication.translate("MainWindow", u"1.25", None))
        self.comboBox_normal_module.setItemText(3, QCoreApplication.translate("MainWindow", u"1.40", None))
        self.comboBox_normal_module.setItemText(4, QCoreApplication.translate("MainWindow", u"1.60", None))
        self.comboBox_normal_module.setItemText(5, QCoreApplication.translate("MainWindow", u"1.80", None))
        self.comboBox_normal_module.setItemText(6, QCoreApplication.translate("MainWindow", u"2.00", None))
        self.comboBox_normal_module.setItemText(7, QCoreApplication.translate("MainWindow", u"2.24", None))
        self.comboBox_normal_module.setItemText(8, QCoreApplication.translate("MainWindow", u"2.50", None))
        self.comboBox_normal_module.setItemText(9, QCoreApplication.translate("MainWindow", u"2.80", None))
        self.comboBox_normal_module.setItemText(10, QCoreApplication.translate("MainWindow", u"3.15", None))
        self.comboBox_normal_module.setItemText(11, QCoreApplication.translate("MainWindow", u"3.55", None))
        self.comboBox_normal_module.setItemText(12, QCoreApplication.translate("MainWindow", u"4.00", None))
        self.comboBox_normal_module.setItemText(13, QCoreApplication.translate("MainWindow", u"4.50", None))
        self.comboBox_normal_module.setItemText(14, QCoreApplication.translate("MainWindow", u"5.00", None))
        self.comboBox_normal_module.setItemText(15, QCoreApplication.translate("MainWindow", u"5.60", None))
        self.comboBox_normal_module.setItemText(16, QCoreApplication.translate("MainWindow", u"6.30", None))
        self.comboBox_normal_module.setItemText(17, QCoreApplication.translate("MainWindow", u"7.10", None))
        self.comboBox_normal_module.setItemText(18, QCoreApplication.translate("MainWindow", u"8.00", None))
        self.comboBox_normal_module.setItemText(19, QCoreApplication.translate("MainWindow", u"9.00", None))
        self.comboBox_normal_module.setItemText(20, QCoreApplication.translate("MainWindow", u"10.00", None))
        self.comboBox_normal_module.setItemText(21, QCoreApplication.translate("MainWindow", u"11.20", None))
        self.comboBox_normal_module.setItemText(22, QCoreApplication.translate("MainWindow", u"12.00", None))
        self.comboBox_normal_module.setItemText(23, QCoreApplication.translate("MainWindow", u"12.50", None))
        self.comboBox_normal_module.setItemText(24, QCoreApplication.translate("MainWindow", u"14.00", None))
        self.comboBox_normal_module.setItemText(25, QCoreApplication.translate("MainWindow", u"16.00", None))
        self.comboBox_normal_module.setItemText(26, QCoreApplication.translate("MainWindow", u"18.00", None))
        self.comboBox_normal_module.setItemText(27, QCoreApplication.translate("MainWindow", u"20.00", None))
        self.comboBox_normal_module.setItemText(28, QCoreApplication.translate("MainWindow", u"22.40", None))
        self.comboBox_normal_module.setItemText(29, QCoreApplication.translate("MainWindow", u"25.00", None))
        self.comboBox_normal_module.setItemText(30, QCoreApplication.translate("MainWindow", u"28.00", None))
        self.comboBox_normal_module.setItemText(31, QCoreApplication.translate("MainWindow", u"31.50", None))
        self.comboBox_normal_module.setItemText(32, QCoreApplication.translate("MainWindow", u"35.50", None))
        self.comboBox_normal_module.setItemText(33, QCoreApplication.translate("MainWindow", u"40.00", None))
        self.comboBox_normal_module.setItemText(34, QCoreApplication.translate("MainWindow", u"45.00", None))
        self.comboBox_normal_module.setItemText(35, QCoreApplication.translate("MainWindow", u"50.00", None))
        self.comboBox_normal_module.setItemText(36, QCoreApplication.translate("MainWindow", u"56.00", None))
        self.comboBox_normal_module.setItemText(37, QCoreApplication.translate("MainWindow", u"63.00", None))
        self.comboBox_normal_module.setItemText(38, QCoreApplication.translate("MainWindow", u"71.00", None))
        self.comboBox_normal_module.setItemText(39, QCoreApplication.translate("MainWindow", u"80.00", None))
        self.comboBox_normal_module.setItemText(40, QCoreApplication.translate("MainWindow", u"90.00", None))
        self.comboBox_normal_module.setItemText(41, QCoreApplication.translate("MainWindow", u"100.00", None))
        self.comboBox_normal_module.setItemText(42, QCoreApplication.translate("MainWindow", u"112.00", None))
        self.comboBox_normal_module.setItemText(43, QCoreApplication.translate("MainWindow", u"125.00", None))
        self.comboBox_normal_module.setItemText(44, QCoreApplication.translate("MainWindow", u"140.00", None))
        self.comboBox_normal_module.setItemText(45, QCoreApplication.translate("MainWindow", u"160.00", None))
        self.comboBox_normal_module.setItemText(46, QCoreApplication.translate("MainWindow", u"180.00", None))
        self.comboBox_normal_module.setItemText(47, QCoreApplication.translate("MainWindow", u"200.00", None))

        self.normal_module_confirm_btn.setText(QCoreApplication.translate("MainWindow", u"ZATWIERD\u0179", None))
        self.label_bottome_ratio_border.setText(QCoreApplication.translate("MainWindow", u"DOLNA GRANICA B\u0141\u0118DU PRZE\u0141O\u017bENIA", None))
        self.lineEdit_bottom_ratio_border.setPlaceholderText("")
        self.label_upper_ratio_border.setText(QCoreApplication.translate("MainWindow", u"G\u00d3RNA GRANICA B\u0141\u0118DU PRZE\u0141O\u017bENIA", None))
        self.lineEdit_upper_ratio_border.setPlaceholderText("")
        self.label_calculated_tooth_number.setText(QCoreApplication.translate("MainWindow", u"OBLICZENIOWA LICZBA Z\u0118B\u00d3W DRUGIEGO KO\u0141A", None))
        self.lineEdit_calculated_tooth_number.setPlaceholderText("")
        self.label_2nd_wheel_tooth_number.setText(QCoreApplication.translate("MainWindow", u"LICZBA Z\u0118B\u00d3W DRUGIEGO KO\u0141A", None))
        self.lineEdit_2nd_wheel_tooth_number.setPlaceholderText("")
        self.second_wheel_tooth_number_confirm_btn.setText(QCoreApplication.translate("MainWindow", u"ZATWIERD\u0179", None))
        self.label_real_ratio.setText(QCoreApplication.translate("MainWindow", u"PRZE\u0141O\u017bENIE RZECZYWISTE", None))
        self.lineEdit_real_ratio.setPlaceholderText("")
        self.correction_factors_header_label.setText(QCoreApplication.translate("MainWindow", u"WSP\u00d3\u0141CZYNNIKI KOREKCJI", None))
        self.bring_back_defaults_btn.setText(QCoreApplication.translate("MainWindow", u"WART. DOMY\u015aLNE", None))
        self.factors_sum_frame.setText(QCoreApplication.translate("MainWindow", u"(X1 + X2) / 2", None))
        self.factors_sum_line_edit.setPlaceholderText("")
        self.tooth_number_sum_frame.setText(QCoreApplication.translate("MainWindow", u"(Z1 + Z2) / 2", None))
        self.tooth_number_sum_line_edit.setPlaceholderText("")
        self.graph_generate_button.setText(QCoreApplication.translate("MainWindow", u"G\n"
"E\n"
"N\n"
"E\n"
"R\n"
"U\n"
"J", None))
        self.label_preconditions_3.setText(QCoreApplication.translate("MainWindow", u"WYNIKI", None))
        self.label_wheelbase_zero.setText(QCoreApplication.translate("MainWindow", u"ZEROWA ODLEG\u0141O\u015a\u0106 OSI", None))
        self.lineEdit_wheelbase_zero.setPlaceholderText("")
        self.label_estimated_correction_factors_sum.setText(QCoreApplication.translate("MainWindow", u"PRZYBLI\u017bONA WARTO\u015a\u0106 SUMY WSP. KOREKCJI", None))
        self.lineEdit_estimated_correction_factors_sum.setPlaceholderText("")
        self.label_alfa_t.setText(QCoreApplication.translate("MainWindow", u"K\u0104T ZARYSU W PRZEKROJU CZO\u0141OWYM", None))
        self.lineEdit_alfa_t.setPlaceholderText("")
        self.label_alfa_tw.setText(QCoreApplication.translate("MainWindow", u"K\u0104T PRZYPORU TOCZNY W PRZEKROJU CZO\u0141OWYM ", None))
        self.lineEdit_alfa_tw.setPlaceholderText("")
        self.label_inv_alfa_tw.setText(QCoreApplication.translate("MainWindow", u"FUNKCJA EWOLWENTOWA ALFA_TW", None))
        self.lineEdit_inv_alfa_tw.setPlaceholderText("")
        self.label_inv_alfa_t.setText(QCoreApplication.translate("MainWindow", u"FUNKCJA EWOLWENTOWA ALFTA_T", None))
        self.lineEdit_inv_alfa_t.setPlaceholderText("")
        self.label_correction_factors_sum.setText(QCoreApplication.translate("MainWindow", u"SUMA WSP\u00d3\u0141CZYNNIK\u00d3W KOREKCJI", None))
        self.lineEdit_correction_factors_sum.setPlaceholderText("")
        self.label_beta_b_helix_angle.setText(QCoreApplication.translate("MainWindow", u"K\u0104T POCHYLENIA LINII Z\u0118BA \n"
"NA WALCU ZASADNICZYM", None))
        self.lineEdit_beta_b_helix_angle.setPlaceholderText("")
        self.label_pinion_tooth_number_placeholder.setText(QCoreApplication.translate("MainWindow", u"ZAST\u0118PCZA LICZBA Z\u0118B\u00d3W Z\u0118BNIKA", None))
        self.lineEdit_pinion_tooth_number_placeholder.setPlaceholderText("")
        self.label_second_wheel_tooth_number_placeholder.setText(QCoreApplication.translate("MainWindow", u"ZAST\u0118PCZA LICZBA Z\u0118B\u00d3W KO\u0141A", None))
        self.lineEdit_second_wheel_tooth_number_placeholder.setPlaceholderText("")
        self.label_pinion_correction_factor.setText(QCoreApplication.translate("MainWindow", u"WSP\u00d3\u0141CZYNNIK KOREKCJI Z\u0118BNIKA", None))
        self.lineEdit_pinion_correction_factor.setPlaceholderText("")
        self.label_second_wheel_correction_factor.setText(QCoreApplication.translate("MainWindow", u"WSP\u00d3\u0141CZYNNIK KOREKCJI KO\u0141A", None))
        self.lineEdit_second_wheel_correction_factor.setPlaceholderText("")
        self.label_pinion_rolling_diameter.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICA TOCZNA Z\u0118BNIKA", None))
        self.lineEdit_pinion_rolling_diameter.setPlaceholderText("")
        self.label_second_wheel_rolling_diameter.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICA TOCZNA KO\u0141A", None))
        self.lineEdit_second_wheel_rolling_diameter.setPlaceholderText("")
        self.label_wheelbase_aparent.setText(QCoreApplication.translate("MainWindow", u"POZORNA ODLEG\u0141O\u015a\u0106 OSI", None))
        self.lineEdit_wheelbase_aparent.setPlaceholderText("")
        self.label_slip_factor.setText(QCoreApplication.translate("MainWindow", u"WSP\u00d3\u0141CZYNNIK ZSUNI\u0118CIA", None))
        self.lineEdit_slip_factor.setPlaceholderText("")
        self.label_pinion_pitch_diameter.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICA PODZIA\u0141OWA Z\u0118BNIKA", None))
        self.lineEdit_pinion_pitch_diameter.setPlaceholderText("")
        self.label_second_wheel_pitch_diameter.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNICA PODZIA\u0141OWA KO\u0141A", None))
        self.lineEdit_second_wheel_pitch_diameter.setPlaceholderText("")
        self.label_frontal_module.setText(QCoreApplication.translate("MainWindow", u"MODU\u0141 CZO\u0141OWY", None))
        self.lineEdit_frontal_module.setPlaceholderText("")
        self.label_pinion_toqrue_outcome.setText(QCoreApplication.translate("MainWindow", u"MOMENT OBROTOWY OBCI\u0104\u017bAJ\u0104CY Z\u0118BNIK", None))
        self.lineEdit_pinion_torque_outcome.setPlaceholderText("")
        self.label_force_tangential.setText(QCoreApplication.translate("MainWindow", u"SI\u0141A STYCZNA", None))
        self.lineEdit_force_tangential.setPlaceholderText("")
        self.label_force_longitudinal.setText(QCoreApplication.translate("MainWindow", u"SI\u0141A WZD\u0141U\u017bNA", None))
        self.lineEdit_force_longitudinal.setPlaceholderText("")
        self.label_force_radial.setText(QCoreApplication.translate("MainWindow", u"SI\u0141A PROMIENIOWA", None))
        self.lineEdit_force_radial.setPlaceholderText("")
        self.label_second_wheel_width.setText(QCoreApplication.translate("MainWindow", u"SZEROKO\u015a\u0106 KO\u0141A", None))
        self.lineEdit_second_wheel_width.setPlaceholderText("")
        self.label_stepping_pressure_number.setText(QCoreApplication.translate("MainWindow", u"POSKOKOWA LICZBA PRZYPORU", None))
        self.lineEdit_stepping_pressure_number.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ZAPISZ WYNIKI \n"
"DO PLIKU PDF", None))
    # retranslateUi


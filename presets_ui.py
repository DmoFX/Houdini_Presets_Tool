# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'presets_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(730, 654)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 30, 621, 551))
        self.load_presets = QWidget()
        self.load_presets.setObjectName(u"load_presets")
        self.gridLayoutWidget = QWidget(self.load_presets)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 611, 521))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.gridLayoutWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout.addWidget(self.treeWidget, 6, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_info = QLabel(self.gridLayoutWidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_info)

        self.btn_load = QPushButton(self.gridLayoutWidget)
        self.btn_load.setObjectName(u"btn_load")

        self.verticalLayout.addWidget(self.btn_load)


        self.gridLayout.addLayout(self.verticalLayout, 6, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_txt1 = QLabel(self.gridLayoutWidget)
        self.label_txt1.setObjectName(u"label_txt1")
        self.label_txt1.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.label_txt1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 7, 3, 1, 1)

        self.tabWidget.addTab(self.load_presets, "")
        self.create_presets = QWidget()
        self.create_presets.setObjectName(u"create_presets")
        self.gridLayoutWidget_2 = QWidget(self.create_presets)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 601, 511))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_txt2 = QLabel(self.gridLayoutWidget_2)
        self.label_txt2.setObjectName(u"label_txt2")

        self.horizontalLayout_3.addWidget(self.label_txt2)

        self.lineEdit_name = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout_3.addWidget(self.lineEdit_name)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.btn_create = QPushButton(self.gridLayoutWidget_2)
        self.btn_create.setObjectName(u"btn_create")

        self.gridLayout_2.addWidget(self.btn_create, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_drop = QLabel(self.gridLayoutWidget_2)
        self.label_drop.setObjectName(u"label_drop")
        self.label_drop.setStyleSheet(u"border: 2px dashed #aaa")
        self.label_drop.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_drop)

        self.txtEdit_info = QTextEdit(self.gridLayoutWidget_2)
        self.txtEdit_info.setObjectName(u"txtEdit_info")

        self.verticalLayout_3.addWidget(self.txtEdit_info)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.listWidget = QListWidget(self.gridLayoutWidget_2)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.create_presets, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_info.setText(QCoreApplication.translate("Form", u"Preset information.", None))
        self.btn_load.setText(QCoreApplication.translate("Form", u"Load", None))
        self.label_txt1.setText(QCoreApplication.translate("Form", u"Load as:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.load_presets), QCoreApplication.translate("Form", u"Load Presets", None))
        self.label_txt2.setText(QCoreApplication.translate("Form", u"Category/Name:", None))
        self.btn_create.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_drop.setText(QCoreApplication.translate("Form", u"Drop your preset here.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_presets), QCoreApplication.translate("Form", u"Create Preset", None))
    # retranslateUi


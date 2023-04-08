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
        Form.resize(730, 655)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.load_presets = QWidget()
        self.load_presets.setObjectName(u"load_presets")
        self.verticalLayout_4 = QVBoxLayout(self.load_presets)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_screenshots = QLabel(self.load_presets)
        self.label_screenshots.setObjectName(u"label_screenshots")
        self.label_screenshots.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_screenshots)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_l_show = QPushButton(self.load_presets)
        self.btn_l_show.setObjectName(u"btn_l_show")

        self.horizontalLayout_4.addWidget(self.btn_l_show)

        self.btn_l_back = QPushButton(self.load_presets)
        self.btn_l_back.setObjectName(u"btn_l_back")

        self.horizontalLayout_4.addWidget(self.btn_l_back)

        self.btn_l_next = QPushButton(self.load_presets)
        self.btn_l_next.setObjectName(u"btn_l_next")

        self.horizontalLayout_4.addWidget(self.btn_l_next)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.label_info = QLabel(self.load_presets)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_info)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(2, 5)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.btn_load = QPushButton(self.load_presets)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btn_load)


        self.gridLayout.addLayout(self.verticalLayout, 6, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.label_username = QLabel(self.load_presets)
        self.label_username.setObjectName(u"label_username")

        self.gridLayout.addWidget(self.label_username, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 7, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_txt1 = QLabel(self.load_presets)
        self.label_txt1.setObjectName(u"label_txt1")
        self.label_txt1.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.label_txt1)

        self.comboBox = QComboBox(self.load_presets)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.treeWidget = QTreeWidget(self.load_presets)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_6.addWidget(self.treeWidget)

        self.lineEdit_filter = QLineEdit(self.load_presets)
        self.lineEdit_filter.setObjectName(u"lineEdit_filter")

        self.verticalLayout_6.addWidget(self.lineEdit_filter)


        self.gridLayout.addLayout(self.verticalLayout_6, 6, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.load_presets, "")
        self.create_presets = QWidget()
        self.create_presets.setObjectName(u"create_presets")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_presets.sizePolicy().hasHeightForWidth())
        self.create_presets.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.create_presets)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.horizontalSpacer_4 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)

        self.label_drop = QLabel(self.create_presets)
        self.label_drop.setObjectName(u"label_drop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_drop.sizePolicy().hasHeightForWidth())
        self.label_drop.setSizePolicy(sizePolicy1)
        self.label_drop.setStyleSheet(u"border: 2px dashed #aaa")
        self.label_drop.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_drop, 4, 0, 1, 1)

        self.btn_create = QPushButton(self.create_presets)
        self.btn_create.setObjectName(u"btn_create")

        self.gridLayout_2.addWidget(self.btn_create, 5, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_txt2 = QLabel(self.create_presets)
        self.label_txt2.setObjectName(u"label_txt2")

        self.horizontalLayout_3.addWidget(self.label_txt2)

        self.lineEdit_name = QLineEdit(self.create_presets)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout_3.addWidget(self.lineEdit_name)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_record = QLabel(self.create_presets)
        self.label_record.setObjectName(u"label_record")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_record.sizePolicy().hasHeightForWidth())
        self.label_record.setSizePolicy(sizePolicy2)
        self.label_record.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_record)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_r_record = QPushButton(self.create_presets)
        self.btn_r_record.setObjectName(u"btn_r_record")

        self.horizontalLayout.addWidget(self.btn_r_record)

        self.btn_r_back = QPushButton(self.create_presets)
        self.btn_r_back.setObjectName(u"btn_r_back")

        self.horizontalLayout.addWidget(self.btn_r_back)

        self.btn_r_next = QPushButton(self.create_presets)
        self.btn_r_next.setObjectName(u"btn_r_next")
        self.btn_r_next.setAutoExclusive(False)
        self.btn_r_next.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_r_next)

        self.btn_r_show = QPushButton(self.create_presets)
        self.btn_r_show.setObjectName(u"btn_r_show")

        self.horizontalLayout.addWidget(self.btn_r_show)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.txtEdit_info = QTextEdit(self.create_presets)
        self.txtEdit_info.setObjectName(u"txtEdit_info")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txtEdit_info.sizePolicy().hasHeightForWidth())
        self.txtEdit_info.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.txtEdit_info, 4, 1, 1, 1)

        self.listWidget = QListWidget(self.create_presets)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(1, 80)

        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.create_presets, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label_screenshots.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Double click for the full resolution image.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_screenshots.setText(QCoreApplication.translate("Form", u"Screenshots", None))
#if QT_CONFIG(tooltip)
        self.btn_l_show.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Show video.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_l_show.setText("")
#if QT_CONFIG(tooltip)
        self.btn_l_back.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Back image.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_l_back.setText("")
#if QT_CONFIG(tooltip)
        self.btn_l_next.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Next image.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_l_next.setText("")
        self.label_info.setText(QCoreApplication.translate("Form", u"Preset information.", None))
        self.btn_load.setText(QCoreApplication.translate("Form", u"Load", None))
        self.label_username.setText("")
        self.label_txt1.setText(QCoreApplication.translate("Form", u"Load as:", None))
        self.lineEdit_filter.setText("")
        self.lineEdit_filter.setPlaceholderText(QCoreApplication.translate("Form", u"Filter presets by name.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.load_presets), QCoreApplication.translate("Form", u"Load Presets", None))
#if QT_CONFIG(tooltip)
        self.label_drop.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt;\">Drag and drop subnetwork or mulitple nodes here. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_drop.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">Drop your preset here.</span></p></body></html>", None))
        self.btn_create.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_txt2.setText(QCoreApplication.translate("Form", u"Category/Name:", None))
#if QT_CONFIG(tooltip)
        self.label_record.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt;\">Add screenshots and short video recording to briefly show what your setup is doing.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_record.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">Screenshots</span></p><p><br/></p><p>Before hit Record ensure that <span style=\" text-decoration: underline;\">Category/Name</span> is final</p><p>and won't change!</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_r_record.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Screen record dialog. You can capture screenshots or video.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_r_record.setText("")
#if QT_CONFIG(tooltip)
        self.btn_r_back.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Back image.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_r_back.setText("")
#if QT_CONFIG(tooltip)
        self.btn_r_next.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Next image.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_r_next.setText("")
#if QT_CONFIG(tooltip)
        self.btn_r_show.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Show video.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_r_show.setText("")
        self.txtEdit_info.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.txtEdit_info.setPlaceholderText(QCoreApplication.translate("Form", u"Add description of your setup please.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_presets), QCoreApplication.translate("Form", u"Create Preset", None))
    # retranslateUi


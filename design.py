# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
        Form.resize(631, 419)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 631, 431))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setDocumentMode(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"QLabel {\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 0, 611, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 122))
        font = QFont()
        font.setPointSize(18)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border: 1px solid black;\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_novosibpatchstatus = QLabel(self.verticalLayoutWidget)
        self.label_novosibpatchstatus.setObjectName(u"label_novosibpatchstatus")
        self.label_novosibpatchstatus.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_novosibpatchstatus, 2, 2, 1, 1)

        self.krasnodar_button = QPushButton(self.verticalLayoutWidget)
        self.krasnodar_button.setObjectName(u"krasnodar_button")

        self.gridLayout.addWidget(self.krasnodar_button, 3, 3, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.msk_button = QPushButton(self.verticalLayoutWidget)
        self.msk_button.setObjectName(u"msk_button")

        self.gridLayout.addWidget(self.msk_button, 1, 3, 1, 1)

        self.label_krasnodarping = QLabel(self.verticalLayoutWidget)
        self.label_krasnodarping.setObjectName(u"label_krasnodarping")
        self.label_krasnodarping.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_krasnodarping, 3, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAutoFillBackground(False)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(-1)
        self.label_7.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_krasnodarpatchstatus = QLabel(self.verticalLayoutWidget)
        self.label_krasnodarpatchstatus.setObjectName(u"label_krasnodarpatchstatus")
        self.label_krasnodarpatchstatus.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_krasnodarpatchstatus, 3, 2, 1, 1)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_habarovskpatchstatus = QLabel(self.verticalLayoutWidget)
        self.label_habarovskpatchstatus.setObjectName(u"label_habarovskpatchstatus")
        self.label_habarovskpatchstatus.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_habarovskpatchstatus, 4, 2, 1, 1)

        self.label_novosibping = QLabel(self.verticalLayoutWidget)
        self.label_novosibping.setObjectName(u"label_novosibping")
        self.label_novosibping.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_novosibping, 2, 1, 1, 1)

        self.novosibirsk_button = QPushButton(self.verticalLayoutWidget)
        self.novosibirsk_button.setObjectName(u"novosibirsk_button")

        self.gridLayout.addWidget(self.novosibirsk_button, 2, 3, 1, 1)

        self.label_mskping = QLabel(self.verticalLayoutWidget)
        self.label_mskping.setObjectName(u"label_mskping")
        self.label_mskping.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_mskping, 1, 1, 1, 1)

        self.label_mskpatchstatus = QLabel(self.verticalLayoutWidget)
        self.label_mskpatchstatus.setObjectName(u"label_mskpatchstatus")
        self.label_mskpatchstatus.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_mskpatchstatus, 1, 2, 1, 1)

        self.habarovsk_button = QPushButton(self.verticalLayoutWidget)
        self.habarovsk_button.setObjectName(u"habarovsk_button")

        self.gridLayout.addWidget(self.habarovsk_button, 4, 3, 1, 1)

        self.label_habarovskping = QLabel(self.verticalLayoutWidget)
        self.label_habarovskping.setObjectName(u"label_habarovskping")
        self.label_habarovskping.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_habarovskping, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayoutWidget_3 = QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(5, 3, 621, 391))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.verticalLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(0, 122))
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_25)

        self.line_3 = QFrame(self.verticalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.label_20 = QLabel(self.verticalLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_20)

        self.line = QFrame(self.verticalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_21 = QLabel(self.verticalLayoutWidget_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setWordWrap(True)
        self.label_21.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label_21)

        self.line_4 = QFrame(self.verticalLayoutWidget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.label_22 = QLabel(self.verticalLayoutWidget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setTextFormat(Qt.AutoText)
        self.label_22.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label_22)

        self.line_2 = QFrame(self.verticalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_24 = QLabel(self.verticalLayoutWidget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_24)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"WF Server Patcher by Shitrya", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Warface Server Patcher", None))
        self.label_novosibpatchstatus.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.krasnodar_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a\u0438\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440\u0441\u043a\u0438\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0441\u043a\u043e\u0432\u0441\u043a\u0438\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.msk_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_krasnodarping.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0440\u0432\u0435\u0440", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u041f\u0438\u043d\u0433", None))
        self.label_krasnodarpatchstatus.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u0430\u0442\u0447\u0430", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0425\u0430\u0431\u0430\u0440\u043e\u0432\u0441\u043a\u0438\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.label_habarovskpatchstatus.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.label_novosibping.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.novosibirsk_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_mskping.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.label_mskpatchstatus.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.habarovsk_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_habarovskping.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt;\"> Warface Server Patcher</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f: \u0434\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0430 \u0434\u043b\u044f \u043e\u0431\u0445\u043e\u0434\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0439 \u0432 \u0418\u0433\u0440\u043e\u0432\u043e\u043c \u0446\u0435\u043d\u0442\u0440\u0435, \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0445 \u0441 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0435\u043c \u0432\u044b\u0431\u043e\u0440\u0430 \u0440\u0435\u0433\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432. \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0432\u043d\u043e\u0441\u0438\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0432 \u0444\u0430\u0439\u043b hosts, \u0442\u0435\u043c \u0441"
                        "\u0430\u043c\u044b\u043c, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u044f \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043b\u044e\u0431\u043e\u0439 \u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u0441\u0435\u0440\u0432\u0435\u0440.</span><span style=\" font-size:9pt;\"><br/></span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a: </span><a href=\"https://vk.com/shitryadima\"><span style=\" font-size:9pt; text-decoration: underline; color:#0000ff;\">\u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0428\u0438\u0442\u0440\u044f</span></a> \u00a9 2022</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>GitHub: <a href = \"https://github.com/ShitryaDima/wf-server-patcher\">https://github.com/ShitryaDima/wf-server-patcher</a></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u0414\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u0430 \u043e\u0442 \u0438\u043c\u0435\u043d\u0438 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430!</span></p><p><span style=\" color:#ff0000;\">\u0427\u0442\u043e\u0431\u044b \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0432\u0441\u0442\u0443\u043f\u0438\u043b\u0438 \u0432 \u0441\u0438\u043b\u0443 \u043f\u0435\u0440\u0435\u0437\u0430\u0439\u0434\u0438\u0442\u0435 \u0432 \u0418\u0433\u0440\u043e\u0432\u043e\u0439 \u0446\u0435\u043d\u0442\u0440!</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u041e \u0441\u043e\u0437\u0434\u0430\u0442\u0435\u043b\u0435", None))
    # retranslateUi


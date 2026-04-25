# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 703)
        self.action_log_out = QAction(MainWindow)
        self.action_log_out.setObjectName(u"action_log_out")
        self.action_close_app = QAction(MainWindow)
        self.action_close_app.setObjectName(u"action_close_app")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.gridLayout = QGridLayout(self.page_login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.page_login)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEditl_login = QLineEdit(self.page_login)
        self.lineEditl_login.setObjectName(u"lineEditl_login")

        self.gridLayout.addWidget(self.lineEditl_login, 1, 1, 1, 3)

        self.label_2 = QLabel(self.page_login)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.page_login)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 2, 1, 1, 3)

        self.pushButton_new_account = QPushButton(self.page_login)
        self.pushButton_new_account.setObjectName(u"pushButton_new_account")

        self.gridLayout.addWidget(self.pushButton_new_account, 3, 2, 1, 1)

        self.pushButton_login = QPushButton(self.page_login)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.gridLayout.addWidget(self.pushButton_login, 3, 3, 1, 1)

        self.label_3 = QLabel(self.page_login)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(35)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 4)

        self.stackedWidget.addWidget(self.page_login)
        self.page_chat = QWidget()
        self.page_chat.setObjectName(u"page_chat")
        self.gridLayout_4 = QGridLayout(self.page_chat)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_input = QLineEdit(self.page_chat)
        self.lineEdit_input.setObjectName(u"lineEdit_input")

        self.gridLayout_4.addWidget(self.lineEdit_input, 5, 2, 1, 2)

        self.label_current_user = QLabel(self.page_chat)
        self.label_current_user.setObjectName(u"label_current_user")

        self.gridLayout_4.addWidget(self.label_current_user, 0, 2, 1, 1)

        self.textEdit_chat = QTextEdit(self.page_chat)
        self.textEdit_chat.setObjectName(u"textEdit_chat")

        self.gridLayout_4.addWidget(self.textEdit_chat, 1, 2, 4, 3)

        self.listWidget_clients_list = QListWidget(self.page_chat)
        self.listWidget_clients_list.setObjectName(u"listWidget_clients_list")
        self.listWidget_clients_list.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_4.addWidget(self.listWidget_clients_list, 1, 1, 1, 1)

        self.label_8 = QLabel(self.page_chat)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 1, 1, 1)

        self.pushButton_send = QPushButton(self.page_chat)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.gridLayout_4.addWidget(self.pushButton_send, 5, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_chat)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.gridLayout_2 = QGridLayout(self.page_register)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_name_reg = QLineEdit(self.page_register)
        self.lineEdit_name_reg.setObjectName(u"lineEdit_name_reg")

        self.gridLayout_2.addWidget(self.lineEdit_name_reg, 3, 1, 1, 3)

        self.pushButton_register = QPushButton(self.page_register)
        self.pushButton_register.setObjectName(u"pushButton_register")

        self.gridLayout_2.addWidget(self.pushButton_register, 5, 3, 1, 1)

        self.lineEdit_password_reg = QLineEdit(self.page_register)
        self.lineEdit_password_reg.setObjectName(u"lineEdit_password_reg")

        self.gridLayout_2.addWidget(self.lineEdit_password_reg, 4, 1, 1, 3)

        self.label_6 = QLabel(self.page_register)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_7 = QLabel(self.page_register)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.pushButton_back = QPushButton(self.page_register)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.gridLayout_2.addWidget(self.pushButton_back, 5, 2, 1, 1)

        self.lineEdit_login_reg = QLineEdit(self.page_register)
        self.lineEdit_login_reg.setObjectName(u"lineEdit_login_reg")

        self.gridLayout_2.addWidget(self.lineEdit_login_reg, 2, 1, 1, 3)

        self.label_5 = QLabel(self.page_register)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 4)

        self.stackedWidget.addWidget(self.page_register)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 33))
        self.menulog_out = QMenu(self.menubar)
        self.menulog_out.setObjectName(u"menulog_out")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menulog_out.menuAction())
        self.menulog_out.addAction(self.action_log_out)
        self.menulog_out.addAction(self.action_close_app)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_log_out.setText(QCoreApplication.translate("MainWindow", u"log out", None))
        self.action_close_app.setText(QCoreApplication.translate("MainWindow", u"close app", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.pushButton_new_account.setText(QCoreApplication.translate("MainWindow", u"New Account", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcame !", None))
        self.label_current_user.setText(QCoreApplication.translate("MainWindow", u"User :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Clients :", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.menulog_out.setTitle(QCoreApplication.translate("MainWindow", u"log out", None))
    # retranslateUi


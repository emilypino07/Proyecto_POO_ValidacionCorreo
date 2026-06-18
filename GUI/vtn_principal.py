# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 600)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblregistro = QLabel(self.centralwidget)
        self.lblregistro.setObjectName(u"lblregistro")
        self.lblregistro.setGeometry(QRect(210, 0, 321, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.lblregistro.setFont(font1)
        self.lblcodigo = QLabel(self.centralwidget)
        self.lblcodigo.setObjectName(u"lblcodigo")
        self.lblcodigo.setGeometry(QRect(100, 70, 161, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lblcodigo.setFont(font2)
        self.txtcodigo = QLineEdit(self.centralwidget)
        self.txtcodigo.setObjectName(u"txtcodigo")
        self.txtcodigo.setGeometry(QRect(260, 70, 311, 21))
        self.lblnombre = QLabel(self.centralwidget)
        self.lblnombre.setObjectName(u"lblnombre")
        self.lblnombre.setGeometry(QRect(100, 110, 161, 21))
        self.lblnombre.setFont(font2)
        self.lblfecha = QLabel(self.centralwidget)
        self.lblfecha.setObjectName(u"lblfecha")
        self.lblfecha.setGeometry(QRect(100, 150, 91, 21))
        self.lblfecha.setFont(font2)
        self.btnguardar = QPushButton(self.centralwidget)
        self.btnguardar.setObjectName(u"btnguardar")
        self.btnguardar.setGeometry(QRect(250, 240, 81, 31))
        self.btnlimpiar = QPushButton(self.centralwidget)
        self.btnlimpiar.setObjectName(u"btnlimpiar")
        self.btnlimpiar.setGeometry(QRect(410, 240, 71, 31))
        self.txtnombre = QLineEdit(self.centralwidget)
        self.txtnombre.setObjectName(u"txtnombre")
        self.txtnombre.setGeometry(QRect(260, 110, 311, 21))
        self.lblemail = QLabel(self.centralwidget)
        self.lblemail.setObjectName(u"lblemail")
        self.lblemail.setGeometry(QRect(100, 190, 71, 21))
        self.lblemail.setFont(font2)
        self.txtemail = QLineEdit(self.centralwidget)
        self.txtemail.setObjectName(u"txtemail")
        self.txtemail.setGeometry(QRect(260, 190, 311, 21))
        self.txtemail.setFont(font)
        self.tbldatos = QTableWidget(self.centralwidget)
        if (self.tbldatos.columnCount() < 4):
            self.tbldatos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbldatos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbldatos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbldatos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbldatos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbldatos.setObjectName(u"tbldatos")
        self.tbldatos.setGeometry(QRect(150, 290, 491, 221))
        self.tbldatos.setRowCount(0)
        self.tbldatos.setColumnCount(4)
        self.tbldatos.horizontalHeader().setStretchLastSection(True)
        self.dtfecha = QDateEdit(self.centralwidget)
        self.dtfecha.setObjectName(u"dtfecha")
        self.dtfecha.setGeometry(QRect(260, 150, 110, 22))
        self.dtfecha.setCalendarPopup(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 870, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblregistro.setText(QCoreApplication.translate("MainWindow", u"REGISTRO DE TRANSPORTE", None))
        self.lblcodigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo: (5 d\u00edgitos)", None))
        self.lblnombre.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.lblfecha.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.btnguardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnlimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.lblemail.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        ___qtablewidgetitem = self.tbldatos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        ___qtablewidgetitem1 = self.tbldatos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        ___qtablewidgetitem2 = self.tbldatos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        ___qtablewidgetitem3 = self.tbldatos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
    # retranslateUi


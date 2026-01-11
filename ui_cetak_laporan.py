# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cetak_laporan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 550)
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #E0E0E0;\n"
"    font-family: \"Arial\";\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #A0A0A0;\n"
"    border-radius: 5px;\n"
"    margin-top: 20px;\n"
"    background-color: #ECECEC;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    left: 10px;\n"
"    color: #333;\n"
"}\n"
"\n"
"/* Label Input Warna Kuning Krem seperti Jurnal */\n"
"QLabel#label_Mulai, QLabel#label_Sampai {\n"
"    background-color: #FFFACD;\n"
"    border: 1px solid #888888;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Judul Besar */\n"
"QLabel#label_Judul {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    font-style: italic;\n"
"    color: #000000;\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"/* Input Tanggal */\n"
"QDateEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #888888;\n"
"    padding: 5px;\n"
"    colo"
                        "r: black;\n"
"}\n"
"\n"
"/* Tabel */\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #888888;\n"
"    gridline-color: #CCCCCC;\n"
"    color: black;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #D3D3D3;\n"
"    padding: 4px;\n"
"    border: 1px solid #888888;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Tombol Klasik */\n"
"QPushButton {\n"
"    background-color: #F5F5F5;\n"
"    border: 1px solid #888888;\n"
"    border-radius: 3px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #CCCCCC;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_Judul = QLabel(self.groupBox)
        self.label_Judul.setObjectName(u"label_Judul")
        self.label_Judul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_Judul)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.label_Mulai = QLabel(self.groupBox)
        self.label_Mulai.setObjectName(u"label_Mulai")

        self.gridLayout.addWidget(self.label_Mulai, 0, 0, 1, 1)

        self.dateEdit_Mulai = QDateEdit(self.groupBox)
        self.dateEdit_Mulai.setObjectName(u"dateEdit_Mulai")
        self.dateEdit_Mulai.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_Mulai, 0, 1, 1, 1)

        self.label_Sampai = QLabel(self.groupBox)
        self.label_Sampai.setObjectName(u"label_Sampai")

        self.gridLayout.addWidget(self.label_Sampai, 1, 0, 1, 1)

        self.dateEdit_Sampai = QDateEdit(self.groupBox)
        self.dateEdit_Sampai.setObjectName(u"dateEdit_Sampai")
        self.dateEdit_Sampai.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_Sampai, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_LapPeminjaman = QPushButton(self.groupBox)
        self.btn_LapPeminjaman.setObjectName(u"btn_LapPeminjaman")

        self.verticalLayout_2.addWidget(self.btn_LapPeminjaman)

        self.btn_LapPembayaran = QPushButton(self.groupBox)
        self.btn_LapPembayaran.setObjectName(u"btn_LapPembayaran")

        self.verticalLayout_2.addWidget(self.btn_LapPembayaran)

        self.btn_LapCetak = QPushButton(self.groupBox)
        self.btn_LapCetak.setObjectName(u"btn_LapCetak")

        self.verticalLayout_2.addWidget(self.btn_LapCetak)

        self.btn_Keluar = QPushButton(self.groupBox)
        self.btn_Keluar.setObjectName(u"btn_Keluar")

        self.verticalLayout_2.addWidget(self.btn_Keluar)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Menu Laporan", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u":: LAPORAN ::", None))
        self.label_Judul.setText(QCoreApplication.translate("Form", u"Lihat Laporan", None))
        self.label_Mulai.setText(QCoreApplication.translate("Form", u"Mulai Tanggal", None))
        self.dateEdit_Mulai.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy-MM-dd", None))
        self.label_Sampai.setText(QCoreApplication.translate("Form", u"Sampai Dengan", None))
        self.dateEdit_Sampai.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy-MM-dd", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Data Preview", None));
        self.btn_LapPeminjaman.setText(QCoreApplication.translate("Form", u"Laporan Peminjaman", None))
        self.btn_LapPembayaran.setText(QCoreApplication.translate("Form", u"Laporan Pembayaran", None))
        self.btn_LapCetak.setText(QCoreApplication.translate("Form", u"Cetak Laporan", None))
        self.btn_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'konsumen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit_IdPelanggan = QLineEdit(self.groupBox)
        self.lineEdit_IdPelanggan.setObjectName(u"lineEdit_IdPelanggan")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_IdPelanggan)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_NamaPerusahaan = QLineEdit(self.groupBox)
        self.lineEdit_NamaPerusahaan.setObjectName(u"lineEdit_NamaPerusahaan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_NamaPerusahaan)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_NamaPemilik = QLineEdit(self.groupBox)
        self.lineEdit_NamaPemilik.setObjectName(u"lineEdit_NamaPemilik")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_NamaPemilik)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.textEdit_Alamat = QTextEdit(self.groupBox)
        self.textEdit_Alamat.setObjectName(u"textEdit_Alamat")
        self.textEdit_Alamat.setMaximumSize(QSize(16777215, 80))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.textEdit_Alamat)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.lineEdit_Telpon = QLineEdit(self.groupBox)
        self.lineEdit_Telpon.setObjectName(u"lineEdit_Telpon")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_Telpon)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Baru = QPushButton(self.frame)
        self.pushButton_Baru.setObjectName(u"pushButton_Baru")

        self.horizontalLayout.addWidget(self.pushButton_Baru)

        self.pushButton_Simpan = QPushButton(self.frame)
        self.pushButton_Simpan.setObjectName(u"pushButton_Simpan")

        self.horizontalLayout.addWidget(self.pushButton_Simpan)

        self.pushButton_Ubah = QPushButton(self.frame)
        self.pushButton_Ubah.setObjectName(u"pushButton_Ubah")

        self.horizontalLayout.addWidget(self.pushButton_Ubah)

        self.pushButton_Hapus = QPushButton(self.frame)
        self.pushButton_Hapus.setObjectName(u"pushButton_Hapus")

        self.horizontalLayout.addWidget(self.pushButton_Hapus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Keluar = QPushButton(self.frame)
        self.pushButton_Keluar.setObjectName(u"pushButton_Keluar")

        self.horizontalLayout.addWidget(self.pushButton_Keluar)


        self.verticalLayout.addWidget(self.frame)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form Konsumen", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"KONSUMEN:", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Pelanggan", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nama Perusahaan", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nama Pemilik", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Telpon / Fax", None))
        self.pushButton_Baru.setText(QCoreApplication.translate("Form", u"Baru", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_Ubah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushButton_Hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
    # retranslateUi


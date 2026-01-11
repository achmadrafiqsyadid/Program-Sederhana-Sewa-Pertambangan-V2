# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alat_berat.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(632, 656)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit_KodeAlat = QLineEdit(self.groupBox)
        self.lineEdit_KodeAlat.setObjectName(u"lineEdit_KodeAlat")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_KodeAlat)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_NamaAlat = QLineEdit(self.groupBox)
        self.lineEdit_NamaAlat.setObjectName(u"lineEdit_NamaAlat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_NamaAlat)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_Merk = QLineEdit(self.groupBox)
        self.lineEdit_Merk.setObjectName(u"lineEdit_Merk")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_Merk)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.comboBox_Jenis = QComboBox(self.groupBox)
        self.comboBox_Jenis.setObjectName(u"comboBox_Jenis")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboBox_Jenis)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.textEdit_Spesifikasi = QTextEdit(self.groupBox)
        self.textEdit_Spesifikasi.setObjectName(u"textEdit_Spesifikasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.textEdit_Spesifikasi)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.lineEdit_Tahun = QLineEdit(self.groupBox)
        self.lineEdit_Tahun.setObjectName(u"lineEdit_Tahun")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_Tahun)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.lineEdit_Sewa = QLineEdit(self.groupBox)
        self.lineEdit_Sewa.setObjectName(u"lineEdit_Sewa")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lineEdit_Sewa)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.comboBox_Status = QComboBox(self.groupBox)
        self.comboBox_Status.setObjectName(u"comboBox_Status")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.comboBox_Status)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form Alat Berat", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Data Alat Berat", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kode Alat", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nama Alat", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Merk", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Jenis / Tipe", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Spesifikasi", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Tahun Pembuatan", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Sewa Harian (Rp)", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Ket Pakai (Status)", None))
        self.pushButton_Baru.setText(QCoreApplication.translate("Form", u"Baru", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_Ubah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushButton_Hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
    # retranslateUi


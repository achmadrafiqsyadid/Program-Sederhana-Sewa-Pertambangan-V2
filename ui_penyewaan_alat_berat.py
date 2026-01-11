# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'penyewaan_alat_berat.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit_IdPenyewaan = QLineEdit(self.groupBox)
        self.lineEdit_IdPenyewaan.setObjectName(u"lineEdit_IdPenyewaan")
        self.lineEdit_IdPenyewaan.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_IdPenyewaan)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.dateEdit_TglSewa = QDateEdit(self.groupBox)
        self.dateEdit_TglSewa.setObjectName(u"dateEdit_TglSewa")
        self.dateEdit_TglSewa.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit_TglSewa)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.dateEdit_EstimasiKembali = QDateEdit(self.groupBox)
        self.dateEdit_EstimasiKembali.setObjectName(u"dateEdit_EstimasiKembali")
        self.dateEdit_EstimasiKembali.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit_EstimasiKembali)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.textEdit_Lokasi = QTextEdit(self.groupBox)
        self.textEdit_Lokasi.setObjectName(u"textEdit_Lokasi")
        self.textEdit_Lokasi.setMaximumSize(QSize(16777215, 60))

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.textEdit_Lokasi)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.layout_konsumen = QHBoxLayout()
        self.layout_konsumen.setObjectName(u"layout_konsumen")
        self.comboBox_Konsumen = QComboBox(self.groupBox)
        self.comboBox_Konsumen.setObjectName(u"comboBox_Konsumen")

        self.layout_konsumen.addWidget(self.comboBox_Konsumen)


        self.formLayout.setLayout(4, QFormLayout.ItemRole.FieldRole, self.layout_konsumen)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.comboBox_AlatBerat = QComboBox(self.groupBox)
        self.comboBox_AlatBerat.setObjectName(u"comboBox_AlatBerat")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboBox_AlatBerat)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.comboBox_Operator = QComboBox(self.groupBox)
        self.comboBox_Operator.setObjectName(u"comboBox_Operator")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.comboBox_Operator)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.comboBox_Status = QComboBox(self.groupBox)
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
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
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form Penyewaan Alat Berat", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"TRANSAKSI PENYEWAAN:", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Penyewaan", None))
        self.lineEdit_IdPenyewaan.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Tanggal Sewa", None))
        self.dateEdit_TglSewa.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy-MM-dd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Estimasi Kembali", None))
        self.dateEdit_EstimasiKembali.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy-MM-dd", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Lokasi Proyek", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Konsumen", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Alat Berat", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Operator", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Status", None))
        self.comboBox_Status.setItemText(0, QCoreApplication.translate("Form", u"aktif", None))
        self.comboBox_Status.setItemText(1, QCoreApplication.translate("Form", u"selesai", None))
        self.comboBox_Status.setItemText(2, QCoreApplication.translate("Form", u"dipesan", None))

        self.pushButton_Baru.setText(QCoreApplication.translate("Form", u"Baru", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_Ubah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushButton_Hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
    # retranslateUi


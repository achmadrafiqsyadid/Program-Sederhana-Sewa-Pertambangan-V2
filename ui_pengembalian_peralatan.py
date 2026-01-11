# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pengembalian_peralatan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 700)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_Atas = QGroupBox(Form)
        self.groupBox_Atas.setObjectName(u"groupBox_Atas")
        self.gridLayout = QGridLayout(self.groupBox_Atas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox_Atas)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_IdSewa = QComboBox(self.groupBox_Atas)
        self.comboBox_IdSewa.setObjectName(u"comboBox_IdSewa")

        self.gridLayout.addWidget(self.comboBox_IdSewa, 0, 1, 1, 3)

        self.label_2 = QLabel(self.groupBox_Atas)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dateEdit_TglKembaliAktual = QDateEdit(self.groupBox_Atas)
        self.dateEdit_TglKembaliAktual.setObjectName(u"dateEdit_TglKembaliAktual")
        self.dateEdit_TglKembaliAktual.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_TglKembaliAktual, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_Atas)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.lineEdit_NoPengembalian = QLineEdit(self.groupBox_Atas)
        self.lineEdit_NoPengembalian.setObjectName(u"lineEdit_NoPengembalian")
        self.lineEdit_NoPengembalian.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_NoPengembalian, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_Atas)

        self.groupBox_Pelanggan = QGroupBox(Form)
        self.groupBox_Pelanggan.setObjectName(u"groupBox_Pelanggan")
        self.gridLayout_2 = QGridLayout(self.groupBox_Pelanggan)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_Pelanggan)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_IdPel = QLineEdit(self.groupBox_Pelanggan)
        self.lineEdit_IdPel.setObjectName(u"lineEdit_IdPel")
        self.lineEdit_IdPel.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_IdPel, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_Pelanggan)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.lineEdit_NmPerusahaan = QLineEdit(self.groupBox_Pelanggan)
        self.lineEdit_NmPerusahaan.setObjectName(u"lineEdit_NmPerusahaan")
        self.lineEdit_NmPerusahaan.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_NmPerusahaan, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_Pelanggan)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_Lokasi = QLineEdit(self.groupBox_Pelanggan)
        self.lineEdit_Lokasi.setObjectName(u"lineEdit_Lokasi")
        self.lineEdit_Lokasi.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_Lokasi, 1, 1, 1, 3)


        self.verticalLayout.addWidget(self.groupBox_Pelanggan)

        self.groupBox_Alat = QGroupBox(Form)
        self.groupBox_Alat.setObjectName(u"groupBox_Alat")
        self.gridLayout_3 = QGridLayout(self.groupBox_Alat)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_Alat)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_IdAlat = QLineEdit(self.groupBox_Alat)
        self.lineEdit_IdAlat.setObjectName(u"lineEdit_IdAlat")
        self.lineEdit_IdAlat.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_IdAlat, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_Alat)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)

        self.lineEdit_NamaAlat = QLineEdit(self.groupBox_Alat)
        self.lineEdit_NamaAlat.setObjectName(u"lineEdit_NamaAlat")
        self.lineEdit_NamaAlat.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_NamaAlat, 0, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox_Alat)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineEdit_IdOp = QLineEdit(self.groupBox_Alat)
        self.lineEdit_IdOp.setObjectName(u"lineEdit_IdOp")
        self.lineEdit_IdOp.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_IdOp, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_Alat)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 2, 1, 1)

        self.lineEdit_NamaOp = QLineEdit(self.groupBox_Alat)
        self.lineEdit_NamaOp.setObjectName(u"lineEdit_NamaOp")
        self.lineEdit_NamaOp.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_NamaOp, 1, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox_Alat)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.lineEdit_TglSewa = QLineEdit(self.groupBox_Alat)
        self.lineEdit_TglSewa.setObjectName(u"lineEdit_TglSewa")
        self.lineEdit_TglSewa.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_TglSewa, 2, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_Alat)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 2, 2, 1, 1)

        self.lineEdit_EstKembali = QLineEdit(self.groupBox_Alat)
        self.lineEdit_EstKembali.setObjectName(u"lineEdit_EstKembali")
        self.lineEdit_EstKembali.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_EstKembali, 2, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_Alat)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_Keterangan = QLineEdit(self.groupBox_4)
        self.lineEdit_Keterangan.setObjectName(u"lineEdit_Keterangan")

        self.gridLayout_4.addWidget(self.lineEdit_Keterangan, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_Denda = QLineEdit(self.groupBox_4)
        self.lineEdit_Denda.setObjectName(u"lineEdit_Denda")

        self.gridLayout_4.addWidget(self.lineEdit_Denda, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Baru = QPushButton(Form)
        self.pushButton_Baru.setObjectName(u"pushButton_Baru")

        self.horizontalLayout.addWidget(self.pushButton_Baru)

        self.pushButton_Simpan = QPushButton(Form)
        self.pushButton_Simpan.setObjectName(u"pushButton_Simpan")
        self.pushButton_Simpan.setStyleSheet(u"background-color: #4CAF50; color: white; font-weight: bold;")

        self.horizontalLayout.addWidget(self.pushButton_Simpan)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Keluar = QPushButton(Form)
        self.pushButton_Keluar.setObjectName(u"pushButton_Keluar")

        self.horizontalLayout.addWidget(self.pushButton_Keluar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form Pengembalian Peralatan", None))
        self.groupBox_Atas.setTitle(QCoreApplication.translate("Form", u"Data Transaksi Pengembalian", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Pilih ID Penyewaan:", None))
#if QT_CONFIG(tooltip)
        self.comboBox_IdSewa.setToolTip(QCoreApplication.translate("Form", u"Pilih ID Penyewaan yang aktif", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Tanggal Kembali (Aktual):", None))
        self.dateEdit_TglKembaliAktual.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy-MM-dd", None))
        self.label.setText(QCoreApplication.translate("Form", u"No Pengembalian (Auto):", None))
        self.lineEdit_NoPengembalian.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis", None))
        self.groupBox_Pelanggan.setTitle(QCoreApplication.translate("Form", u"Informasi Pelanggan & Proyek (Otomatis Terisi)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ID Pelanggan:", None))
        self.lineEdit_IdPel.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Nama Perusahaan:", None))
        self.lineEdit_NmPerusahaan.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Lokasi Proyek:", None))
        self.lineEdit_Lokasi.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.groupBox_Alat.setTitle(QCoreApplication.translate("Form", u"Informasi Alat Berat & Operator (Otomatis Terisi)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"ID Alat:", None))
        self.lineEdit_IdAlat.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Nama Alat:", None))
        self.lineEdit_NamaAlat.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"ID Operator:", None))
        self.lineEdit_IdOp.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Nama Operator:", None))
        self.lineEdit_NamaOp.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Tgl Sewa Awal:", None))
        self.lineEdit_TglSewa.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Est. Kembali:", None))
        self.lineEdit_EstKembali.setPlaceholderText(QCoreApplication.translate("Form", u"Otomatis...", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Catatan & Denda", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Keterangan / Kondisi Alat:", None))
        self.lineEdit_Keterangan.setPlaceholderText(QCoreApplication.translate("Form", u"Contoh: Baik, Rusak Ringan, Kotor, dll...", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Denda (Jika ada):", None))
        self.lineEdit_Denda.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_Denda.setPlaceholderText(QCoreApplication.translate("Form", u"Input angka denda jika ada keterlambatan/kerusakan", None))
        self.pushButton_Baru.setText(QCoreApplication.translate("Form", u"Bersihkan Form", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Proses Pengembalian", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pengembalian", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tgl Kembali", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID Sewa", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kondisi", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Denda", None));
    # retranslateUi


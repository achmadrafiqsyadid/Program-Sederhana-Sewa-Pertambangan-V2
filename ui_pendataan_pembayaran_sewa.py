# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pendataan_Pembayaran_Sewa.ui'
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
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(816, 515)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_IdSewa = QComboBox(self.groupBox)
        self.comboBox_IdSewa.setObjectName(u"comboBox_IdSewa")

        self.gridLayout.addWidget(self.comboBox_IdSewa, 0, 1, 1, 3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_NamaPerusahaan = QLineEdit(self.groupBox)
        self.lineEdit_NamaPerusahaan.setObjectName(u"lineEdit_NamaPerusahaan")
        self.lineEdit_NamaPerusahaan.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_NamaPerusahaan, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.lineEdit_NamaAlat = QLineEdit(self.groupBox)
        self.lineEdit_NamaAlat.setObjectName(u"lineEdit_NamaAlat")
        self.lineEdit_NamaAlat.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_NamaAlat, 1, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.dateEdit_TglBayar = QDateEdit(self.groupBox)
        self.dateEdit_TglBayar.setObjectName(u"dateEdit_TglBayar")
        self.dateEdit_TglBayar.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_TglBayar, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.lineEdit_InfoDenda = QLineEdit(self.groupBox)
        self.lineEdit_InfoDenda.setObjectName(u"lineEdit_InfoDenda")
        self.lineEdit_InfoDenda.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_InfoDenda, 2, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.comboBox_Metode = QComboBox(self.groupBox)
        self.comboBox_Metode.addItem("")
        self.comboBox_Metode.addItem("")
        self.comboBox_Metode.setObjectName(u"comboBox_Metode")

        self.gridLayout.addWidget(self.comboBox_Metode, 3, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)

        self.lineEdit_TotalBayar = QLineEdit(self.groupBox)
        self.lineEdit_TotalBayar.setObjectName(u"lineEdit_TotalBayar")

        self.gridLayout.addWidget(self.lineEdit_TotalBayar, 3, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.textEdit_Keterangan = QTextEdit(self.groupBox)
        self.textEdit_Keterangan.setObjectName(u"textEdit_Keterangan")

        self.gridLayout.addWidget(self.textEdit_Keterangan, 4, 1, 1, 3)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Baru = QPushButton(Form)
        self.pushButton_Baru.setObjectName(u"pushButton_Baru")

        self.horizontalLayout.addWidget(self.pushButton_Baru)

        self.pushButton_Simpan = QPushButton(Form)
        self.pushButton_Simpan.setObjectName(u"pushButton_Simpan")

        self.horizontalLayout.addWidget(self.pushButton_Simpan)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Keluar = QPushButton(Form)
        self.pushButton_Keluar.setObjectName(u"pushButton_Keluar")

        self.horizontalLayout.addWidget(self.pushButton_Keluar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form Pembayaran Sewa", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Input Pembayaran", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pilih ID Sewa (Belum Lunas):", None))
#if QT_CONFIG(tooltip)
        self.comboBox_IdSewa.setToolTip(QCoreApplication.translate("Form", u"Hanya menampilkan sewa yang sudah selesai tapi belum lunas", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Nama Perusahaan:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Unit Alat:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tanggal Bayar:", None))
        self.dateEdit_TglBayar.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy-MM-dd", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Info Denda:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Metode Pembayaran:", None))
        self.comboBox_Metode.setItemText(0, QCoreApplication.translate("Form", u"Cash / Tunai", None))
        self.comboBox_Metode.setItemText(1, QCoreApplication.translate("Form", u"Transfer Bank", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Total Bayar (Rp):", None))
        self.lineEdit_TotalBayar.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Keterangan:", None))
        self.pushButton_Baru.setText(QCoreApplication.translate("Form", u"Baru", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Simpan Pembayaran", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Bayar", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tgl Bayar", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID Sewa", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Metode", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Total", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Keterangan", None));
    # retranslateUi


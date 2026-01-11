# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(452, 232)
        self.actionKonsumen = QAction(main)
        self.actionKonsumen.setObjectName(u"actionKonsumen")
        self.actionOperator = QAction(main)
        self.actionOperator.setObjectName(u"actionOperator")
        self.actionPenyewaan_Alat_Berat = QAction(main)
        self.actionPenyewaan_Alat_Berat.setObjectName(u"actionPenyewaan_Alat_Berat")
        self.actionAlat_Berat = QAction(main)
        self.actionAlat_Berat.setObjectName(u"actionAlat_Berat")
        self.actionPengembalian_Peralatan = QAction(main)
        self.actionPengembalian_Peralatan.setObjectName(u"actionPengembalian_Peralatan")
        self.actionCetak_Laporan = QAction(main)
        self.actionCetak_Laporan.setObjectName(u"actionCetak_Laporan")
        self.actionPendataan_Pembayaran_Sewa = QAction(main)
        self.actionPendataan_Pembayaran_Sewa.setObjectName(u"actionPendataan_Pembayaran_Sewa")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 452, 21))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addAction(self.actionKonsumen)
        self.menuMenu_Utama.addAction(self.actionOperator)
        self.menuMenu_Utama.addAction(self.actionPenyewaan_Alat_Berat)
        self.menuMenu_Utama.addAction(self.actionAlat_Berat)
        self.menuMenu_Utama.addAction(self.actionPengembalian_Peralatan)
        self.menuMenu_Utama.addAction(self.actionCetak_Laporan)
        self.menuMenu_Utama.addAction(self.actionPendataan_Pembayaran_Sewa)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionKonsumen.setText(QCoreApplication.translate("main", u"Konsumen", None))
        self.actionOperator.setText(QCoreApplication.translate("main", u"Operator", None))
        self.actionPenyewaan_Alat_Berat.setText(QCoreApplication.translate("main", u"Penyewaan Alat Berat", None))
        self.actionAlat_Berat.setText(QCoreApplication.translate("main", u"Alat Berat", None))
        self.actionPengembalian_Peralatan.setText(QCoreApplication.translate("main", u"Pengembalian Peralatan", None))
        self.actionCetak_Laporan.setText(QCoreApplication.translate("main", u"Cetak Laporan", None))
        self.actionPendataan_Pembayaran_Sewa.setText(QCoreApplication.translate("main", u"Pendataan Pembayaran Sewa", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("main", u"Menu Utama", None))
    # retranslateUi


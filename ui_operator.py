# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operator.ui'
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
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(597, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit_IdOperator = QLineEdit(self.groupBox)
        self.lineEdit_IdOperator.setObjectName(u"lineEdit_IdOperator")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_IdOperator)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_NamaOperator = QLineEdit(self.groupBox)
        self.lineEdit_NamaOperator.setObjectName(u"lineEdit_NamaOperator")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_NamaOperator)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineEdit_Lisensi = QLineEdit(self.groupBox)
        self.lineEdit_Lisensi.setObjectName(u"lineEdit_Lisensi")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_Lisensi)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.lineEdit_Telepon = QLineEdit(self.groupBox)
        self.lineEdit_Telepon.setObjectName(u"lineEdit_Telepon")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_Telepon)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.comboBox_Status = QComboBox(self.groupBox)
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
        self.comboBox_Status.addItem("")
        self.comboBox_Status.setObjectName(u"comboBox_Status")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox_Status)


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
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form Operator", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"DATA OPERATOR:", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID Operator", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nama Operator", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"No. Lisensi / SIO", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"No. Telepon", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Status", None))
        self.comboBox_Status.setItemText(0, QCoreApplication.translate("Form", u"tersedia", None))
        self.comboBox_Status.setItemText(1, QCoreApplication.translate("Form", u"bertugas", None))
        self.comboBox_Status.setItemText(2, QCoreApplication.translate("Form", u"cuti", None))

        self.pushButton_Baru.setText(QCoreApplication.translate("Form", u"Baru", None))
        self.pushButton_Simpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.pushButton_Ubah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.pushButton_Hapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.pushButton_Keluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_op", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nm_op", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"tgl_lahir", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"lisensi", None));
    # retranslateUi


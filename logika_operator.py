# File: logika_operator.py
# Modul Logika Operator
# Versi FINAL – stabil & production-ready

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)

# ======================================================
# IMPORT UI (HASIL COMPILE)
# ======================================================
try:
    from ui_operator import Ui_Form as Ui_OperatorForm
except ImportError:
    Ui_OperatorForm = None

from database import connect_db


class OperatorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- VALIDASI UI ---
        if Ui_OperatorForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Operator belum tersedia.\n"
                "Pastikan ui_operator.py sudah di-generate."
            )
            self.close()
            return

        # --- SETUP UI ---
        self.ui = Ui_OperatorForm()
        self.ui.setupUi(self)

        # --- DATABASE ---
        self.db = connect_db()
        if not self.db:
            QMessageBox.critical(
                self,
                "Error Database",
                "Gagal terhubung ke database."
            )
            self.close()
            return

        self.konfigurasi_tabel()
        self.hubungkan_tombol()
        self.load_data()

    # ==================================================
    # SETUP UI
    # ==================================================
    def konfigurasi_tabel(self):
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "ID Operator",
            "Nama Operator",
            "No. Lisensi",
            "No. Telepon",
            "Status"
        ])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def hubungkan_tombol(self):
        self.ui.pushButton_Baru.clicked.connect(self.bersihkan_form)
        self.ui.pushButton_Simpan.clicked.connect(self.simpan_data)
        self.ui.pushButton_Ubah.clicked.connect(self.simpan_data)
        self.ui.pushButton_Hapus.clicked.connect(self.hapus_data)
        self.ui.pushButton_Keluar.clicked.connect(self.close)
        self.ui.tableWidget.cellClicked.connect(self.data_tabel_diklik)

    # ==================================================
    # FORM
    # ==================================================
    def bersihkan_form(self):
        self.ui.lineEdit_IdOperator.clear()
        self.ui.lineEdit_NamaOperator.clear()
        self.ui.lineEdit_Lisensi.clear()
        self.ui.lineEdit_Telepon.clear()
        self.ui.comboBox_Status.setCurrentIndex(0)

        self.ui.lineEdit_IdOperator.setReadOnly(False)
        self.ui.lineEdit_IdOperator.setFocus()

    # ==================================================
    # LOAD DATA
    # ==================================================
    def load_data(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id_operator, nama_operator, no_lisensi, no_telepon, status
                FROM operator
            """)
            records = cursor.fetchall()
            cursor.close()

            self.ui.tableWidget.setRowCount(0)
            for r, row in enumerate(records):
                self.ui.tableWidget.insertRow(r)
                for c, val in enumerate(row):
                    value = "" if val is None else str(val)
                    self.ui.tableWidget.setItem(
                        r, c, QTableWidgetItem(value)
                    )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat data:\n{e}"
            )

    # ==================================================
    # SIMPAN / UPDATE
    # ==================================================
    def simpan_data(self):
        if not self.db or not self.db.is_connected():
            return

        id_op = self.ui.lineEdit_IdOperator.text().strip()
        nama = self.ui.lineEdit_NamaOperator.text().strip()
        lisensi = self.ui.lineEdit_Lisensi.text().strip()
        telepon = self.ui.lineEdit_Telepon.text().strip()
        status = self.ui.comboBox_Status.currentText()

        if not id_op or not nama:
            QMessageBox.warning(
                self,
                "Input Error",
                "ID Operator dan Nama Operator wajib diisi."
            )
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                REPLACE INTO operator
                (id_operator, nama_operator, no_lisensi, no_telepon, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                id_op, nama, lisensi, telepon, status
            ))

            self.db.commit()
            cursor.close()

            QMessageBox.information(
                self,
                "Sukses",
                "Data operator berhasil disimpan."
            )
            self.load_data()
            self.bersihkan_form()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal menyimpan data:\n{e}"
            )

    # ==================================================
    # TABLE CLICK
    # ==================================================
    def data_tabel_diklik(self, row, column):
        self.ui.lineEdit_IdOperator.setText(
            self.ui.tableWidget.item(row, 0).text()
        )
        self.ui.lineEdit_IdOperator.setReadOnly(True)

        self.ui.lineEdit_NamaOperator.setText(
            self.ui.tableWidget.item(row, 1).text()
        )
        self.ui.lineEdit_Lisensi.setText(
            self.ui.tableWidget.item(row, 2).text()
        )
        self.ui.lineEdit_Telepon.setText(
            self.ui.tableWidget.item(row, 3).text()
        )
        self.ui.comboBox_Status.setCurrentText(
            self.ui.tableWidget.item(row, 4).text()
        )

    # ==================================================
    # DELETE
    # ==================================================
    def hapus_data(self):
        id_op = self.ui.lineEdit_IdOperator.text()
        if not id_op:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Pilih data dari tabel terlebih dahulu."
            )
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus operator dengan ID {id_op}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            try:
                cursor = self.db.cursor()
                cursor.execute(
                    "DELETE FROM operator WHERE id_operator = %s",
                    (id_op,)
                )
                self.db.commit()
                cursor.close()

                QMessageBox.information(
                    self,
                    "Sukses",
                    "Data operator berhasil dihapus."
                )
                self.load_data()
                self.bersihkan_form()

            except Exception as e:
                self.db.rollback()
                QMessageBox.critical(
                    self,
                    "Database Error",
                    f"Gagal menghapus data:\n{e}"
                )

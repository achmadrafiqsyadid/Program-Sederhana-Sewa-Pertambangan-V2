# File: logika_alat_berat.py
# Modul logika Form Alat Berat
# Versi FINAL – tanpa pyside6-uic, tanpa print runtime, aman production

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)
from PySide6.QtCore import Qt

# ==========================================================
# IMPORT UI (HASIL COMPILE, BUKAN COMPILE RUNTIME)
# ==========================================================
try:
    from ui_alat_berat import Ui_Form as Ui_AlatBeratForm
except ImportError:
    Ui_AlatBeratForm = None

from database import connect_db


class AlatBeratWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- VALIDASI UI ---
        if Ui_AlatBeratForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Alat Berat belum tersedia.\n"
                "Pastikan ui_alat_berat.py sudah di-generate dari Qt Designer."
            )
            self.close()
            return

        # --- SETUP UI ---
        self.ui = Ui_AlatBeratForm()
        self.ui.setupUi(self)

        self.db = None
        self.hubungkan_ke_db()
        self.konfigurasi_tabel()
        self.isi_combobox()
        self.hubungkan_tombol()
        self.load_data()

    # ======================================================
    # DATABASE
    # ======================================================
    def hubungkan_ke_db(self):
        self.db = connect_db()
        if not self.db:
            QMessageBox.critical(
                self,
                "Error Database",
                "Tidak bisa terhubung ke database."
            )
            self.close()

    # ======================================================
    # SETUP UI
    # ======================================================
    def konfigurasi_tabel(self):
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "Kode Alat", "Nama Alat", "Merk", "Jenis/Tipe",
            "Spesifikasi", "Tahun", "Sewa Harian", "Status"
        ])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def isi_combobox(self):
        self.ui.comboBox_Status.clear()
        self.ui.comboBox_Status.addItems([
            "tersedia", "disewa", "perbaikan", "nonaktif"
        ])

        self.ui.comboBox_Jenis.clear()
        self.ui.comboBox_Jenis.addItems([
            "Dump Truck", "Tronton", "Excavator", "Bulldozer", "Bak"
        ])

    def hubungkan_tombol(self):
        self.ui.pushButton_Baru.clicked.connect(self.bersihkan_form)
        self.ui.pushButton_Simpan.clicked.connect(self.simpan_data)
        self.ui.pushButton_Ubah.clicked.connect(self.simpan_data)
        self.ui.pushButton_Hapus.clicked.connect(self.hapus_data)
        self.ui.pushButton_Keluar.clicked.connect(self.close)
        self.ui.tableWidget.cellClicked.connect(self.data_tabel_diklik)

    # ======================================================
    # FORM HANDLING
    # ======================================================
    def bersihkan_form(self):
        self.ui.lineEdit_KodeAlat.clear()
        self.ui.lineEdit_NamaAlat.clear()
        self.ui.lineEdit_Merk.clear()
        self.ui.comboBox_Jenis.setCurrentIndex(0)
        self.ui.textEdit_Spesifikasi.clear()
        self.ui.lineEdit_Tahun.clear()
        self.ui.lineEdit_Sewa.clear()
        self.ui.comboBox_Status.setCurrentIndex(0)

        self.ui.lineEdit_KodeAlat.setReadOnly(False)
        self.ui.lineEdit_KodeAlat.setFocus()

    # ======================================================
    # LOAD DATA
    # ======================================================
    def load_data(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id_alat, nama_alat, merk, jenis_alat,
                       spesifikasi, tahun_pembuatan,
                       harga_sewa_per_jam, status_alat
                FROM alat_berat
            """)
            records = cursor.fetchall()

            self.ui.tableWidget.setRowCount(0)
            for row_idx, row_data in enumerate(records):
                self.ui.tableWidget.insertRow(row_idx)
                for col_idx, data in enumerate(row_data):
                    value = "" if data is None else str(data)
                    self.ui.tableWidget.setItem(
                        row_idx, col_idx, QTableWidgetItem(value)
                    )

            cursor.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat data:\n{e}"
            )

    # ======================================================
    # SIMPAN / UPDATE
    # ======================================================
    def simpan_data(self):
        if not self.db or not self.db.is_connected():
            return

        kode = self.ui.lineEdit_KodeAlat.text().strip()
        nama = self.ui.lineEdit_NamaAlat.text().strip()
        merk = self.ui.lineEdit_Merk.text().strip()
        jenis = self.ui.comboBox_Jenis.currentText()
        spesifikasi = self.ui.textEdit_Spesifikasi.toPlainText().strip()
        status = self.ui.comboBox_Status.currentText()

        if not kode or not nama:
            QMessageBox.warning(
                self,
                "Input Error",
                "Kode Alat dan Nama Alat wajib diisi."
            )
            return

        try:
            tahun = int(self.ui.lineEdit_Tahun.text()) if self.ui.lineEdit_Tahun.text() else None
            sewa = float(self.ui.lineEdit_Sewa.text()) if self.ui.lineEdit_Sewa.text() else 0.0
        except ValueError:
            QMessageBox.warning(
                self,
                "Input Error",
                "Tahun dan Sewa Harian harus berupa angka."
            )
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                REPLACE INTO alat_berat
                (id_alat, nama_alat, merk, jenis_alat,
                 spesifikasi, tahun_pembuatan,
                 harga_sewa_per_jam, status_alat)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                kode, nama, merk, jenis,
                spesifikasi, tahun, sewa, status
            ))

            self.db.commit()
            cursor.close()

            QMessageBox.information(
                self,
                "Sukses",
                "Data alat berat berhasil disimpan."
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

    # ======================================================
    # TABLE CLICK
    # ======================================================
    def data_tabel_diklik(self, row, column):
        self.ui.lineEdit_KodeAlat.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.lineEdit_KodeAlat.setReadOnly(True)

        self.ui.lineEdit_NamaAlat.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.lineEdit_Merk.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.comboBox_Jenis.setCurrentText(self.ui.tableWidget.item(row, 3).text())

        self.ui.textEdit_Spesifikasi.setPlainText(
            self.ui.tableWidget.item(row, 4).text()
        )
        self.ui.lineEdit_Tahun.setText(
            self.ui.tableWidget.item(row, 5).text()
        )
        self.ui.lineEdit_Sewa.setText(
            self.ui.tableWidget.item(row, 6).text()
        )
        self.ui.comboBox_Status.setCurrentText(
            self.ui.tableWidget.item(row, 7).text()
        )

    # ======================================================
    # DELETE
    # ======================================================
    def hapus_data(self):
        kode = self.ui.lineEdit_KodeAlat.text()
        if not kode:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Pilih data dari tabel terlebih dahulu."
            )
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus Alat dengan Kode: {kode}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            try:
                cursor = self.db.cursor()
                cursor.execute(
                    "DELETE FROM alat_berat WHERE id_alat=%s",
                    (kode,)
                )
                self.db.commit()
                cursor.close()

                QMessageBox.information(
                    self,
                    "Sukses",
                    "Data berhasil dihapus."
                )
                self.load_data()
                self.bersihkan_form()

            except Exception as e:
                self.db.rollback()
                if "1451" in str(e):
                    QMessageBox.critical(
                        self,
                        "Database Error",
                        "Data tidak bisa dihapus karena masih dipakai di tabel Penyewaan."
                    )
                else:
                    QMessageBox.critical(
                        self,
                        "Database Error",
                        f"Gagal menghapus data:\n{e}"
                    )

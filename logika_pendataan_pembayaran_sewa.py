# File: logika_pendataan_pembayaran_sewa.py
# Modul Pembayaran Sewa
# Versi FINAL – stabil & bersih

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)
from PySide6.QtCore import QDate

# ======================================================
# IMPORT UI
# ======================================================
try:
    from ui_pendataan_pembayaran_sewa import Ui_Form as Ui_PembayaranForm
except ImportError:
    Ui_PembayaranForm = None

from database import connect_db


class PembayaranWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- VALIDASI UI ---
        if Ui_PembayaranForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Pembayaran tidak ditemukan.\n"
                "Pastikan ui_pendataan_pembayaran_sewa.py tersedia."
            )
            self.close()
            return

        # --- SETUP UI ---
        self.ui = Ui_PembayaranForm()
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

        # Default tanggal hari ini
        self.ui.dateEdit_TglBayar.setDate(QDate.currentDate())

        self.konfigurasi_tabel()
        self.hubungkan_tombol()
        self.isi_combobox_tagihan()
        self.load_data_tabel()

    # ==================================================
    # SETUP
    # ==================================================
    def konfigurasi_tabel(self):
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "ID Bayar",
            "Tanggal",
            "ID Sewa",
            "Metode",
            "Total",
            "Keterangan"
        ])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def hubungkan_tombol(self):
        self.ui.pushButton_Simpan.clicked.connect(self.simpan_pembayaran)
        self.ui.pushButton_Baru.clicked.connect(self.bersihkan_form)
        self.ui.pushButton_Keluar.clicked.connect(self.close)
        self.ui.comboBox_IdSewa.currentIndexChanged.connect(
            self.tampilkan_detail_tagihan
        )

    # ==================================================
    # COMBOBOX TAGIHAN
    # ==================================================
    def isi_combobox_tagihan(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            self.ui.comboBox_IdSewa.clear()
            self.ui.comboBox_IdSewa.addItem("- Pilih Tagihan -", None)

            cursor.execute("""
                SELECT p.id_penyewaan, k.nm_perusahaan, a.nama_alat
                FROM penyewaan p
                JOIN konsumen k ON p.id_pel_fk = k.id_pel
                JOIN alat_berat a ON p.id_alat_fk = a.id_alat
                WHERE p.status_penyewaan = 'selesai'
                  AND (p.status_pembayaran IS NULL
                       OR p.status_pembayaran = 'belum_lunas')
            """)

            for row in cursor.fetchall():
                label = f"{row[0]} | {row[1]} | {row[2]}"
                self.ui.comboBox_IdSewa.addItem(label, row[0])

            cursor.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat daftar tagihan:\n{e}"
            )

    # ==================================================
    # DETAIL TAGIHAN
    # ==================================================
    def tampilkan_detail_tagihan(self):
        id_sewa = self.ui.comboBox_IdSewa.currentData()
        if not id_sewa:
            self.bersihkan_info_detail()
            return

        try:
            cursor = self.db.cursor()

            cursor.execute("""
                SELECT k.nm_perusahaan, a.nama_alat
                FROM penyewaan p
                JOIN konsumen k ON p.id_pel_fk = k.id_pel
                JOIN alat_berat a ON p.id_alat_fk = a.id_alat
                WHERE p.id_penyewaan = %s
            """, (id_sewa,))
            info = cursor.fetchone()

            if info:
                self.ui.lineEdit_NamaPerusahaan.setText(info[0])
                self.ui.lineEdit_NamaAlat.setText(info[1])

            cursor.execute(
                "SELECT denda FROM pengembalian WHERE id_penyewaan_fk = %s",
                (id_sewa,)
            )
            row = cursor.fetchone()
            denda = row[0] if row and row[0] else 0

            self.ui.lineEdit_InfoDenda.setText(str(int(denda)))
            self.ui.lineEdit_TotalBayar.setText(str(int(denda)))

            cursor.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat detail tagihan:\n{e}"
            )

    def bersihkan_info_detail(self):
        self.ui.lineEdit_NamaPerusahaan.clear()
        self.ui.lineEdit_NamaAlat.clear()
        self.ui.lineEdit_InfoDenda.clear()
        self.ui.lineEdit_TotalBayar.setText("0")

    # ==================================================
    # FORM
    # ==================================================
    def bersihkan_form(self):
        self.ui.comboBox_IdSewa.setCurrentIndex(0)
        self.ui.comboBox_Metode.setCurrentIndex(0)
        self.ui.dateEdit_TglBayar.setDate(QDate.currentDate())
        self.ui.textEdit_Keterangan.clear()
        self.bersihkan_info_detail()
        self.isi_combobox_tagihan()

    # ==================================================
    # TABLE
    # ==================================================
    def load_data_tabel(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id_pembayaran, tgl_pembayaran,
                       id_penyewaan_fk, metode_pembayaran,
                       total_bayar, keterangan
                FROM pembayaran
                ORDER BY id_pembayaran DESC
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
                f"Gagal memuat data pembayaran:\n{e}"
            )

    # ==================================================
    # SIMPAN PEMBAYARAN
    # ==================================================
    def simpan_pembayaran(self):
        id_sewa = self.ui.comboBox_IdSewa.currentData()
        if not id_sewa:
            QMessageBox.warning(
                self,
                "Input Error",
                "Pilih tagihan sewa terlebih dahulu."
            )
            return

        try:
            total = float(self.ui.lineEdit_TotalBayar.text())
        except ValueError:
            QMessageBox.warning(
                self,
                "Input Error",
                "Total bayar harus berupa angka."
            )
            return

        tgl = self.ui.dateEdit_TglBayar.date().toString("yyyy-MM-dd")
        metode = self.ui.comboBox_Metode.currentText()
        ket = self.ui.textEdit_Keterangan.toPlainText()

        try:
            cursor = self.db.cursor()

            cursor.execute("""
                INSERT INTO pembayaran
                (tgl_pembayaran, metode_pembayaran,
                 total_bayar, keterangan, id_penyewaan_fk)
                VALUES (%s, %s, %s, %s, %s)
            """, (tgl, metode, total, ket, id_sewa))

            cursor.execute("""
                UPDATE penyewaan
                SET status_pembayaran='lunas'
                WHERE id_penyewaan=%s
            """, (id_sewa,))

            self.db.commit()
            cursor.close()

            QMessageBox.information(
                self,
                "Sukses",
                "Pembayaran berhasil disimpan."
            )

            self.bersihkan_form()
            self.load_data_tabel()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal menyimpan pembayaran:\n{e}"
            )

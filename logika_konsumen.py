# File: logika_konsumen.py
# Modul Logika Konsumen
# Versi FINAL – tanpa pyside6-uic, tanpa print runtime

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)

# ==========================================================
# IMPORT UI (HASIL COMPILE)
# ==========================================================
try:
    from ui_konsumen import Ui_Form as Ui_KonsumenForm
except ImportError:
    Ui_KonsumenForm = None

from database import connect_db


class KonsumenWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- VALIDASI UI ---
        if Ui_KonsumenForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Konsumen belum tersedia.\n"
                "Pastikan ui_konsumen.py sudah di-generate."
            )
            self.close()
            return

        # --- SETUP UI ---
        self.ui = Ui_KonsumenForm()
        self.ui.setupUi(self)

        # --- DATABASE ---
        self.db = connect_db()
        if not self.db:
            QMessageBox.critical(
                self,
                "Error Database",
                "Tidak bisa terhubung ke database."
            )
            self.close()
            return

        self.konfigurasi_tabel()
        self.hubungkan_tombol()
        self.load_data()

    # ======================================================
    # SETUP UI
    # ======================================================
    def konfigurasi_tabel(self):
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "ID Pelanggan",
            "Nama Perusahaan",
            "Nama Pemilik",
            "Alamat",
            "Telpon / Fax"
        ])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

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
        self.ui.lineEdit_IdPelanggan.clear()
        self.ui.lineEdit_NamaPerusahaan.clear()
        self.ui.lineEdit_NamaPemilik.clear()
        self.ui.textEdit_Alamat.clear()
        self.ui.lineEdit_Telpon.clear()

        self.ui.lineEdit_IdPelanggan.setReadOnly(False)
        self.ui.lineEdit_IdPelanggan.setFocus()

    # ======================================================
    # LOAD DATA
    # ======================================================
    def load_data(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id_pel, nm_perusahaan, nm_pemilik, alamat, telp_fax
                FROM konsumen
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

    # ======================================================
    # SIMPAN / UPDATE
    # ======================================================
    def simpan_data(self):
        if not self.db or not self.db.is_connected():
            return

        id_pel = self.ui.lineEdit_IdPelanggan.text().strip()
        nm_perusahaan = self.ui.lineEdit_NamaPerusahaan.text().strip()
        nm_pemilik = self.ui.lineEdit_NamaPemilik.text().strip()
        alamat = self.ui.textEdit_Alamat.toPlainText().strip()
        telp_fax = self.ui.lineEdit_Telpon.text().strip()

        if not id_pel or not nm_perusahaan:
            QMessageBox.warning(
                self,
                "Input Error",
                "ID Pelanggan dan Nama Perusahaan wajib diisi."
            )
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                REPLACE INTO konsumen
                (id_pel, nm_perusahaan, nm_pemilik, alamat, telp_fax)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                id_pel, nm_perusahaan, nm_pemilik, alamat, telp_fax
            ))

            self.db.commit()
            cursor.close()

            QMessageBox.information(
                self,
                "Sukses",
                "Data konsumen berhasil disimpan."
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
        self.ui.lineEdit_IdPelanggan.setText(
            self.ui.tableWidget.item(row, 0).text()
        )
        self.ui.lineEdit_IdPelanggan.setReadOnly(True)

        self.ui.lineEdit_NamaPerusahaan.setText(
            self.ui.tableWidget.item(row, 1).text()
        )
        self.ui.lineEdit_NamaPemilik.setText(
            self.ui.tableWidget.item(row, 2).text()
        )
        self.ui.textEdit_Alamat.setPlainText(
            self.ui.tableWidget.item(row, 3).text()
        )
        self.ui.lineEdit_Telpon.setText(
            self.ui.tableWidget.item(row, 4).text()
        )

    # ======================================================
    # DELETE
    # ======================================================
    def hapus_data(self):
        id_pel = self.ui.lineEdit_IdPelanggan.text()
        if not id_pel:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Pilih data dari tabel terlebih dahulu."
            )
            return

        konfirmasi = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus konsumen dengan ID: {id_pel}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if konfirmasi == QMessageBox.Yes:
            try:
                cursor = self.db.cursor()
                cursor.execute(
                    "DELETE FROM konsumen WHERE id_pel = %s",
                    (id_pel,)
                )
                self.db.commit()
                cursor.close()

                QMessageBox.information(
                    self,
                    "Sukses",
                    "Data konsumen berhasil dihapus."
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

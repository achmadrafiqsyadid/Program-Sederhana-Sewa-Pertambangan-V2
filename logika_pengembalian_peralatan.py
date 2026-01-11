# File: logika_pengembalian_peralatan.py
# Modul Pengembalian Alat
# Versi FINAL – stabil & konsisten

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QLineEdit, QTextEdit
)
from PySide6.QtCore import QDate

# ======================================================
# IMPORT UI
# ======================================================
try:
    from ui_pengembalian_peralatan import Ui_Form as Ui_PengembalianForm
except ImportError:
    Ui_PengembalianForm = None

from database import connect_db


class PengembalianWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- VALIDASI UI ---
        if Ui_PengembalianForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Pengembalian tidak ditemukan.\n"
                "Pastikan ui_pengembalian_peralatan.py tersedia."
            )
            self.close()
            return

        # --- SETUP UI ---
        self.ui = Ui_PengembalianForm()
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

        # Set tanggal default
        if hasattr(self.ui, 'dateEdit_TglKembaliAktual'):
            self.ui.dateEdit_TglKembaliAktual.setDate(QDate.currentDate())
        else:
            self.ui.dateEdit_TglKembali.setDate(QDate.currentDate())

        self.konfigurasi_tabel()
        self.hubungkan_tombol()
        self.isi_combobox_sewa_aktif()
        self.load_data_tabel()

    # ==================================================
    # SETUP
    # ==================================================
    def konfigurasi_tabel(self):
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "ID Kembali",
            "ID Sewa",
            "Tanggal Kembali",
            "Kondisi",
            "Denda"
        ])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def hubungkan_tombol(self):
        tombol = [
            'pushButton_Simpan',
            'pushButton_Proses',
            'pushButton_ProsesPengembalian'
        ]
        for t in tombol:
            if hasattr(self.ui, t):
                getattr(self.ui, t).clicked.connect(self.simpan_pengembalian)
                break

        self.ui.pushButton_Baru.clicked.connect(self.bersihkan_form)
        self.ui.pushButton_Keluar.clicked.connect(self.close)

        if hasattr(self.ui, 'comboBox_IdSewa'):
            self.ui.comboBox_IdSewa.currentIndexChanged.connect(
                self.tampilkan_detail_sewa
            )
        else:
            self.ui.comboBox_IdPenyewaan.currentIndexChanged.connect(
                self.tampilkan_detail_sewa
            )

    # ==================================================
    # COMBOBOX
    # ==================================================
    def isi_combobox_sewa_aktif(self):
        if not self.db or not self.db.is_connected():
            return

        combo = (
            self.ui.comboBox_IdSewa
            if hasattr(self.ui, 'comboBox_IdSewa')
            else self.ui.comboBox_IdPenyewaan
        )

        try:
            cursor = self.db.cursor()
            combo.clear()
            combo.addItem("- Pilih ID Sewa -", None)

            cursor.execute("""
                SELECT p.id_penyewaan, k.nm_perusahaan, a.nama_alat
                FROM penyewaan p
                JOIN konsumen k ON p.id_pel_fk = k.id_pel
                JOIN alat_berat a ON p.id_alat_fk = a.id_alat
                WHERE p.status_penyewaan IN ('disewa', 'aktif')
            """)

            for row in cursor.fetchall():
                label = f"{row[0]} | {row[1]} | {row[2]}"
                combo.addItem(label, row[0])

            cursor.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat data penyewaan:\n{e}"
            )

    # ==================================================
    # DETAIL SEWA
    # ==================================================
    def get_input_keterangan(self):
        for name in [
            'lineEdit_Keterangan', 'textEdit_Keterangan',
            'lineEdit_Kondisi', 'textEdit_Kondisi'
        ]:
            if hasattr(self.ui, name):
                widget = getattr(self.ui, name)
                if isinstance(widget, QLineEdit):
                    return widget.text(), widget
                if isinstance(widget, QTextEdit):
                    return widget.toPlainText(), widget
        return "", None

    def tampilkan_detail_sewa(self):
        id_sewa = (
            self.ui.comboBox_IdSewa.currentData()
            if hasattr(self.ui, 'comboBox_IdSewa')
            else self.ui.comboBox_IdPenyewaan.currentData()
        )

        if not id_sewa:
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT k.nm_perusahaan, a.nama_alat
                FROM penyewaan p
                JOIN konsumen k ON p.id_pel_fk = k.id_pel
                JOIN alat_berat a ON p.id_alat_fk = a.id_alat
                WHERE p.id_penyewaan=%s
            """, (id_sewa,))
            row = cursor.fetchone()

            if row:
                if hasattr(self.ui, 'lineEdit_NamaPerusahaan'):
                    self.ui.lineEdit_NamaPerusahaan.setText(row[0])
                if hasattr(self.ui, 'lineEdit_NamaAlat'):
                    self.ui.lineEdit_NamaAlat.setText(row[1])

            cursor.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat detail sewa:\n{e}"
            )

    # ==================================================
    # FORM
    # ==================================================
    def bersihkan_form(self):
        if hasattr(self.ui, 'comboBox_IdSewa'):
            self.ui.comboBox_IdSewa.setCurrentIndex(0)
        else:
            self.ui.comboBox_IdPenyewaan.setCurrentIndex(0)

        if hasattr(self.ui, 'dateEdit_TglKembaliAktual'):
            self.ui.dateEdit_TglKembaliAktual.setDate(QDate.currentDate())
        else:
            self.ui.dateEdit_TglKembali.setDate(QDate.currentDate())

        teks, widget = self.get_input_keterangan()
        if widget:
            widget.clear()

        if hasattr(self.ui, 'lineEdit_Denda'):
            self.ui.lineEdit_Denda.setText("0")

        self.isi_combobox_sewa_aktif()

    # ==================================================
    # TABLE
    # ==================================================
    def load_data_tabel(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id_kembali, id_penyewaan_fk,
                       tgl_kembali, kondisi_alat, denda
                FROM pengembalian
                ORDER BY id_kembali DESC
            """)
            data = cursor.fetchall()
            cursor.close()

            self.ui.tableWidget.setRowCount(0)
            for r, row in enumerate(data):
                self.ui.tableWidget.insertRow(r)
                for c, val in enumerate(row):
                    self.ui.tableWidget.setItem(
                        r, c, QTableWidgetItem("" if val is None else str(val))
                    )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat data pengembalian:\n{e}"
            )

    # ==================================================
    # SIMPAN
    # ==================================================
    def simpan_pengembalian(self):
        id_sewa = (
            self.ui.comboBox_IdSewa.currentData()
            if hasattr(self.ui, 'comboBox_IdSewa')
            else self.ui.comboBox_IdPenyewaan.currentData()
        )

        if not id_sewa:
            QMessageBox.warning(
                self,
                "Input Error",
                "Pilih transaksi penyewaan terlebih dahulu."
            )
            return

        try:
            denda = float(self.ui.lineEdit_Denda.text())
        except Exception:
            QMessageBox.warning(
                self,
                "Input Error",
                "Denda harus berupa angka."
            )
            return

        kondisi, _ = self.get_input_keterangan()
        tanggal = (
            self.ui.dateEdit_TglKembaliAktual.date().toString("yyyy-MM-dd")
            if hasattr(self.ui, 'dateEdit_TglKembaliAktual')
            else self.ui.dateEdit_TglKembali.date().toString("yyyy-MM-dd")
        )

        try:
            cursor = self.db.cursor()

            cursor.execute("""
                SELECT id_alat_fk, id_operator_fk
                FROM penyewaan WHERE id_penyewaan=%s
            """, (id_sewa,))
            alat, operator = cursor.fetchone()

            cursor.execute("""
                INSERT INTO pengembalian
                (tgl_kembali, kondisi_alat, denda, id_penyewaan_fk)
                VALUES (%s, %s, %s, %s)
            """, (tanggal, kondisi, denda, id_sewa))

            cursor.execute("""
                UPDATE penyewaan
                SET status_penyewaan='selesai'
                WHERE id_penyewaan=%s
            """, (id_sewa,))

            cursor.execute(
                "UPDATE alat_berat SET status_alat='tersedia' WHERE id_alat=%s",
                (alat,)
            )

            if operator:
                cursor.execute(
                    "UPDATE operator SET status='tersedia' WHERE id_operator=%s",
                    (operator,)
                )

            self.db.commit()
            cursor.close()

            QMessageBox.information(
                self,
                "Sukses",
                "Pengembalian berhasil diproses."
            )

            self.bersihkan_form()
            self.load_data_tabel()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memproses pengembalian:\n{e}"
            )

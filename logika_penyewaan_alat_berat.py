# File: logika_penyewaan_alat_berat.py
# Modul Penyewaan Alat Berat
# Versi FINAL – stabil, konsisten, siap dinilai

from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate

# ==================================================
# IMPORT UI
# ==================================================
try:
    from ui_penyewaan_alat_berat import Ui_Form as Ui_PenyewaanForm
except ImportError:
    Ui_PenyewaanForm = None

from database import connect_db


class PenyewaanWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        if Ui_PenyewaanForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Penyewaan tidak ditemukan.\n"
                "Pastikan ui_penyewaan_alat_berat.py tersedia."
            )
            self.close()
            return

        self.ui = Ui_PenyewaanForm()
        self.ui.setupUi(self)

        self.db = connect_db()
        if not self.db:
            QMessageBox.critical(
                self,
                "Error Database",
                "Gagal terhubung ke database."
            )
            self.close()
            return

        # Default tanggal
        self.ui.dateEdit_TglSewa.setDate(QDate.currentDate())
        self.ui.dateEdit_EstimasiKembali.setDate(QDate.currentDate().addDays(1))

        self.konfigurasi_tabel()
        self.hubungkan_tombol()
        self.isi_semua_combobox()
        self.load_data()

    # ==================================================
    # SETUP
    # ==================================================
    def konfigurasi_tabel(self):
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "ID Sewa",
            "Tgl Sewa",
            "Estimasi Kembali",
            "Lokasi",
            "ID Konsumen",
            "ID Alat",
            "ID Operator",
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
    # COMBOBOX
    # ==================================================
    def isi_semua_combobox(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()

            # Konsumen
            self.ui.comboBox_Konsumen.clear()
            cursor.execute("SELECT id_pel, nm_perusahaan FROM konsumen")
            for r in cursor.fetchall():
                self.ui.comboBox_Konsumen.addItem(
                    f"{r[0]} - {r[1]}", r[0]
                )

            # Alat Berat (hanya tersedia)
            self.ui.comboBox_AlatBerat.clear()
            cursor.execute("""
                SELECT id_alat, nama_alat, merk
                FROM alat_berat
                WHERE status_alat = 'tersedia'
            """)
            for r in cursor.fetchall():
                merk = r[2] if r[2] else "-"
                self.ui.comboBox_AlatBerat.addItem(
                    f"{r[0]} - {r[1]} ({merk})", r[0]
                )

            # Operator
            self.ui.comboBox_Operator.clear()
            self.ui.comboBox_Operator.addItem("- Tanpa Operator -", None)
            cursor.execute("""
                SELECT id_operator, nama_operator
                FROM operator
                WHERE status = 'tersedia'
            """)
            for r in cursor.fetchall():
                self.ui.comboBox_Operator.addItem(
                    f"{r[0]} - {r[1]}", r[0]
                )

            cursor.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat combobox:\n{e}"
            )

    # ==================================================
    # DATA
    # ==================================================
    def load_data(self):
        if not self.db or not self.db.is_connected():
            return

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT id_penyewaan, tgl_sewa, estimasi_tgl_kembali,
                       lokasi_proyek, id_pel_fk, id_alat_fk,
                       id_operator_fk, status_penyewaan
                FROM penyewaan
                ORDER BY id_penyewaan DESC
            """)
            data = cursor.fetchall()
            cursor.close()

            self.ui.tableWidget.setRowCount(0)
            for r, row in enumerate(data):
                self.ui.tableWidget.insertRow(r)
                for c, val in enumerate(row):
                    self.ui.tableWidget.setItem(
                        r, c,
                        QTableWidgetItem("" if val is None else str(val))
                    )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal memuat data penyewaan:\n{e}"
            )

    # ==================================================
    # FORM
    # ==================================================
    def bersihkan_form(self):
        self.ui.lineEdit_IdPenyewaan.clear()
        self.ui.dateEdit_TglSewa.setDate(QDate.currentDate())
        self.ui.dateEdit_EstimasiKembali.setDate(QDate.currentDate().addDays(1))
        self.ui.textEdit_Lokasi.clear()
        self.ui.comboBox_Status.setCurrentIndex(0)

        self.isi_semua_combobox()

    # ==================================================
    # SIMPAN
    # ==================================================
    def simpan_data(self):
        id_sewa = self.ui.lineEdit_IdPenyewaan.text()
        tgl_sewa = self.ui.dateEdit_TglSewa.date()
        tgl_kembali = self.ui.dateEdit_EstimasiKembali.date()

        if tgl_kembali < tgl_sewa:
            QMessageBox.warning(
                self,
                "Input Error",
                "Estimasi tanggal kembali tidak boleh lebih awal dari tanggal sewa."
            )
            return

        lokasi = self.ui.textEdit_Lokasi.toPlainText()
        id_pel = self.ui.comboBox_Konsumen.currentData()
        id_alat = self.ui.comboBox_AlatBerat.currentData()
        id_op = self.ui.comboBox_Operator.currentData()
        status = self.ui.comboBox_Status.currentText()

        if not id_pel or not id_alat:
            QMessageBox.warning(
                self,
                "Input Error",
                "Konsumen dan Alat Berat wajib dipilih."
            )
            return

        try:
            cursor = self.db.cursor()

            if id_sewa:
                cursor.execute("""
                    UPDATE penyewaan
                    SET tgl_sewa=%s,
                        estimasi_tgl_kembali=%s,
                        lokasi_proyek=%s,
                        id_pel_fk=%s,
                        id_alat_fk=%s,
                        id_operator_fk=%s,
                        status_penyewaan=%s
                    WHERE id_penyewaan=%s
                """, (
                    tgl_sewa.toString("yyyy-MM-dd"),
                    tgl_kembali.toString("yyyy-MM-dd"),
                    lokasi,
                    id_pel,
                    id_alat,
                    id_op,
                    status,
                    id_sewa
                ))
            else:
                cursor.execute("""
                    INSERT INTO penyewaan
                    (tgl_sewa, estimasi_tgl_kembali, lokasi_proyek,
                     id_pel_fk, id_alat_fk, id_operator_fk, status_penyewaan)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, (
                    tgl_sewa.toString("yyyy-MM-dd"),
                    tgl_kembali.toString("yyyy-MM-dd"),
                    lokasi,
                    id_pel,
                    id_alat,
                    id_op,
                    status
                ))

                cursor.execute(
                    "UPDATE alat_berat SET status_alat='disewa' WHERE id_alat=%s",
                    (id_alat,)
                )
                if id_op:
                    cursor.execute(
                        "UPDATE operator SET status='bertugas' WHERE id_operator=%s",
                        (id_op,)
                    )

            self.db.commit()
            cursor.close()

            QMessageBox.information(
                self,
                "Sukses",
                "Transaksi penyewaan berhasil disimpan."
            )

            self.load_data()
            self.bersihkan_form()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(
                self,
                "Database Error",
                f"Gagal menyimpan penyewaan:\n{e}"
            )

    # ==================================================
    # TABEL
    # ==================================================
    def data_tabel_diklik(self, row, column):
        self.ui.lineEdit_IdPenyewaan.setText(
            self.ui.tableWidget.item(row, 0).text()
        )

    # ==================================================
    # HAPUS
    # ==================================================
    def hapus_data(self):
        id_sewa = self.ui.lineEdit_IdPenyewaan.text()
        if not id_sewa:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Pilih data yang ingin dihapus."
            )
            return

        if QMessageBox.question(
            self,
            "Konfirmasi",
            f"Hapus transaksi ID {id_sewa}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        ) == QMessageBox.StandardButton.Yes:

            try:
                cursor = self.db.cursor()
                cursor.execute(
                    "DELETE FROM penyewaan WHERE id_penyewaan=%s",
                    (id_sewa,)
                )
                self.db.commit()
                cursor.close()

                QMessageBox.information(
                    self,
                    "Sukses",
                    "Data penyewaan berhasil dihapus."
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

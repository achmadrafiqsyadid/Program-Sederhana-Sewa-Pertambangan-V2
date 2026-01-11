# File: logika_cetak_laporan.py
# Modul Laporan (Preview & Cetak PDF)
# Versi FINAL – tanpa pyside6-uic, tanpa print runtime

from PySide6.QtWidgets import (
    QWidget, QMessageBox, QFileDialog,
    QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import QDate
from PySide6.QtGui import QTextDocument, QPageSize
from PySide6.QtPrintSupport import QPrinter

# ==========================================================
# IMPORT UI (HASIL COMPILE)
# ==========================================================
try:
    from ui_cetak_laporan import Ui_Form as Ui_LaporanForm
except ImportError:
    Ui_LaporanForm = None

from database import connect_db


class LaporanWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- VALIDASI UI ---
        if Ui_LaporanForm is None:
            QMessageBox.critical(
                self,
                "Error UI",
                "File UI Laporan belum tersedia.\n"
                "Pastikan ui_cetak_laporan.py sudah di-generate."
            )
            self.close()
            return

        # --- SETUP UI ---
        self.ui = Ui_LaporanForm()
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

        # Menyimpan jenis laporan aktif
        self.jenis_laporan_aktif = None

        # --- SET DEFAULT TANGGAL ---
        hari_ini = QDate.currentDate()
        awal_bulan = QDate(hari_ini.year(), hari_ini.month(), 1)
        self.ui.dateEdit_Mulai.setDate(awal_bulan)
        self.ui.dateEdit_Sampai.setDate(hari_ini)

        # --- SETUP TABEL ---
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # --- HUBUNGKAN TOMBOL ---
        self.ui.btn_LapPeminjaman.clicked.connect(self.tampilkan_peminjaman)
        self.ui.btn_LapPembayaran.clicked.connect(self.tampilkan_pembayaran)
        self.ui.btn_Keluar.clicked.connect(self.close)

        if hasattr(self.ui, "btn_LapCetak"):
            self.ui.btn_LapCetak.clicked.connect(self.proses_cetak_pdf)

    # ======================================================
    # PREVIEW LAPORAN PEMINJAMAN
    # ======================================================
    def tampilkan_peminjaman(self):
        self.jenis_laporan_aktif = "PEMINJAMAN"

        tgl_mulai = self.ui.dateEdit_Mulai.date().toString("yyyy-MM-dd")
        tgl_sampai = self.ui.dateEdit_Sampai.date().toString("yyyy-MM-dd")

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT p.id_penyewaan, p.tgl_sewa,
                       k.nm_perusahaan, a.nama_alat,
                       o.nama_operator, p.status_penyewaan
                FROM penyewaan p
                JOIN konsumen k ON p.id_pel_fk = k.id_pel
                JOIN alat_berat a ON p.id_alat_fk = a.id_alat
                LEFT JOIN operator o ON p.id_operator_fk = o.id_operator
                WHERE p.tgl_sewa BETWEEN %s AND %s
            """, (tgl_mulai, tgl_sampai))
            data = cursor.fetchall()
            cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Gagal mengambil data:\n{e}")
            return

        self._isi_tabel(
            ["ID", "Tgl Sewa", "Perusahaan", "Alat", "Operator", "Status"],
            data,
            kolom_operator=4
        )

    # ======================================================
    # PREVIEW LAPORAN PEMBAYARAN
    # ======================================================
    def tampilkan_pembayaran(self):
        self.jenis_laporan_aktif = "PEMBAYARAN"

        tgl_mulai = self.ui.dateEdit_Mulai.date().toString("yyyy-MM-dd")
        tgl_sampai = self.ui.dateEdit_Sampai.date().toString("yyyy-MM-dd")

        try:
            cursor = self.db.cursor()
            cursor.execute("""
                SELECT b.id_pembayaran, b.tgl_pembayaran,
                       k.nm_perusahaan, b.metode_pembayaran,
                       b.total_bayar, b.keterangan
                FROM pembayaran b
                JOIN penyewaan p ON b.id_penyewaan_fk = p.id_penyewaan
                JOIN konsumen k ON p.id_pel_fk = k.id_pel
                WHERE b.tgl_pembayaran BETWEEN %s AND %s
            """, (tgl_mulai, tgl_sampai))
            data = cursor.fetchall()
            cursor.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Gagal mengambil data:\n{e}")
            return

        self.ui.tableWidget.clear()
        headers = ["ID Bayar", "Tgl Bayar", "Perusahaan", "Metode", "Total (Rp)", "Keterangan"]
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setRowCount(0)

        for r, row in enumerate(data):
            self.ui.tableWidget.insertRow(r)
            for c, val in enumerate(row):
                if c == 4:
                    val = "{:,.0f}".format(val)
                self.ui.tableWidget.setItem(r, c, QTableWidgetItem(str(val)))

    # ======================================================
    # CETAK PDF
    # ======================================================
    def proses_cetak_pdf(self):
        if self.jenis_laporan_aktif is None:
            QMessageBox.warning(
                self,
                "Peringatan",
                "Tampilkan laporan terlebih dahulu sebelum mencetak."
            )
            return

        if self.jenis_laporan_aktif == "PEMINJAMAN":
            self._cetak_peminjaman()
        elif self.jenis_laporan_aktif == "PEMBAYARAN":
            self._cetak_pembayaran()

    # ======================================================
    # CETAK PEMINJAMAN
    # ======================================================
    def _cetak_peminjaman(self):
        tgl_mulai = self.ui.dateEdit_Mulai.date().toString("yyyy-MM-dd")
        tgl_sampai = self.ui.dateEdit_Sampai.date().toString("yyyy-MM-dd")

        cursor = self.db.cursor()
        cursor.execute("""
            SELECT p.id_penyewaan, p.tgl_sewa,
                   k.nm_perusahaan, a.nama_alat,
                   o.nama_operator, p.status_penyewaan
            FROM penyewaan p
            JOIN konsumen k ON p.id_pel_fk = k.id_pel
            JOIN alat_berat a ON p.id_alat_fk = a.id_alat
            LEFT JOIN operator o ON p.id_operator_fk = o.id_operator
            WHERE p.tgl_sewa BETWEEN %s AND %s
        """, (tgl_mulai, tgl_sampai))
        data = cursor.fetchall()
        cursor.close()

        if not data:
            QMessageBox.information(self, "Info", "Data kosong.")
            return

        html = f"""
        <h2 align='center'>LAPORAN PEMINJAMAN ALAT BERAT</h2>
        <p align='center'>Periode: {tgl_mulai} s/d {tgl_sampai}</p>
        <table border='1' cellspacing='0' cellpadding='5' width='100%'>
        <tr bgcolor='#CCCCCC'>
            <th>ID</th><th>Tgl Sewa</th><th>Perusahaan</th>
            <th>Alat</th><th>Operator</th><th>Status</th>
        </tr>
        """
        for r in data:
            html += f"""
            <tr>
                <td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td>
                <td>{r[3]}</td><td>{r[4] or '-'}</td><td>{r[5]}</td>
            </tr>
            """
        html += "</table>"

        self._simpan_pdf(html, "Laporan_Peminjaman")

    # ======================================================
    # CETAK PEMBAYARAN
    # ======================================================
    def _cetak_pembayaran(self):
        tgl_mulai = self.ui.dateEdit_Mulai.date().toString("yyyy-MM-dd")
        tgl_sampai = self.ui.dateEdit_Sampai.date().toString("yyyy-MM-dd")

        cursor = self.db.cursor()
        cursor.execute("""
            SELECT b.id_pembayaran, b.tgl_pembayaran,
                   k.nm_perusahaan, b.metode_pembayaran,
                   b.total_bayar, b.keterangan
            FROM pembayaran b
            JOIN penyewaan p ON b.id_penyewaan_fk = p.id_penyewaan
            JOIN konsumen k ON p.id_pel_fk = k.id_pel
            WHERE b.tgl_pembayaran BETWEEN %s AND %s
        """, (tgl_mulai, tgl_sampai))
        data = cursor.fetchall()
        cursor.close()

        if not data:
            QMessageBox.information(self, "Info", "Data kosong.")
            return

        total = sum(row[4] for row in data)

        html = f"""
        <h2 align='center'>LAPORAN PEMBAYARAN SEWA</h2>
        <p align='center'>Periode: {tgl_mulai} s/d {tgl_sampai}</p>
        <table border='1' cellspacing='0' cellpadding='5' width='100%'>
        <tr bgcolor='#CCCCCC'>
            <th>ID</th><th>Tgl Bayar</th><th>Perusahaan</th>
            <th>Metode</th><th>Total</th><th>Keterangan</th>
        </tr>
        """
        for r in data:
            html += f"""
            <tr>
                <td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td>
                <td>{r[3]}</td><td align='right'>{r[4]:,.0f}</td><td>{r[5]}</td>
            </tr>
            """
        html += f"""
        <tr>
            <td colspan='4' align='right'><b>TOTAL</b></td>
            <td align='right'><b>Rp {total:,.0f}</b></td>
            <td></td>
        </tr>
        </table>
        """

        self._simpan_pdf(html, "Laporan_Pembayaran")

    # ======================================================
    # SIMPAN PDF
    # ======================================================
    def _simpan_pdf(self, html, default_name):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Simpan PDF",
            f"{default_name}.pdf",
            "PDF Files (*.pdf)"
        )

        if not filename:
            return

        if not filename.endswith(".pdf"):
            filename += ".pdf"

        doc = QTextDocument()
        doc.setHtml(html)

        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        printer.setPageSize(QPageSize(QPageSize.A4))

        doc.print_(printer)

        QMessageBox.information(
            self,
            "Sukses",
            f"Laporan berhasil disimpan:\n{filename}"
        )

    # ======================================================
    # HELPER ISI TABEL
    # ======================================================
    def _isi_tabel(self, headers, data, kolom_operator=None):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setRowCount(0)

        for r, row in enumerate(data):
            self.ui.tableWidget.insertRow(r)
            for c, val in enumerate(row):
                if kolom_operator is not None and c == kolom_operator:
                    val = val or "-"
                self.ui.tableWidget.setItem(r, c, QTableWidgetItem(str(val)))

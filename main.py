import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# ============================================================
# PENTING:
# - File ui_form.py HARUS SUDAH ADA
# - Compile UI dilakukan MANUAL, BUKAN saat runtime
# ============================================================

try:
    from ui_form import Ui_main
except ImportError:
    QMessageBox.critical(
        None,
        "Fatal Error",
        "File 'ui_form.py' tidak ditemukan.\n\n"
        "Pastikan Anda sudah menjalankan:\n"
        "pyside6-uic form.ui -o ui_form.py"
    )
    sys.exit(1)

# ============================================================
# IMPORT WINDOW LOGIKA
# ============================================================

try:
    from logika_konsumen import KonsumenWindow
except ImportError:
    KonsumenWindow = None

try:
    from logika_alat_berat import AlatBeratWindow
except ImportError:
    AlatBeratWindow = None

try:
    from logika_operator import OperatorWindow
except ImportError:
    OperatorWindow = None

try:
    from logika_penyewaan_alat_berat import PenyewaanWindow
except ImportError:
    PenyewaanWindow = None

try:
    from logika_pengembalian_peralatan import PengembalianWindow
except ImportError:
    PengembalianWindow = None

try:
    from logika_pendataan_pembayaran_sewa import PembayaranWindow
except ImportError:
    PembayaranWindow = None

try:
    from logika_cetak_laporan import LaporanWindow
except ImportError:
    LaporanWindow = None

# ============================================================
# MAIN WINDOW
# ============================================================

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)

        self.window_konsumen = None
        self.window_alat_berat = None
        self.window_operator = None
        self.window_penyewaan = None
        self.window_pengembalian = None
        self.window_pembayaran = None
        self.window_laporan = None

        self._hubungkan_menu()

    # ========================================================
    # HUBUNGKAN MENU
    # ========================================================

    def _hubungkan_menu(self):

        if hasattr(self.ui, "actionKonsumen"):
            self.ui.actionKonsumen.triggered.connect(self.tampilkan_konsumen)

        if hasattr(self.ui, "actionAlat_Berat"):
            self.ui.actionAlat_Berat.triggered.connect(self.tampilkan_alat_berat)

        if hasattr(self.ui, "actionOperator"):
            self.ui.actionOperator.triggered.connect(self.tampilkan_operator)

        if hasattr(self.ui, "actionPenyewaan_Alat_Berat"):
            self.ui.actionPenyewaan_Alat_Berat.triggered.connect(self.tampilkan_penyewaan)

        if hasattr(self.ui, "actionPengembalian_Peralatan"):
            self.ui.actionPengembalian_Peralatan.triggered.connect(self.tampilkan_pengembalian)

        if hasattr(self.ui, "actionPendataan_Pembayaran_Sewa"):
            self.ui.actionPendataan_Pembayaran_Sewa.triggered.connect(self.tampilkan_pembayaran)

        if hasattr(self.ui, "actionCetak_Laporan"):
            self.ui.actionCetak_Laporan.triggered.connect(self.tampilkan_laporan)

    # ========================================================
    # FUNGSI BUKA WINDOW
    # ========================================================

    def tampilkan_konsumen(self):
        if KonsumenWindow is None:
            QMessageBox.warning(self, "Error", "Modul Konsumen tidak tersedia.")
            return
        if self.window_konsumen is None:
            self.window_konsumen = KonsumenWindow()
        self.window_konsumen.show()
        self.window_konsumen.raise_()

    def tampilkan_alat_berat(self):
        if AlatBeratWindow is None:
            QMessageBox.warning(self, "Error", "Modul Alat Berat tidak tersedia.")
            return
        if self.window_alat_berat is None:
            self.window_alat_berat = AlatBeratWindow()
        self.window_alat_berat.show()
        self.window_alat_berat.raise_()

    def tampilkan_operator(self):
        if OperatorWindow is None:
            QMessageBox.warning(self, "Error", "Modul Operator tidak tersedia.")
            return
        if self.window_operator is None:
            self.window_operator = OperatorWindow()
        self.window_operator.show()
        self.window_operator.raise_()

    def tampilkan_penyewaan(self):
        if PenyewaanWindow is None:
            QMessageBox.warning(self, "Error", "Modul Penyewaan tidak tersedia.")
            return
        if self.window_penyewaan is None:
            self.window_penyewaan = PenyewaanWindow()
        self.window_penyewaan.show()
        self.window_penyewaan.raise_()

    def tampilkan_pengembalian(self):
        if PengembalianWindow is None:
            QMessageBox.warning(self, "Error", "Modul Pengembalian tidak tersedia.")
            return
        if self.window_pengembalian is None:
            self.window_pengembalian = PengembalianWindow()
        self.window_pengembalian.show()
        self.window_pengembalian.raise_()

    def tampilkan_pembayaran(self):
        if PembayaranWindow is None:
            QMessageBox.warning(self, "Error", "Modul Pembayaran tidak tersedia.")
            return
        if self.window_pembayaran is None:
            self.window_pembayaran = PembayaranWindow()
        self.window_pembayaran.show()
        self.window_pembayaran.raise_()

    def tampilkan_laporan(self):
        if LaporanWindow is None:
            QMessageBox.warning(self, "Error", "Modul Laporan tidak tersedia.")
            return
        if self.window_laporan is None:
            self.window_laporan = LaporanWindow()
        self.window_laporan.show()
        self.window_laporan.raise_()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

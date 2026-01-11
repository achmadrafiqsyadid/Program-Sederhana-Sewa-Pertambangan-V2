import os

# Nama file desain (dari Qt Designer)
input_file = "pengembalian_peralatan.ui"
# Nama file output (yang dicari program)
output_file = "ui_Pengembalian_Peralatan.py"

print(f"Sedang mengubah {input_file} menjadi {output_file}...")

# Jalankan perintah konversi
exit_code = os.system(f"pyside6-uic {input_file} -o {output_file}")

if exit_code == 0:
    print("✅ BERHASIL! File UI Python sudah dibuat.")
    print("Sekarang coba jalankan main.py lagi.")
else:
    print("❌ GAGAL. Pastikan file 'pengembalian_peralatan.ui' ada di folder ini.")

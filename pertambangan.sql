-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Nov 2025 pada 03.38
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pertambangan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alat_berat`
--

CREATE TABLE `alat_berat` (
  `id_alat` varchar(10) NOT NULL,
  `nama_alat` varchar(100) NOT NULL,
  `jenis_alat` varchar(50) DEFAULT NULL,
  `merk` varchar(50) DEFAULT NULL,
  `harga_sewa_per_jam` decimal(10,2) NOT NULL,
  `status_alat` enum('tersedia','disewa','perbaikan') DEFAULT 'tersedia'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `cetak_laporan`
--

CREATE TABLE `cetak_laporan` (
  `id_laporan` int(11) NOT NULL,
  `nama_laporan` varchar(255) NOT NULL,
  `tgl_dibuat` timestamp NOT NULL DEFAULT current_timestamp(),
  `dibuat_oleh` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `konsumen`
--

CREATE TABLE `konsumen` (
  `id_pel` varchar(10) NOT NULL,
  `nm_perusahaan` varchar(100) DEFAULT NULL,
  `nm_pemilik` varchar(100) DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `telp_fax` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `konsumen`
--

INSERT INTO `konsumen` (`id_pel`, `nm_perusahaan`, `nm_pemilik`, `alamat`, `telp_fax`) VALUES
('1', 'yasuga', 'Nama Pemilik', 'veteran', '08213759'),
('2', 'momoji', 'Nama Pemilik', 'handil', '0971563');

-- --------------------------------------------------------

--
-- Struktur dari tabel `operator`
--

CREATE TABLE `operator` (
  `id_operator` varchar(10) NOT NULL,
  `nama_operator` varchar(100) NOT NULL,
  `no_lisensi` varchar(50) DEFAULT NULL,
  `no_telepon` varchar(20) DEFAULT NULL,
  `status` enum('tersedia','bertugas','cuti') DEFAULT 'tersedia'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pembayaran`
--

CREATE TABLE `pembayaran` (
  `id_pembayaran` int(11) NOT NULL,
  `tgl_bayar` date NOT NULL,
  `jumlah_bayar` decimal(10,2) NOT NULL,
  `metode_bayar` varchar(50) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `id_penyewaan_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengembalian`
--

CREATE TABLE `pengembalian` (
  `id_pengembalian` int(11) NOT NULL,
  `tgl_kembali_aktual` datetime NOT NULL,
  `total_jam_pakai` int(11) DEFAULT NULL,
  `kondisi_alat_saat_kembali` text DEFAULT NULL,
  `diterima_oleh` varchar(100) DEFAULT NULL,
  `id_penyewaan_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `penyewaan`
--

CREATE TABLE `penyewaan` (
  `id_penyewaan` int(11) NOT NULL,
  `tgl_sewa` datetime NOT NULL,
  `estimasi_tgl_kembali` datetime DEFAULT NULL,
  `lokasi_proyek` text DEFAULT NULL,
  `status_penyewaan` enum('aktif','selesai','dipesan') DEFAULT 'aktif',
  `id_pel_fk` varchar(10) DEFAULT NULL,
  `id_alat_fk` varchar(10) DEFAULT NULL,
  `id_operator_fk` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alat_berat`
--
ALTER TABLE `alat_berat`
  ADD PRIMARY KEY (`id_alat`);

--
-- Indeks untuk tabel `cetak_laporan`
--
ALTER TABLE `cetak_laporan`
  ADD PRIMARY KEY (`id_laporan`);

--
-- Indeks untuk tabel `konsumen`
--
ALTER TABLE `konsumen`
  ADD PRIMARY KEY (`id_pel`);

--
-- Indeks untuk tabel `operator`
--
ALTER TABLE `operator`
  ADD PRIMARY KEY (`id_operator`);

--
-- Indeks untuk tabel `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`id_pembayaran`),
  ADD KEY `id_penyewaan_fk` (`id_penyewaan_fk`);

--
-- Indeks untuk tabel `pengembalian`
--
ALTER TABLE `pengembalian`
  ADD PRIMARY KEY (`id_pengembalian`),
  ADD KEY `id_penyewaan_fk` (`id_penyewaan_fk`);

--
-- Indeks untuk tabel `penyewaan`
--
ALTER TABLE `penyewaan`
  ADD PRIMARY KEY (`id_penyewaan`),
  ADD KEY `id_pel_fk` (`id_pel_fk`),
  ADD KEY `id_alat_fk` (`id_alat_fk`),
  ADD KEY `id_operator_fk` (`id_operator_fk`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `cetak_laporan`
--
ALTER TABLE `cetak_laporan`
  MODIFY `id_laporan` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `pembayaran`
--
ALTER TABLE `pembayaran`
  MODIFY `id_pembayaran` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `pengembalian`
--
ALTER TABLE `pengembalian`
  MODIFY `id_pengembalian` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `penyewaan`
--
ALTER TABLE `penyewaan`
  MODIFY `id_penyewaan` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`id_penyewaan_fk`) REFERENCES `penyewaan` (`id_penyewaan`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `pengembalian`
--
ALTER TABLE `pengembalian`
  ADD CONSTRAINT `pengembalian_ibfk_1` FOREIGN KEY (`id_penyewaan_fk`) REFERENCES `penyewaan` (`id_penyewaan`) ON DELETE SET NULL;

--
-- Ketidakleluasaan untuk tabel `penyewaan`
--
ALTER TABLE `penyewaan`
  ADD CONSTRAINT `penyewaan_ibfk_1` FOREIGN KEY (`id_pel_fk`) REFERENCES `konsumen` (`id_pel`),
  ADD CONSTRAINT `penyewaan_ibfk_2` FOREIGN KEY (`id_alat_fk`) REFERENCES `alat_berat` (`id_alat`),
  ADD CONSTRAINT `penyewaan_ibfk_3` FOREIGN KEY (`id_operator_fk`) REFERENCES `operator` (`id_operator`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

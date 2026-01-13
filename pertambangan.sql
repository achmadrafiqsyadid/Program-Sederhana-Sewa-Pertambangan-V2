-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Jan 2026 pada 17.31
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
  `merk` varchar(50) DEFAULT NULL,
  `jenis_alat` varchar(50) DEFAULT NULL,
  `spesifikasi` text DEFAULT NULL,
  `tahun_pembuatan` int(11) DEFAULT NULL,
  `harga_sewa_per_jam` decimal(12,2) DEFAULT NULL,
  `status_alat` enum('tersedia','disewa','perbaikan','nonaktif') DEFAULT 'tersedia'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `alat_berat`
--

INSERT INTO `alat_berat` (`id_alat`, `nama_alat`, `merk`, `jenis_alat`, `spesifikasi`, `tahun_pembuatan`, `harga_sewa_per_jam`, `status_alat`) VALUES
('AB-001', 'Truck Double Gardan 2', 'Hyno Lohan', 'Dump Truck', 'Kapasitas 20 Ton, 6 Roda', 2018, 1500000.00, 'disewa'),
('AB-002', 'Truck Double Gardan 4', 'Hyno', 'Tronton', 'Kapasitas 30 Ton, 10 Roda', 2020, 2500000.00, 'tersedia'),
('AB-003', 'Excavator PC200', 'Komatsu', 'Excavator', 'Standard bucket 0.8m3, AC Cabin', 2019, 1800000.00, 'disewa'),
('AB-004', 'Bulldozer D85', 'Caterpillar', 'Bulldozer', 'Ripper, 3.5m blade width', 2017, 2000000.00, 'perbaikan'),
('AB-005', 'Excavator PC300', 'Komatsu', 'Excavator', 'Bucket 1.4 m3, AC Cabin', 2021, 2200000.00, 'tersedia'),
('AB-006', 'Excavator 320D', 'Caterpillar', 'Excavator', 'Bucket 1.2 m3, AC Cabin', 2019, 2000000.00, 'disewa'),
('AB-007', 'Bulldozer D65', 'Komatsu', 'Bulldozer', 'Blade 3.7m, Ripper', 2018, 2100000.00, 'disewa'),
('AB-008', 'Bulldozer D155', 'Komatsu', 'Bulldozer', 'Blade 4.2m, Heavy Duty', 2020, 2600000.00, 'perbaikan'),
('AB-009', 'Wheel Loader WA380', 'Komatsu', 'Wheel Loader', 'Bucket 3.2 m3', 2019, 1900000.00, 'tersedia'),
('AB-010', 'Wheel Loader 950H', 'Caterpillar', 'Wheel Loader', 'Bucket 3.1 m3', 2017, 1800000.00, 'disewa'),
('AB-011', 'Dump Truck HD785', 'Komatsu', 'Dump Truck', 'Kapasitas 60 Ton', 2016, 3500000.00, 'tersedia'),
('AB-012', 'Dump Truck HD465', 'Komatsu', 'Dump Truck', 'Kapasitas 55 Ton', 2018, 3300000.00, 'disewa'),
('AB-013', 'Motor Grader GD705', 'Komatsu', 'Motor Grader', 'Blade 3.7m', 2020, 2400000.00, 'tersedia'),
('AB-014', 'Motor Grader 140K', 'Caterpillar', 'Motor Grader', 'Blade 3.6m', 2019, 2300000.00, 'tersedia'),
('AB-015', 'Vibro Roller BW213', 'Bomag', 'Compactor', 'Drum 2.1m', 2017, 1700000.00, 'disewa'),
('AB-016', 'Vibro Roller SD100', 'Sakai', 'Compactor', 'Drum 2.0m', 2018, 1650000.00, 'tersedia'),
('AB-017', 'Crane RT50', 'Tadano', 'Crane', 'Kapasitas 50 Ton', 2016, 4000000.00, 'perbaikan'),
('AB-018', 'Crane RT70', 'Kato', 'Crane', 'Kapasitas 70 Ton', 2019, 4500000.00, 'tersedia'),
('AB-019', 'Backhoe Loader 3DX', 'JCB', 'Backhoe Loader', 'Bucket 1.0 m3', 2021, 1600000.00, 'tersedia'),
('AB-020', 'Backhoe Loader B877', 'Hidromek', 'Backhoe Loader', 'Bucket 1.1 m3', 2020, 1700000.00, 'disewa'),
('AB-021', 'Asphalt Finisher ABG6820', 'Volvo', 'Asphalt Finisher', 'Lebar hampar 6.5m', 2018, 2800000.00, 'tersedia'),
('AB-022', 'Asphalt Finisher AP655', 'Caterpillar', 'Asphalt Finisher', 'Lebar hampar 6.0m', 2019, 2900000.00, 'disewa'),
('AB-023', 'Drilling Rig SR155', 'Sany', 'Drilling Rig', 'Kedalaman 56m', 2020, 5000000.00, 'tersedia'),
('AB-024', 'Drilling Rig BG28', 'Bauer', 'Drilling Rig', 'Kedalaman 70m', 2017, 5500000.00, 'perbaikan'),
('AC-0079', 'truck', 'hyno', 'Tronton', '20Ton', 2012, 15000000.00, 'disewa');

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

--
-- Dumping data untuk tabel `cetak_laporan`
--

INSERT INTO `cetak_laporan` (`id_laporan`, `nama_laporan`, `tgl_dibuat`, `dibuat_oleh`) VALUES
(1, 'Laporan Penyewaan Januari 2026', '2026-01-11 14:35:07', 'admin'),
(2, 'Laporan Pembayaran Januari 2026', '2026-01-11 14:35:07', 'admin'),
(3, 'Laporan Pengembalian Januari 2026', '2026-01-11 14:35:07', 'admin'),
(4, 'Laporan Denda Januari 2026', '2026-01-11 14:35:07', 'admin'),
(5, 'Laporan Alat Berat', '2026-01-11 14:35:07', 'admin'),
(6, 'Laporan Konsumen', '2026-01-11 14:35:07', 'admin'),
(7, 'Laporan Operator', '2026-01-11 14:35:07', 'admin'),
(8, 'Laporan Penyewaan Mingguan', '2026-01-11 14:35:07', 'admin'),
(9, 'Laporan Pembayaran Mingguan', '2026-01-11 14:35:07', 'admin'),
(10, 'Laporan Pengembalian Mingguan', '2026-01-11 14:35:07', 'admin'),
(11, 'Laporan Penyewaan Bulanan', '2026-01-11 14:35:07', 'admin'),
(12, 'Laporan Pembayaran Bulanan', '2026-01-11 14:35:07', 'admin'),
(13, 'Laporan Pengembalian Bulanan', '2026-01-11 14:35:07', 'admin'),
(14, 'Laporan Denda Bulanan', '2026-01-11 14:35:07', 'admin'),
(15, 'Laporan Alat Paling Sering Disewa', '2026-01-11 14:35:07', 'admin'),
(16, 'Laporan Operator Aktif', '2026-01-11 14:35:07', 'admin'),
(17, 'Laporan Penyewaan Aktif', '2026-01-11 14:35:07', 'admin'),
(18, 'Laporan Riwayat Penyewaan', '2026-01-11 14:35:07', 'admin'),
(19, 'Laporan Keuangan', '2026-01-11 14:35:07', 'admin'),
(20, 'Laporan Rekapitulasi Tahunan', '2026-01-11 14:35:07', 'admin');

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
('AB-001', 'momogi', 'rofi', 'aliali', '082973732'),
('KP-002', 'PT Bara Jaya', 'Andi Saputra', 'Balikpapan', '081234567801'),
('KP-003', 'CV Tambang Makmur', 'Budi Santoso', 'Samarinda', '081234567802'),
('KP-004', 'PT Mineral Nusantara', 'Rizal Akbar', 'Banjarmasin', '081234567803'),
('KP-005', 'PT Energi Kalimantan', 'Hendra Wijaya', 'Kutai Kartanegara', '081234567804'),
('KP-006', 'CV Sumber Alam', 'Fajar Pratama', 'Balikpapan', '081234567805'),
('KP-007', 'PT Mega Tambang', 'Arief Rahman', 'Sangatta', '081234567806'),
('KP-008', 'PT Batu Hitam', 'Doni Kurniawan', 'Samarinda', '081234567807'),
('KP-009', 'CV Karya Mandiri', 'Agus Salim', 'Bontang', '081234567808'),
('KP-010', 'PT Mitra Energi', 'Yusuf Maulana', 'Balikpapan', '081234567809'),
('KP-011', 'PT Alam Sejahtera', 'Rudi Hartono', 'Penajam', '081234567810'),
('KP-012', 'CV Putra Jaya', 'Ilham Fauzi', 'Samarinda', '081234567811'),
('KP-013', 'PT Daya Mineral', 'Eko Prasetyo', 'Kutai Timur', '081234567812'),
('KP-014', 'PT Sinar Borneo', 'Zainal Abidin', 'Banjarmasin', '081234567813'),
('KP-015', 'CV Cahaya Tambang', 'Wahyu Nugroho', 'Balikpapan', '081234567814'),
('KP-016', 'PT Global Mining', 'Irwan Setiawan', 'Sangatta', '081234567815'),
('KP-017', 'PT Kalimantan Raya', 'Rahmat Hidayat', 'Samarinda', '081234567816'),
('KP-018', 'CV Prima Jasa', 'Dedi Firmansyah', 'Bontang', '081234567817'),
('KP-019', 'PT Indo Mineral', 'Ahmad Fauzan', 'Kutai Kartanegara', '081234567818'),
('KP-020', 'PT Borneo Coal', 'Slamet Riyadi', 'Balikpapan', '081234567819'),
('KP-021', 'CV Multi Karya', 'Taufik Hidayat', 'Penajam', '081234567820');

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

--
-- Dumping data untuk tabel `operator`
--

INSERT INTO `operator` (`id_operator`, `nama_operator`, `no_lisensi`, `no_telepon`, `status`) VALUES
('OP-001', 'Budi Santoso', 'BII-Umum', '08123456789', 'tersedia'),
('OP-002', 'Agus Salim', 'SIO-Excavator', '08987654321', 'bertugas'),
('OP-003', 'Rudi Hartono', 'SIO-Bulldozer', '081234567801', 'tersedia'),
('OP-004', 'Deni Prasetyo', 'SIO-Excavator', '081234567802', 'bertugas'),
('OP-005', 'Ahmad Fauzi', 'SIO-Dump Truck', '081234567803', 'tersedia'),
('OP-006', 'Hendra Gunawan', 'SIO-Wheel Loader', '081234567804', 'bertugas'),
('OP-007', 'Eko Saputra', 'SIO-Motor Grader', '081234567805', 'bertugas'),
('OP-008', 'Fajar Nugroho', 'SIO-Excavator', '081234567806', 'bertugas'),
('OP-009', 'Ilham Maulana', 'SIO-Bulldozer', '081234567807', 'tersedia'),
('OP-010', 'Arif Setiawan', 'SIO-Dump Truck', '081234567808', 'bertugas'),
('OP-011', 'Rizki Ramadhan', 'SIO-Wheel Loader', '081234567809', 'tersedia'),
('OP-012', 'Yudi Santoso', 'SIO-Compactor', '081234567810', 'tersedia'),
('OP-013', 'Bagus Pratama', 'SIO-Crane', '081234567811', 'bertugas'),
('OP-014', 'Agung Wibowo', 'SIO-Backhoe Loader', '081234567812', 'tersedia'),
('OP-015', 'Taufik Hidayat', 'SIO-Asphalt Finisher', '081234567813', 'bertugas'),
('OP-016', 'Rian Kurniawan', 'SIO-Excavator', '081234567814', 'tersedia'),
('OP-017', 'Dimas Saputro', 'SIO-Dump Truck', '081234567815', 'tersedia'),
('OP-018', 'Bayu Permana', 'SIO-Bulldozer', '081234567816', 'bertugas'),
('OP-019', 'Roni Firmansyah', 'SIO-Wheel Loader', '081234567817', 'tersedia'),
('OP-020', 'Yoga Pratama', 'SIO-Motor Grader', '081234567818', 'bertugas'),
('OP-021', 'Andika Saputra', 'SIO-Compactor', '081234567819', 'tersedia'),
('OP-022', 'Surya Wijaya', 'SIO-Crane', '081234567820', 'tersedia'),
('OP-70', 'Ajem', 'SIO Bulldozer', '0878677856', 'tersedia');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pembayaran`
--

CREATE TABLE `pembayaran` (
  `id_pembayaran` int(11) NOT NULL,
  `tgl_pembayaran` date DEFAULT NULL,
  `metode_pembayaran` varchar(50) DEFAULT NULL,
  `total_bayar` decimal(15,2) DEFAULT NULL,
  `keterangan` text DEFAULT NULL,
  `id_penyewaan_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pembayaran`
--

INSERT INTO `pembayaran` (`id_pembayaran`, `tgl_pembayaran`, `metode_pembayaran`, `total_bayar`, `keterangan`, `id_penyewaan_fk`) VALUES
(1, '2026-01-09', 'Transfer Bank', 2000000.00, 'terlambat', 2),
(22, '2026-01-01', 'Transfer Bank', 500000.00, 'lunas', 2),
(23, '2026-01-02', 'Cash', 750000.00, 'lunas', 2),
(24, '2026-01-03', 'Transfer Bank', 600000.00, 'lunas', 2),
(25, '2026-01-04', 'Cash', 450000.00, 'lunas', 2),
(26, '2026-01-05', 'Transfer Bank', 800000.00, 'lunas', 2),
(27, '2026-01-06', 'Cash', 700000.00, 'lunas', 2),
(28, '2026-01-07', 'Transfer Bank', 650000.00, 'lunas', 2),
(29, '2026-01-08', 'Cash', 900000.00, 'lunas', 2),
(30, '2026-01-09', 'Transfer Bank', 550000.00, 'lunas', 2),
(31, '2026-01-10', 'Cash', 600000.00, 'lunas', 2),
(32, '2026-01-11', 'Transfer Bank', 750000.00, 'lunas', 2),
(33, '2026-01-12', 'Cash', 500000.00, 'lunas', 2),
(34, '2026-01-13', 'Transfer Bank', 850000.00, 'lunas', 2),
(35, '2026-01-14', 'Cash', 650000.00, 'lunas', 2),
(36, '2026-01-15', 'Transfer Bank', 700000.00, 'lunas', 2),
(37, '2026-01-16', 'Cash', 550000.00, 'lunas', 2),
(38, '2026-01-17', 'Transfer Bank', 900000.00, 'lunas', 2),
(39, '2026-01-18', 'Cash', 800000.00, 'lunas', 2),
(40, '2026-01-19', 'Transfer Bank', 600000.00, 'lunas', 2),
(41, '2026-01-20', 'Cash', 750000.00, 'lunas', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengembalian`
--

CREATE TABLE `pengembalian` (
  `id_kembali` int(11) NOT NULL,
  `tgl_kembali` date DEFAULT NULL,
  `kondisi_alat` varchar(255) DEFAULT NULL,
  `denda` decimal(15,2) DEFAULT NULL,
  `id_penyewaan_fk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pengembalian`
--

INSERT INTO `pengembalian` (`id_kembali`, `tgl_kembali`, `kondisi_alat`, `denda`, `id_penyewaan_fk`) VALUES
(1, '2026-01-16', 'rusak', 2000000.00, 2),
(2, '2026-01-01', 'baik', 0.00, 2),
(3, '2026-01-02', 'baik', 0.00, 2),
(4, '2026-01-03', 'lecet', 50000.00, 2),
(5, '2026-01-04', 'baik', 0.00, 2),
(6, '2026-01-05', 'rusak ringan', 150000.00, 2),
(7, '2026-01-06', 'baik', 0.00, 2),
(8, '2026-01-07', 'lecet', 75000.00, 2),
(9, '2026-01-08', 'baik', 0.00, 2),
(10, '2026-01-09', 'rusak ringan', 200000.00, 2),
(11, '2026-01-10', 'baik', 0.00, 2),
(12, '2026-01-11', 'lecet', 50000.00, 2),
(13, '2026-01-12', 'baik', 0.00, 2),
(14, '2026-01-13', 'rusak sedang', 300000.00, 2),
(15, '2026-01-14', 'baik', 0.00, 2),
(16, '2026-01-15', 'lecet', 100000.00, 2),
(17, '2026-01-16', 'baik', 0.00, 2),
(18, '2026-01-17', 'rusak ringan', 150000.00, 2),
(19, '2026-01-18', 'baik', 0.00, 2),
(20, '2026-01-19', 'lecet', 75000.00, 2),
(21, '2026-01-20', 'baik', 0.00, 2);

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
  `id_operator_fk` varchar(10) DEFAULT NULL,
  `status_pembayaran` enum('lunas','belum_lunas') DEFAULT 'belum_lunas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penyewaan`
--

INSERT INTO `penyewaan` (`id_penyewaan`, `tgl_sewa`, `estimasi_tgl_kembali`, `lokasi_proyek`, `status_penyewaan`, `id_pel_fk`, `id_alat_fk`, `id_operator_fk`, `status_pembayaran`) VALUES
(2, '2026-01-09 00:00:00', '2026-01-10 00:00:00', 'tamiang layang', 'selesai', 'AB-001', 'AB-002', 'OP-001', 'lunas'),
(43, '2026-01-01 08:00:00', '2026-01-05 08:00:00', 'Tambang Alpha', 'selesai', 'KP-002', 'AB-001', 'OP-001', 'lunas'),
(44, '2026-01-02 08:00:00', '2026-01-06 08:00:00', 'Tambang Beta', 'selesai', 'KP-003', 'AB-002', 'OP-002', 'lunas'),
(45, '2026-01-03 08:00:00', '2026-01-07 08:00:00', 'Tambang Gamma', 'selesai', 'KP-004', 'AB-003', 'OP-003', 'lunas'),
(46, '2026-01-04 08:00:00', '2026-01-08 08:00:00', 'Tambang Delta', 'selesai', 'KP-005', 'AB-004', 'OP-004', 'lunas'),
(47, '2026-01-05 08:00:00', '2026-01-09 08:00:00', 'Tambang Epsilon', 'selesai', 'KP-006', 'AB-005', 'OP-005', 'lunas'),
(48, '2026-01-06 08:00:00', '2026-01-10 08:00:00', 'Tambang Zeta', 'selesai', 'KP-007', 'AB-006', 'OP-006', 'lunas'),
(49, '2026-01-07 08:00:00', '2026-01-11 08:00:00', 'Tambang Eta', 'selesai', 'KP-008', 'AB-007', 'OP-007', 'lunas'),
(50, '2026-01-08 08:00:00', '2026-01-12 08:00:00', 'Tambang Theta', 'selesai', 'KP-009', 'AB-008', 'OP-008', 'lunas'),
(51, '2026-01-09 08:00:00', '2026-01-13 08:00:00', 'Tambang Iota', 'selesai', 'KP-010', 'AB-009', 'OP-009', 'lunas'),
(52, '2026-01-10 08:00:00', '2026-01-14 08:00:00', 'Tambang Kappa', 'selesai', 'KP-011', 'AB-010', 'OP-010', 'lunas'),
(53, '2026-01-11 08:00:00', '2026-01-16 08:00:00', 'Tambang Lambda', 'aktif', 'KP-012', 'AB-002', 'OP-001', 'belum_lunas'),
(54, '2026-01-12 08:00:00', '2026-01-17 08:00:00', 'Tambang Mu', 'aktif', 'KP-013', 'AB-003', 'OP-002', 'belum_lunas'),
(55, '2026-01-13 08:00:00', '2026-01-18 08:00:00', 'Tambang Nu', 'aktif', 'KP-014', 'AB-004', 'OP-003', 'belum_lunas'),
(56, '2026-01-14 08:00:00', '2026-01-19 08:00:00', 'Tambang Xi', 'aktif', 'KP-015', 'AB-005', 'OP-004', 'belum_lunas'),
(57, '2026-01-15 08:00:00', '2026-01-20 08:00:00', 'Tambang Omicron', 'aktif', 'KP-016', 'AB-006', 'OP-005', 'belum_lunas'),
(58, '2026-01-16 08:00:00', NULL, 'Tambang Pi', 'dipesan', 'KP-017', 'AB-007', 'OP-006', 'belum_lunas'),
(59, '2026-01-17 08:00:00', NULL, 'Tambang Rho', 'dipesan', 'KP-018', 'AB-008', 'OP-007', 'belum_lunas'),
(60, '2026-01-18 08:00:00', NULL, 'Tambang Sigma', 'dipesan', 'KP-019', 'AB-009', 'OP-008', 'belum_lunas'),
(61, '2026-01-19 08:00:00', NULL, 'Tambang Tau', 'dipesan', 'KP-020', 'AB-010', 'OP-009', 'belum_lunas'),
(62, '2026-01-20 08:00:00', NULL, 'Tambang Upsilon', 'dipesan', 'KP-021', 'AB-001', 'OP-010', 'belum_lunas'),
(63, '2026-01-01 00:00:00', '2026-01-30 00:00:00', '', 'aktif', 'KP-005', 'AB-007', 'OP-007', 'belum_lunas');

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
  ADD PRIMARY KEY (`id_kembali`);

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
  MODIFY `id_laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT untuk tabel `pembayaran`
--
ALTER TABLE `pembayaran`
  MODIFY `id_pembayaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT untuk tabel `pengembalian`
--
ALTER TABLE `pengembalian`
  MODIFY `id_kembali` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT untuk tabel `penyewaan`
--
ALTER TABLE `penyewaan`
  MODIFY `id_penyewaan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`id_penyewaan_fk`) REFERENCES `penyewaan` (`id_penyewaan`) ON DELETE CASCADE;

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

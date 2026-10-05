# Pertemuan 06 Nested Loop Python

**Nama:** Firgi Erviansyah
**NIM:** 2225250170
**Kelas:** 3B

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Struktur Folder

```text
pertemuan-06-nested-loop-NIM/
├── README.md
├── .gitignore
├── Kuis.docx
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
└── tugas/
    └── tabel_perkalian_dan_statistik.py
```

## Cara Menjalankan

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

* **Loop luar (`i`)** berperan mengatur baris pada tabel perkalian.
* **Loop dalam (`j`)** berperan memproses setiap nilai pada baris.
* **Akumulator (`total_baris` dan `total_semua`)** digunakan untuk menjumlahkan hasil perkalian.
* **Counter (`count_genap`)** digunakan untuk menghitung jumlah hasil perkalian yang bernilai genap.

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Keluaran Aktual       | Status   |
| ----- | --------------------- | --------------------- | -------- |
| 1     | Total = 1, Genap = 0  | Total = 1, Genap = 0  | Berhasil |
| 2     | Total = 9, Genap = 3  | Total = 9, Genap = 3  | Berhasil |
| 3     | Total = 36, Genap = 5 | Total = 36, Genap = 5 | Berhasil |

## Analisis Efisiensi

Untuk input `n`, badan loop dalam berjalan sebanyak `n × n` atau `n²` kali.

Contoh:

* `n = 1` → 1 kali
* `n = 2` → 4 kali
* `n = 3` → 9 kali

## Refleksi

Salah satu kesalahan yang perlu diperhatikan dalam nested loop adalah posisi inisialisasi `total_baris`. Jika `total_baris` tidak di-reset pada setiap pergantian baris, hasil dari baris sebelumnya akan ikut terakumulasi.

Perbaikannya adalah menempatkan `total_baris = 0` di dalam loop luar, sebelum loop dalam dijalankan.
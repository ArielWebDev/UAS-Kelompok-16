Berikut adalah file `readme.md` yang lebih rinci dengan penjelasan di setiap bagian:

```markdown
# Rental Kendaraan App

Aplikasi Rental Kendaraan sederhana dengan tiga modul utama: Mobil, Format, dan Pemesanan. Dibuat untuk memahami konsep OOP (Object-Oriented Programming) dan modularisasi dalam Python.

## Struktur Proyek

- `main.py`: Program utama untuk menjalankan aplikasi.
- `program_format.py`: Modul untuk kelas `Format` yang menangani pemformatan uang dan waktu.
- `program_mobil.py`: Modul untuk kelas `Mobil` yang mengelola daftar mobil.
- `program_pemesanan.py`: Modul untuk kelas `Pemesanan` yang membuat pemesanan, menghitung pembayaran, dan menulis ke file.
- `readme.md`: Dokumen ini memberikan panduan penggunaan dan struktur proyek.

## Instalasi

1. Pastikan Python telah terinstal di sistem Anda.
2. Unduh repositori ini atau _clone_ menggunakan perintah:
   ```
   git clone https://github.com/namauser/rental-kendaraan-app.git
   ```
3. Masuk ke direktori proyek:
   ```
   cd rental-kendaraan-app
   ```

## Penggunaan

1. Jalankan `main.py` untuk memulai program Rental Kendaraan.
2. Pilih menu:
    - 1. Tambah Mobil
    - 2. Daftar Mobil
    - 3. Buat Pemesanan
    - 4. Keluar

## Modul

### Program Format (`program_format.py`)

Modul ini menyediakan kelas `Format` untuk memformat uang dan waktu. Kelas ini memiliki metode `format_uang` dan `format_waktu` untuk pemformatan.

### Program Mobil (`program_mobil.py`)

Modul ini menyediakan kelas `Mobil` untuk manajemen daftar mobil. Kelas ini memiliki metode `tambah_mobil` dan `tampilkan_daftar_mobil`.

### Program Pemesanan (`program_pemesanan.py`)

Modul ini menyediakan kelas `Pemesanan` untuk membuat pemesanan, menghitung pembayaran, dan menulis ke file. Kelas ini memiliki metode `buat_pemesanan`, `pembayaran`, dan `tulis_ke_file`.

## Kontribusi

Jika Anda ingin berkontribusi pada pengembangan program ini, silakan buat _pull request_ atau laporkan masalah (_issue_).

## Lisensi

Dilisensikan di bawah [MIT License](LICENSE).
```


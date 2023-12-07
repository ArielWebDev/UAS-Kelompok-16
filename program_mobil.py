# program_mobil.py

from program_format import Format  # Bergantung pada class Format dari file program_format.py

class Mobil:
    def __init__(self):
        # Konstruktor untuk inisialisasi daftar mobil dan objek Format di dalam Mobil
        self.daftar_mobil = []
        self.format = Format()

    def tambah_mobil(self):
        # Metode untuk menambahkan mobil ke daftar berdasarkan input pengguna
        nama = input("Masukkan nama mobil: ")
        harga = float(input("Masukkan harga mobil: "))
        mobil = {'nama': nama, 'harga': harga}
        self.daftar_mobil.append(mobil)
        print(f"{nama} berhasil ditambahkan.\n")

    def tampilkan_daftar_mobil(self):
        # Metode untuk menampilkan daftar mobil beserta harga yang sudah diformat menggunakan objek Format
        print("Daftar Mobil")
        if not self.daftar_mobil:
            print("Belum ada mobil.")
        else:
            for nomor, mobil in enumerate(self.daftar_mobil, start=1):
                harga_rupiah = self.format.format_uang(mobil['harga'])
                print(f"{nomor}. {mobil['nama']} - Harga: {harga_rupiah}")
        print()

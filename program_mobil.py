# program_mobil.py

from program_format import Format  # Mengimpor class Format dari file program_format.py

class Mobil:
    def __init__(self):
        # Konstruktor untuk inisialisasi daftar mobil dan objek Format di dalam Mobil
        self.daftar_mobil = []  # Daftar mobil sebagai atribut instance
        self.format = Format()  # Objek Format sebagai atribut instance

        # Menambahkan beberapa mobil ke daftar saat program dimulai
        mobil1 = {'nama': 'Avanza', 'harga': 200000}
        mobil2 = {'nama': 'Innova', 'harga': 300000}
        mobil3 = {'nama': 'Xenia', 'harga': 180000}

        self.daftar_mobil.extend([mobil1, mobil2, mobil3])

    def tambah_mobil(self):
        # Metode untuk menambahkan mobil ke daftar berdasarkan input pengguna
        nama = input("Masukkan nama mobil: ")
        harga = float(input("Masukkan harga mobil: "))
        mobil = {'nama': nama, 'harga': harga}
        self.daftar_mobil.append(mobil)  # Menambahkan mobil ke daftar
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

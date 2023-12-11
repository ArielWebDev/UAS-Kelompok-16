# main.py

from program_mobil import Mobil  # Import kelas Mobil dari program_mobil.py
from program_pemesanan import Pemesanan  # Import kelas Pemesanan dari program_pemesanan.py

# Program utama
mobil = Mobil()  # Inisiasi objek Mobil

# Membuat objek Pemesanan
pemesanan = Pemesanan()

while True:
    print("Selamat datang di Rental Kendaraan")
    print("1. Tambah Mobil")
    print("2. Daftar Mobil")
    print("3. Buat Pemesanan")
    print("4. Keluar")

    # Meminta input pengguna untuk memilih menu
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        mobil.tambah_mobil()  # Memanggil metode tambah_mobil dari objek mobil

    elif pilihan == '2':
        mobil.tampilkan_daftar_mobil()  # Memanggil metode tampilkan_daftar_mobil dari objek mobil

    elif pilihan == '3':
        pemesanan.buat_pemesanan(mobil)  # Memanggil metode buat_pemesanan dari objek pemesanan dengan melewatkan objek mobil sebagai argumen

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih lagi.\n")

# main.py

from program_mobil import Mobil
from program_pemesanan import Pemesanan

# Program utama
mobil = Mobil()
pemesanan = Pemesanan()

while True:
    print("Selamat datang di Rental Kendaraan")
    print("1. Tambah Mobil")
    print("2. Daftar Mobil")
    print("3. Buat Pemesanan")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        mobil.tambah_mobil()

    elif pilihan == '2':
        mobil.tampilkan_daftar_mobil()

    elif pilihan == '3':
        pemesanan.buat_pemesanan(mobil)

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih lagi.\n")

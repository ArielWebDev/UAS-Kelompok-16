# program_pemesanan.py

from datetime import datetime
from program_format import Format  # Bergantung pada class Format dari file program_format.py

class Pemesanan:
    def __init__(self):
        # Konstruktor untuk inisialisasi objek Format di dalam Pemesanan
        self.format = Format()

    def buat_pemesanan(self, mobil):
        # Metode untuk membuat pemesanan berdasarkan input pengguna
        print("BIODATA PENYEWA")

        nama = str(input("Masukkan Nama: "))
        nomor_telpon = int(input("Masukkan Nomor Telepon: "))

        # Menampilkan daftar mobil
        mobil.tampilkan_daftar_mobil()

        kendaraan_input = int(input("Pilih Nomor Mobil yang akan disewa: "))
        if 1 <= kendaraan_input <= len(mobil.daftar_mobil):
            kendaraan = mobil.daftar_mobil[kendaraan_input - 1]
            nama_kendaraan = kendaraan['nama']
            harga_kendaraan = kendaraan['harga']

            print(f"Harga Sewa {nama_kendaraan}: {self.format.format_uang(harga_kendaraan)} per hari")
            tanggal_awal = datetime.strptime(input("Masukkan tanggal awal (DD/MM/YYYY): "), "%d/%m/%Y")
            tanggal_selesai = datetime.strptime(input("Masukkan tanggal selesai (DD/MM/YYYY): "), "%d/%m/%Y")

            if tanggal_awal and tanggal_selesai:
                if tanggal_awal <= tanggal_selesai:
                    jumlah_hari = (tanggal_selesai - tanggal_awal).days + 1
                    total_harga = harga_kendaraan * jumlah_hari

                    # Tampilkan informasi pembayaran dan struk
                    self.pembayaran(nama, nomor_telpon, total_harga, jumlah_hari, nama_kendaraan)
                else:
                    print("Tanggal selesai harus lebih besar atau sama dengan tanggal awal.")
            else:
                print("Tanggal awal dan tanggal selesai harus terisi.")
        else:
            print("Pilihan mobil tidak valid. Silakan pilih kembali.")

    def pembayaran(self, nama, nomor_telpon, total_harga, jumlah_hari, nama_kendaraan):
        # Metode untuk melakukan pembayaran berdasarkan input pengguna
        print("===============================")
        print(f"Nama Penyewa: {nama}")
        print(f"Nomor Telpon Penyewa: {nomor_telpon}")
        print(f"Mobil yang disewa: {nama_kendaraan}")
        print(f"Total Harga Sewa Mobil: {self.format.format_uang(total_harga)}")
        print(f"Jumlah Hari: {jumlah_hari}")
        print("===============================")

        while True:
            pembayaran = float(input("Masukkan jumlah pembayaran: "))
            if pembayaran >= total_harga:
                kembalian = pembayaran - total_harga
                print(f"Terima kasih! Kembalian Anda: {self.format.format_uang(kembalian)}")

                # Tulis ke file setelah pembayaran
                self.tulis_ke_file(nama, nomor_telpon, total_harga, jumlah_hari, nama_kendaraan, pembayaran, kembalian)
                break
            else:
                print("Jumlah pembayaran tidak mencukupi. Silakan masukkan jumlah yang cukup.")

    def tulis_ke_file(self, nama, nomor_telpon, total_harga, jumlah_hari, nama_kendaraan, pembayaran, kembalian):
        # Metode untuk menulis data pemesanan ke file
        timestamp = self.format.format_waktu(datetime.now())
        nama_file = f"{nama}.txt"  # Gunakan informasi nama penyewa dan timestamp dalam nama file
        with open(nama_file, "w") as file:
            file.write("===============================\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Nama Penyewa: {nama}\n")
            file.write(f"Nomor Telpon Penyewa: {nomor_telpon}\n")
            file.write(f"Mobil yang disewa: {nama_kendaraan}\n")
            file.write(f"Total Harga Sewa Mobil: {self.format.format_uang(total_harga)}\n")
            file.write(f"Jumlah Hari: {jumlah_hari}\n")
            file.write(f"Jumlah Pembayaran: {self.format.format_uang(pembayaran)}\n")
            file.write(f"Kembalian: {self.format.format_uang(kembalian)}\n")
            file.write("===============================\n")
            print(f"Data berhasil ditulis ke file '{nama_file}'")

# program_format.py

import locale
from datetime import datetime

class Format:
    def __init__(self, locale_id='id_ID'):
        # Konstruktor untuk inisialisasi objek Format dengan pengaturan locale bahasa Indonesia
        self.locale_id = locale_id
        locale.setlocale(locale.LC_ALL, self.locale_id)

    def format_uang(self, jumlah):
        # Metode untuk memformat jumlah uang dengan menggunakan locale untuk pemisah ribuan
        return locale.currency(jumlah, grouping=True)

    def format_waktu(self, waktu, format='%Y-%m-%d %H:%M:%S'):
        # Metode untuk memformat objek datetime sesuai dengan format yang diinginkan
        return waktu.strftime(format)

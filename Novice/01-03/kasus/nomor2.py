import datetime
import time

sekarang = datetime.datetime.now()
tanggal = sekarang.date()
waktu = sekarang.time()

print ('Hari = ',tanggal.day)
print ('Bulan = ',tanggal.month)
print ('Tahun = ',tanggal.year)
print ('jam = ',waktu.hour)
print ('Menit = ',waktu.minute)
print ('Detik = ',waktu.second)
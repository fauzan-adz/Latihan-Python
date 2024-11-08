#I.S.: pengguna memasukkan data yaitu jenis kendaraan, NoPol, jam masuk, menit masuk, jam keluar, menit keluar
#F.S.: menampilkan biaya parkir yang harus dibayar

#badan program

import os

print("<====BIAYA PARKIR====>")
Kendaraan = input("Jenis Kendaraan: ")
NoPol = input("Nomor Polisi: ")

#input waktu masuk

JamMasuk = input("Jam Masuk  : ")
MenitMasuk = input("Menit Masuk :")
JamMasuk = int(JamMasuk)
MenitMasuk = int(MenitMasuk)

#input waktu keluar

JamKeluar = input("Jam Keluar  : ")
MenitKeluar = input("Menit Keluar :")
JamKeluar = int(JamKeluar)
MenitKeluar = int(MenitKeluar)

#menentukan lama parkir

if MenitKeluar < MenitMasuk:
    MenitKeluar = MenitKeluar + 60
    JamKeluar = JamKeluar - 1
Menit = MenitKeluar - MenitMasuk

if JamKeluar < JamMasuk:
    JamKeluar = JamKeluar + 12
Jam = JamKeluar - JamMasuk

print("Lama Parkir  : ",Jam," Jam",Menit," Menit" )

if (Menit > 0):
    Jam = Jam + 1
print('              :', Jam, ' Jam')

#menghitung biaya parkir

Kendaraan = Kendaraan.upper()
if Kendaraan == "MOTOR":
    Biaya = 1500 + (Jam - 1) * 500
else:
    Biaya = 3000 + (Jam - 1) * 1000

#menampilkan tiket parkir

os.system('pause')
os.system('cls')

print("<<<< TIKET PARKIR >>>>")
print(f'Jenis Kendaraan  : {Kendaraan}')
print(f'Nomor Polisi     : {NoPol}')
print(f'Jam Masuk        : {JamMasuk}')
print(f'Jam Keluar       : {JamKeluar}')
print(f'Lama Parkir      : {Jam} Jam')
print(f'Biaya Parkir     :Rp. {Biaya}')



    

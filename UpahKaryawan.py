#Upah Karyawan Selama Seminggu

#I.S.: pengguna memasukkan data karyawan yaitu Nama Karyawan, NIK, Jam kerja selama seminggu
#F.S.: menampilkan total gaji yang didapatkan karyawan selama seminggu

#badan program

import os

print("")
print("------------ MASUKKAN DATA KARYAWAN ------------")
Nama     = str(input("Nama Karyawan                        : "))
NIK      = str(input("NIK                                  : "))
JamKerja = int(input("Jam Kerja Karyawan (Selama Seminggu) : "))
Upah     = int(input("Upah Perjam                          : "))
print("")

#menghitung upah karyawan

JamLembur = 0

if JamKerja > 40:
    JamLembur = JamKerja - 40
    JamKerja = JamKerja - JamLembur

GajiPokok = JamKerja * Upah
GajiLembur = JamLembur * (Upah * 2)
TotalGaji = GajiPokok + GajiLembur

#Menampilkan upah yang diberikan kepada seorang karyawan selama seminggu

os.system("pause")
os.system("cls")


print("")
print("------------ GAJI POKOK ------------")
print(f'Nama Karyawan       : {Nama}')
print(f'NIK                 : {NIK}')
print(f'Jam Kerja           : {JamKerja}')
print(f'Jam Lembur          : {JamLembur}')
print(f'Gaji Pokok          : {GajiPokok:>14,.2f}')
print(f'Gaji Lembur         : {GajiLembur:>14,.2f}')
print(f'Total Gaji          : {TotalGaji:>14 ,.2f}')
print("")
#i.s. pengguna memasukkan bulan, bulan2, bulan3, tahun1, tahun2, tahun3, nk1, nik2, nik3, nama1, nama2, nama3, gajipokok1, gajipokok2, gajipokok3.
#f.s. manmpilkan gajibersih1, gajibersih2, gajibersih3

import os 
#badan program
print(" DATA PENGGAJIAN KARYAWAN")
#memasukkan bulan dan tahun
bulan = str(input("Memasukkan bulan :"))
tahun = str(input("Memasukkan tahun :"))
print("=======================================================================")
print(f"TANGGAL     ;{bulan,tahun}")
print("=======================================================================")
#memasukkan penggajian karyawan ke-1
nik = str(input("Masukkan nik :"))
nama = str(input("Masukkan nama :"))
gajipokok = float(input("Masukkan gaji pokok :"))
pajak = gajipokok * 10 / 100
tunjangan = gajipokok * 20 / 100
gajibersih = (gajipokok + tunjangan) - pajak
print (f"Pajak yang harus dibayarkan        : Rp. {pajak:<12,.1f}")
print (f"Tunjangan yang didapatkan          : Rp. {tunjangan:<12,.1f}")
print (f"Gaji bersih karyawan               : Rp. {gajibersih:<12,.1f}")

print("=======================================================================")
#memasukkan bulan dan tahun
bulan2 = str(input("Memasukkan bulan :"))
tahun2= str(input("Memasukkan tahun :"))
print("=======================================================================")
print(f"TANGGAL     ;{bulan2,tahun2}")
print("=======================================================================")
#memasukkan penggajian karyawan ke-2
nik2 = str(input("Masukkan nik :"))
nama2 = str(input("Masukkan nama :"))
gajipokok2 = float(input("Masukkan gaji pokok :"))
pajak2 = gajipokok2 * 10 / 100
tunjangan2 = gajipokok2 * 20 / 100
gajibersih2 = (gajipokok2 + tunjangan2) - pajak2
print (f"Pajak yang harus dibayarkan        : Rp. {pajak2:<12,.1f}")
print (f"Tunjangan yang didapatkan          : Rp. {tunjangan2:<12,.1f}")
print (f"Gaji bersih karyawan               : Rp. {gajibersih2:<12,.1f}")

print("=======================================================================")
#memasukkan bulan dan tahun
bulan3 = str(input("Memasukkan bulan :"))
tahun3 = str(input("Memasukkan tahun :"))
print("=======================================================================")
print(f"TANGGAL     ;{bulan3,tahun3}")
print("=======================================================================")
#memasukkan penggajian karyawan ke-2
nik3 = str(input("Masukkan nik :"))
nama3 = str(input("Masukkan nama :"))
gajipokok3 = float(input("Masukkan gaji pokok :"))
pajak3 = gajipokok3 * 10 / 100
tunjangan3 = gajipokok3 * 20 / 100
gajibersih3 = (gajipokok3 + tunjangan3) - pajak3
print (f"Pajak yang harus dibayarkan        : Rp. {pajak3:<12,.1f}")
print (f"Tunjangan yang didapatkan : Rp. {tunjangan3:<12,.1f}")
print (f"Gaji bersih karyawan : Rp. {gajibersih3:<12,.1f}")


os.system('pause')
os.system('cls')
print("                                     LAPORAN PENGGAJIAN                                                 ")
print(f"BUlam/Tahun : {bulan:>8}/{tahun:4}")
print("====================================================================================================================")
print("|    NIK    |    NAMA KARYAWAN   |     GAJI POKOK     |       PAJAK        |     TUNJANGAN     |     GAJI BERSIH   |")
print("====================================================================================================================")
print(f"| {nik:9} | {nama:18} | Rp. {gajipokok:10}     | Rp. {pajak:>11.1f}    | Rp. {tunjangan:12.1f}  | Rp. {gajibersih:>12.1f} |")
print("====================================================================================================================")
print(f"| {nik2:9} | {nama2:18} | Rp. {gajipokok2:10}     | Rp. {pajak2:>11.1f}    | Rp. {tunjangan2:12.1f}  | Rp. {gajibersih2:>12.1f} |")
print("====================================================================================================================")
print(f"| {nik3:9} | {nama3:18} | Rp. {gajipokok3:10}     | Rp. {pajak3:>11.1f}    | Rp. {tunjangan3:12.1f}  | Rp. {gajibersih3:>12.1f} |")
print("====================================================================================================================")
#total biaya yang harus dibayarkan perusahaan
totalbiayaperusahaan = gajibersih + gajibersih2 + gajibersih3
#meanmpilkan total biaya perusahaan
print (f"Total biaya yang harus dibayarkan perusahaan : Rp. {totalbiayaperusahaan}") 





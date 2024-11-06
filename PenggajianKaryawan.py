#DATA_PENGGAJIAN_KARYAWAN
#I.S.: pengguna memasukkan data karyawan yang terdiri dari 3 data yaitu NIK, Nama,
#      dan Gaji pokok
#F.S.: menampilkan gaji bersih, PPN, Tunjangan, dan Total gaji yang harus dibayar
#      oleh perusahaan

import os
#badan program

print('DATA PENGGAJIAN KARYAWAN')

#pengguna memasukkan periode pendataan dan data karyawan

print('MASUKKAN PERIODE PENDATAAN')
print('===============<<>>================')
bulan = str(input('Masukkan bulan : '))
tahun = str(input('Masukkan tahun : '))
print('===============<<>>================')

os.system('pause')
os.system('cls')
print('PERIODE :', {bulan,tahun})

#pengguna memasukkan data karyawan kesatu
print('===============<<>>================')
Nama1 = str(input('Nama Karyawan   : '))
NIK1 = str(input('NIK Karyawan    : '))
GajiPokok1 = int(input('Gaji Pokok    : '))
PPN1 = GajiPokok1 * 0.1
Tunjangan1 = GajiPokok1 * 0.2
GajiBersih1 = GajiPokok1 - PPN1 + Tunjangan1
print('=============== <>>================')
print (f'PPN         : Rp. {PPN1:<12,.1f}' )
print (f'Tunjangan   : Rp. {Tunjangan1:<12,.1f}')
print (f'Gaji bersih : Rp. {GajiBersih1:<12,.1f}')
print('===============<<>>================')

#pengguna memasukkan data karyawan kedua
Nama2 = str(input('Nama Karyawan   : '))
NIK2 = str(input('NIK Karyawan    : '))
GajiPokok2 = int(input('Gaji Pokok    : '))
PPN2 = GajiPokok2 * 0.1
Tunjangan2 = GajiPokok2 * 0.2
GajiBersih2 = GajiPokok2 - PPN2 + Tunjangan2
print('=============== <>>================')
print (f'PPN         : Rp. {PPN2:<12,.1f}' )
print (f'Tunjangan   : Rp. {Tunjangan2:<12,.1f}')
print (f'Gaji bersih : Rp. {GajiBersih2:<12,.1f}')
print('===============<<>>================')

#pengguna memasukkan data karyawan ketiga
Nama3 = str(input('Nama Karyawan   : '))
NIK3 = str(input('NIK Karyawan    : '))
GajiPokok3 = int(input('Gaji Pokok    : '))
PPN3 = GajiPokok3 * 0.1
Tunjangan3 = GajiPokok3 * 0.2
GajiBersih3 = GajiPokok3 - PPN3 + Tunjangan3
print('===============<<>>================')
print (f'PPN         : Rp. {PPN3:<12,.1f}' )
print (f'Tunjangan   : Rp. {Tunjangan3:<12,.1f}')
print (f'Gaji bersih : Rp. {GajiBersih3:<12,.1f}')
print('===============<<>>================')

#menampilkan total gaji yang harus dibayar perusahaan

os.system('pause')
os.system('cls')
print('-------------------------------------------<LAPORAN PENGGAJIAN>-----------------------------------------')
print('--------------------------------------------------------------------------------------------------------')
print('|   NIK   |    NAMA    |     GAJI POKOK     |      PAJAK      |      TUNJANGAN     |     GAJI BERSIH    |')
print('----------------------------------------------------------------------------------------------------')
print(f'| {NIK1:7} | {Nama1:10} | Rp. {GajiPokok1:14} | Rp. {PPN1:11} | Rp. {Tunjangan1:14} | Rp. {GajiBersih1:14} |')
print('----------------------------------------------------------------------------------------------------')
print(f'| {NIK2:7} | {Nama2:10} | Rp. {GajiPokok2:14}. | Rp. {PPN2:11} | Rp. {Tunjangan2:14} | Rp. {GajiBersih2:14} |')
print('----------------------------------------------------------------------------------------------------')
print(f'| {NIK3:7} | {Nama3:10} | Rp. {GajiPokok3:14} | Rp. {PPN3:11} | Rp. {Tunjangan3:14} | Rp. {GajiBersih3:14} |')
print('--------------------------------------------------------------------------------------------------------')
TotalGaji = GajiBersih1 + GajiBersih2 + GajiBersih3
print(f'TOTAL GAJI YANG HARUS DIBAYAR PERUSAHAAN : {TotalGaji:<12,.1f}')
print('===============<<>>================')
print('--------------------------------------------------------------------------------------------------------')
#Struk Pembayaran agen PD Cepat Laku
#I.S.:{ }
#F.S.:{ }

#Badan Program

import os

#MEMASUKKAN KODE BARANG DAN JUMLAH BARANG

KodeBarang = str(input("Masukkan kode Barang    : ")).upper()

if (KodeBarang != 'PK01') and (KodeBarang != 'TS02') and (KodeBarang != 'SP03') and (KodeBarang != 'AK04'):
    print('KODE PRODUK YANG ANDA MASUKKAN TIDAK TERDAFTAR')
else:
    print(f'PRODUK {KodeBarang} TERSEDIA')

if (KodeBarang == 'PK01'):
    NamaBarang = 'Pakaian'
    HargaBarang = 75000
else:
    if (KodeBarang == 'TS02'):
        NamaBarang = 'Tas'
        HargaBarang =  65500
    else:
        if (KodeBarang == 'SP03'):
            NamaBarang = 'Sepatu'
            HargaBarang = 157000
        else:
            if (KodeBarang == 'AK04'):
                NamaBarang = 'Aksesoris'
                HargaBarang = 45000

JumlahBarang = int(input("Masukkan Jumlah Barang: "))

Diskon = 0 
StatusDiskon = 'T'
if (JumlahBarang >= 10):
    StatusDiskon = input('ADA DISKON [Y/T]: ')
if (StatusDiskon == 'Y'):
    Diskon = int(input("Besar Diskon : "))

HargaTotal = HargaBarang * JumlahBarang
BesaranDiskon = Diskon / 100
HargaDiskon = HargaTotal * BesaranDiskon
TotalBayar = HargaTotal - HargaDiskon


print(f'Total Harga :Rp. {HargaTotal}')
print(f'Diskon      :Rp. {HargaDiskon}')
print(f'Total Bayar :Rp. {TotalBayar}')
Bayar = int(input('Bayar :Rp. '))

Kembalian = Bayar - TotalBayar

#Layar Keluaran
os.system('pause')
os.system('cls')

print(f'Kode Barang         : {KodeBarang}')
print(f'Nama Barang         : {NamaBarang}')
print(f'Jumlah Beli         : {JumlahBarang}')
print(f'Harga Satuan        :Rp. {HargaBarang}')
print(f'Harga Total         :Rp. {HargaTotal}')
print(f'Diskon {Diskon}%          :Rp. {HargaDiskon}')
print('-----------------------------------------')
print(f'Total Bayar         :Rp. {TotalBayar}')
print(f'Bayar               :Rp. {Bayar}')
print(f'Kembalian           :Rp. {Kembalian}')
#Menghitung Volume Balok dari satuan inch ke cm

#I.S.: Pengguna memasukkan nilai panjang,lebar,tinggi
#F.S.: Menampilkan hasil perhitungan dari volume balok

#Badan program

print("MASUKKAN DATA")
print("--------<>--------")

Panjang = float(input('Panjang ='))
Lebar = float(input('Lebar ='))
Tinggi = float(input('Tinggi ='))
konst = 2.54

#Proses menghitung luas balok

VolumeBalok = (Panjang*konst)*(Tinggi*konst)*(Lebar*konst)

#Menampilkan nilai volume balok
print("--------<>--------")
print("HASIL :")

print(f'Volume Balok =  {VolumeBalok:.2f}')

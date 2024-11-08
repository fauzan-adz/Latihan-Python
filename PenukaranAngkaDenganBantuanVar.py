#Penukaran dua buah angka dengan bantuan variable
#I.S.: pengguna memasukkan angka kesatu dan kedua
#F.S.: menampilkan hasil penukaran angka kesatu dan kedua

#badanprogram

print("SEBELUM DITUKAR")

A = int(input('Angka Ke-1  :'))
B = int(input('Angka Ke-2  :'))

#proses penukaran

temp = A
A = B
B = temp

#menampilkan hasil

print("SESUDAH DITUKAR")

print("Angka Ke-1 :",A)
print("Angka Ke-2 :",B)

print("ANJAYYYYY")
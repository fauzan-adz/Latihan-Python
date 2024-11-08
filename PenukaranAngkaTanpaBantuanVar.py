#Menukarkan dua buah angka tanpa bantuan variabel
#I.S.: pengguna memasukkan dua buah angka
#F.S.: menampilkan pertukaran angka kesatu dan kedua

#badan program

print("SEBELUM PENUKARAN")

A = int(input('Masukkan Angka ke-1 : '))
B = int(input('Masukkan Angka ke-2 : '))

#proses penukaran nilai

A = A+B
B = A-B
A = A-B

#menampilkan hasil 
print ("<---------<>-------->")
print("SESUDAH PENUKARAN")

print("A = ", A)
print("B = ", B)
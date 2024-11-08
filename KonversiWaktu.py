#Mengkonversi Waktu

#I.S.: Pengguna memasukkan nilai waktu yaitu detik
#F.S.: Menampilkan hasil konversi ke hari, jam , menit, dan detik

#Badan program

NilaiDetik = int(input("Masukkan nilai detik "))

Hari = NilaiDetik // (24 * 3600)
NilaiDetik = NilaiDetik % (24 * 3600)
Jam = NilaiDetik // 3600
NilaiDetik = NilaiDetik % 3600
Menit = NilaiDetik // 60
Detik = NilaiDetik % 60

print("Jumlah :", Hari, " Hari")
print("Jumlah :", Jam, " Jam")
print("Jumlah :", Menit, " Menit")
print("Jumlah :", Detik, " Detik")
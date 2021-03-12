import math

#Menampilkan informasi program
print("Luas dan keliling lingkaran")

#Input nilai jari-jari
r = float(input("Masukkan nilai jari-jari:  "))

#Menghitung luas lingkaran
luas_lingkaran = 3.14 * math.pow(r,2)

#Menghitung keliling lingkaran
keliling_lingkaran = 2 * 3.14 * r

#Menghasilkan hasil perhitungan kelayar
print("Luas lingkaran:  ", luas_lingkaran)
print("Keliling lingkaran:  ", keliling_lingkaran)
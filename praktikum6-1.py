# Program 1
print("Program 1: Memfilter bilangan genap dan ganjil dari suatu list")
list_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]

genap = [x for x in list_angka if x % 2 == 0]
ganjil = [x for x in list_angka if x % 2 != 0]

jumlah_genap = len(genap)
jumlah_ganjil = len(ganjil)

# Menampilkan hasil
print("Jumlah bilangan genap  : ", jumlah_genap)
print("Jumlah bilangan ganjil : ", jumlah_ganjil)
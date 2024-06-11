#program 1 : perhitungan sederhana
BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100
RumusPenjumlahan = BilanganPertama+BilanganKedua+BilanganKetiga
RumusPengurangan = BilanganPertama-BilanganKedua-BilanganKetiga
RumusPerkalian = BilanganPertama*BilanganKedua*BilanganKetiga
print("Penjumlahan =",BilanganPertama ,"+",BilanganKedua ,"+",BilanganKetiga ,"=",RumusPenjumlahan)
print("Pengurangan =",BilanganPertama ,"-",BilanganKedua ,"-",BilanganKetiga ,"=",RumusPengurangan)
print("Perkalian =",BilanganPertama ,"x",BilanganKedua ,"x",BilanganKetiga ,"=",RumusPerkalian)

print("\n")

#program 2 : menghitung luas bangun datar
#1. Luas persegi
panjang_sisi = 20
luas_persegi = panjang_sisi*panjang_sisi
print("Luas persegi dengan panjang sisi",panjang_sisi ,"cm adalah",luas_persegi)

#2. Luas persegi panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp*lebar_pp
print("Luas persegi panjang dengan panjang ",panjang_pp ,"cm dan lebar",lebar_pp ,"cm adalah", luas_pp)

#3. Luas segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5*alas_segitiga*tinggi_segitiga
print("Luas segitiga dengan panjang alas",alas_segitiga ,"cm dan tinggi segitiga",tinggi_segitiga ,"cm adalah", luas_segitiga)

#4. Luas lingkaran
phi = 3.14
jari_jari = 15
luas_lingkaran = phi*jari_jari*jari_jari
print("Luas lingkaran dengan jari-jari", jari_jari,"cm x phi :",phi,"adalah",luas_lingkaran)

#5. Luas jajar genjang
alas_jg = 4
tinggi_jg = 10
luas_jg = alas_jg*tinggi_jg
print("Luas jajar genjang dengaas",alas_jg,"cm dan tinggi",tinggi_jg,"cm adalah",luas_jg)

#6. Luas trapesium
alas_a = 6
alas_b = 9
tinggi_trpsm = 12
luas_trapesium=0.5*(alas_a+alas_b)*tinggi_trpsm
print("Luas trapesium yang memiliki tinggi",tinggi_trpsm,"cm, alas a",alas_a,"cm dan alas b",alas_b,"cm adalah",luas_trapesium)

print("\n")

#program 3 : operator bitwise
a = 9
b = 4

hasil_and = a & b
print("a & b =", hasil_and)

hasil_or = a | b
print("a | b =", hasil_or)

hasil_not = ~a
print("~a =", hasil_not)

hasil_xor = a ^ b
print("a ^ b =", hasil_xor)
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))
bilangan3 = float(input("Masukkan bilangan ketiga: "))

if bilangan1 <= bilangan2 <= bilangan3 or bilangan3 <= bilangan2 <= bilangan1:
    nilai_median = bilangan2
elif bilangan2 <= bilangan1 <= bilangan3 or bilangan3 <= bilangan1 <= bilangan2:
    nilai_median = bilangan1
else:
    nilai_median = bilangan3

print("Nilai median adalah:", nilai_median)

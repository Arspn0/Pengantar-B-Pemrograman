# Inisialisasi variabel PIN dan saldo awal
pin = "1234"
saldo = 1000

# Main program
kondisi = True
print("Selamat datang di ATM")
while kondisi:
    input_pin = input("Masukkan PIN Anda: ")
    if input_pin == pin:
        kondisi = True
    else:
        print("PIN salah.")
        kondisi =  False

    while kondisi:
        print("\nMenu ATM:")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Simpan Uang")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            print("Saldo Anda: Rp", saldo)
        elif pilihan == "2":
            jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: Rp "))
            if jumlah_tarik <= saldo:
                saldo -= jumlah_tarik
                kondisi = True
                print("Penarikan berhasil. Saldo Anda sekarang Rp", saldo)
            else:
                kondisi = False
                print("Saldo tidak mencukupi.")
        elif pilihan == "3":
            jumlah_simpan = int(input("Masukkan jumlah yang ingin disimpan: Rp "))
            saldo += jumlah_simpan
            kondisi = True
            print("Uang berhasil disimpan. Saldo Anda sekarang Rp", saldo)
        elif pilihan == "4":
            kondisi = False
            print("Terima kasih telah menggunakan layanan ATM.")
            break
        else:
            print("Pilihan tidak valid.")

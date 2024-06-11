# Program a: String Arrays
a = "Hello World"

print(f"Full string: {a}")
print(f"Menampilkan character pada index ke-2 adalah huruf: {a[2]}")
print(f"Menampilkan character pada index ke-4 adalah huruf: {a[4]}")
print(f"Menampilkan character pada index ke-8 adalah huruf: {a[8]}")
print(f"Menampilkan character pada index ke-10 adalah huruf: {a[10]}")



# Program b: String Range (Slicing)
a = "Hello World"

print(f"Full string: {a}")
print(f"Menampilkan character pada index ke 1 sampai 3 adalah huruf: {a[1:4]}")
print(f"Menampilkan character pada index ke 2 sampai 5 adalah huruf: {a[2:6]}")
print(f"Menampilkan character pada index ke 3 sampai 10 adalah huruf: {a[3:11]}")



# Program c: Fungsi Lowercase, Uppercase, dan Replace
a = "Hello World"

lowercase_a = a.lower()
uppercase_a = a.upper()
replace_a = a.replace("o", "e")

print(f"Original string: {a}")
print(f"Lowercase string: {lowercase_a}")
print(f"Uppercase string: {uppercase_a}")
print(f"Original string yang 'o' diganti dengan 'e': {replace_a}")



# Program d: Implementasi Enkripsi Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

text = input("Masukkan kata yang ingin dienkripsi: ")
shift = int(input("Masukkan berapa langkah: "))

encrypted_text = caesar_cipher(text, shift)

print(f"Setelah dienkripsi: {encrypted_text}")
# Input angka dari pengguna
angka = int(input("Masukkan angka bulat: "))

# Mengubah angka menjadi string, membalik urutan, lalu mengubahnya kembali menjadi integer
angka_terbalik = int(str(angka)[::-1])

# Menampilkan hasil
print("Angka setelah dibalik:", angka_terbalik)

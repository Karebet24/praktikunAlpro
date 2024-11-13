# Input ukuran dari pengguna
size = int(input("Masukkan Size : "))

# Cetak angka "1"
for i in range(size):
    if i == 0:
        print(" " * (size - 1) + "I")
    else:
        print(" " * (size - 1) + "I")
print()

# Cetak angka "8"
for i in range(size):
    if i == 0 or i == size - 1 or i == size // 2:
        print("O" * size)
    else:
        print("O" + " " * (size - 2) + "O")
print()

# Cetak angka "2"
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("Z" * size)
    elif i < size // 2:
        print(" " * (size - 1) + "Z")
    else:
        print("Z")
print()

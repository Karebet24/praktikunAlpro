n = int(input("Masukkan ukuran sisi N: "))
char = input("Masukkan karakter untuk pola checkerboard: ")

for i in range(n):
#loop luar
    print(" " * (n - i - 1), end="")
    for j in range(2 * i + 1):
        if (i + j) % 2 == 0:
            print("x", end="")
        else:
            print(" ", end="")
    print()
        
for i in range(n - 2, -1, -1):
#loop dalam
    print(" " * (n - i - 1), end="")
    for j in range(2 * i + 1):
        if (i + j) % 2 == 0:
            print("o", end="")
        else:
            print(" ", end="")
    print()
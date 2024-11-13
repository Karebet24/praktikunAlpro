# Mengecek apakah satu tahun adalah kabisat
tahun = 1904

habis_dibagi_400 = tahun % 400 == 0
habis_dibagi_100 = tahun % 100 == 0
habis_dibagi_4 = tahun % 4 == 0

if habis_dibagi_400:
    print(f'{tahun} adalah tahun kabisat')
elif habis_dibagi_4 and not habis_dibagi_100:
    print(f'{tahun} adalah tahun kabisat')
else:
    print(f'{tahun} bukan tahun kabisat')

# Mengecek tahun kabisat berdasarkan input pengguna
tahun = int(input("Masukkan tahun untuk dicek: "))
habis_dibagi_400 = tahun % 400 == 0
habis_dibagi_100 = tahun % 100 == 0
habis_dibagi_4 = tahun % 4 == 0

if habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")

# Mengecek dan menampilkan semua tahun kabisat dalam rentang tertentu
tahun_awal = int(input("\nMasukkan tahun awal: "))
tahun_akhir = int(input("Masukkan tahun akhir: "))

tahun_kabisat = []

for tahun in range(tahun_awal, tahun_akhir + 1):
    habis_dibagi_400 = tahun % 400 == 0
    habis_dibagi_100 = tahun % 100 == 0
    habis_dibagi_4 = tahun % 4 == 0

    if habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100):
        tahun_kabisat.append(tahun)

print("\nTahun kabisat dalam rentang tersebut:")
print(tahun_kabisat)

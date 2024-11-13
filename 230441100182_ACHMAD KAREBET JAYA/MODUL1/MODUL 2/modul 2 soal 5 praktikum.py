# Input data pembeli
nama_pembeli = input("Masukkan nama pembeli: ")
total_belanja = float(input("Masukkan total belanja: Rp"))
member = input("Apakah pembeli memiliki kartu member? (ya/tidak): ").strip().lower() == "ya"
usia = int(input("Masukkan usia pembeli: "))

# Cek usia pembeli
if usia < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    # Inisialisasi diskon
    diskon = 0

    # Diskon 15% jika memiliki kartu member
    if member:
        diskon += 15

    # Diskon tambahan 10% jika total belanja lebih dari Rp500.000
    if total_belanja > 500000:
        diskon += 10

    # Hitung total diskon dan harga setelah diskon
    total_diskon = (diskon / 100) * total_belanja
    harga_setelah_diskon = total_belanja - total_diskon

    # Tampilkan hasil
    print("\nRincian Pembelian:")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Total belanja sebelum diskon: Rp{total_belanja}")
    print(f"Diskon yang didapatkan: {diskon}% (Rp{total_diskon})")
    print(f"Total harga setelah diskon: Rp{harga_setelah_diskon}")

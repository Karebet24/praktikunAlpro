# Konstanta untuk denda per hari dan denda tambahan setiap 5 hari
denda_per_hari = 2500
denda_tambahan_per_5_hari = 5500

while True:
    print("\n=== Program Perhitungan Denda Keterlambatan DVD ===")
    lama_penyewaan = int(input("Masukkan lama waktu penyewaan DVD (dalam hari): "))

    # Hitung hari keterlambatan
    if lama_penyewaan > 5:
        hari_terlambat = lama_penyewaan - 5
        total_denda = 0

        # Hitung denda untuk hari keterlambatan pertama sampai hari ke-10
        if hari_terlambat <= 10:
            total_denda = hari_terlambat * denda_per_hari
        else:
            # Tambah denda untuk 10 hari pertama
            total_denda = 10 * denda_per_hari
            # Hitung sisa hari setelah 10 hari
            sisa_hari = hari_terlambat - 10
            # Hitung denda tambahan untuk setiap 5 hari berikutnya
            total_denda += (sisa_hari * denda_per_hari) + ((sisa_hari // 5) * denda_tambahan_per_5_hari)

        print(f"Denda keterlambatan: Rp{total_denda}")
    else:
        print("Tidak ada denda keterlambatan.")

    # Tanya apakah ingin menghitung ulang
    ulang = input("Apakah Anda ingin menghitung kembali? (y/n): ").strip().lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program ini!")
        break

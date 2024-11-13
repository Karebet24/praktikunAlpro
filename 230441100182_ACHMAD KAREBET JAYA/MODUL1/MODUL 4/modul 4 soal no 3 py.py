gaji_harian = 100000

jam_lembur_mingguan = []
total_lembur = 0  # Total lembur selama seminggu
total_gaji_lembur = 0  # Total uang lembur selama seminggu

for hari in range(1, 8):
    jam_lembur = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0  # Lembur tidak dihitung jika lebih dari 8 jam
    elif total_lembur + jam_lembur > 40:
        print("Total jam lembur mencapai atau melebihi 40 jam, lembur dihentikan.")
        jam_lembur = 0  # Lembur tidak dihitung jika total lebih dari 40 jam

    jam_lembur_mingguan.append(jam_lembur)
    total_lembur += jam_lembur  # Tambahkan jam lembur harian ke total

    # Hitung gaji lembur
    if jam_lembur == 0:
        gaji_lembur = 0
    elif 1 <= jam_lembur < 4:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    
    total_gaji_lembur += gaji_lembur

gaji_mingguan_tanpa_lembur = gaji_harian * 7

gaji_mingguan_dengan_lembur = gaji_mingguan_tanpa_lembur + total_gaji_lembur

print("\nLaporan Gaji Mingguan Mas Ironi:")
for hari, lembur in enumerate(jam_lembur_mingguan, start=1):
    print(f"  Hari ke-{hari}: Jam lembur = {lembur} jam")
print(f"Total lembur selama satu minggu: {total_lembur} jam")
print(f"Total gaji lembur selama satu minggu: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{gaji_mingguan_tanpa_lembur}")
print(f"Total gaji mingguan termasuk lembur: Rp{gaji_mingguan_dengan_lembur}")
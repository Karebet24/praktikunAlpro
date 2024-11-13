def tambah_barang(daftar_barang, nama, id_barang, prioritas):
    if prioritas.lower() == "darurat":
        daftar_barang.insert(0, (nama, id_barang, prioritas))
    elif prioritas.lower() == "biasa":
        tengah_index = len(daftar_barang) // 1
        daftar_barang.insert(tengah_index, (nama, id_barang, prioritas))
    elif prioritas.lower() == "non-darurat":
        daftar_barang.append((nama, id_barang, prioritas))
    else:
        print("Tingkat prioritas tidak valid, barang tidak ditambahkan.")
    return daftar_barang

def tampilkan_barang(daftar_barang):
    print("\nDaftar Barang:")
    for idx, (nama, id_barang, prioritas) in enumerate(daftar_barang):
        print(f"{idx+1}. Nama: {nama}, ID: {id_barang}, Prioritas: {prioritas}")

def main():
    daftar_barang = []
    while True:
        print("\n--- Input Data Barang ---")
        nama = input("Masukkan nama barang: ")
        id_barang = input("Masukkan ID barang: ")
        prioritas = input("Masukkan tingkat prioritas (Darurat, Biasa, Non-Darurat): ")

        daftar_barang = tambah_barang(daftar_barang, nama, id_barang, prioritas)
        tampilkan_barang(daftar_barang)

        lanjut = input("\nApakah ingin mengisi data barang lagi? (y/n): ").lower()
        if lanjut != 'y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
    
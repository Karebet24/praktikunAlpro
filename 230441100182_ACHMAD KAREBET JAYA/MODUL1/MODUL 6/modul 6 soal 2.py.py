def tampilkan_menu():
    print("\nSistem Peminjaman Buku")
    print("1. Tambah Data Peminjaman (Create)")
    print("2. Lihat Semua Data Peminjaman (Read)")
    print("3. Perbarui Data Peminjaman (Update)")
    print("4. Hapus Data Peminjaman (Delete)")
    print("5. Keluar")

def tambah_peminjaman(peminjaman_list):
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman (dd-mm-yyyy): ")

    peminjaman_baru = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
    peminjaman_list.append(peminjaman_baru)
    print("Data peminjaman berhasil ditambahkan!")

def lihat_semua_peminjaman(peminjaman_list):
    if peminjaman_list:
        print("\nDaftar Semua Data Peminjaman:")
        for idx, peminjaman in enumerate(peminjaman_list):
            print(f"{idx + 1}. ID: {peminjaman[0]}, Nama: {peminjaman[1]}, Judul Buku: {peminjaman[2]}, Tanggal: {peminjaman[3]}")
    else:
        print("Tidak ada data peminjaman.")

def perbarui_peminjaman(peminjaman_list):
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin diperbarui: ")
    for idx, peminjaman in enumerate(peminjaman_list):
        if peminjaman[0] == id_peminjaman:
            nama_peminjam = input("Masukkan Nama Peminjam Baru: ")
            judul_buku = input("Masukkan Judul Buku Baru: ")
            tanggal_peminjaman = input("Masukkan Tanggal Peminjaman Baru (dd-mm-yyyy): ")
            peminjaman_baru = (id_peminjaman, nama_peminjam, judul_buku, tanggal_peminjaman)
            peminjaman_list[idx] = peminjaman_baru
            print("Data peminjaman berhasil diperbarui!")
            return
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

def hapus_peminjaman(peminjaman_list):
    id_peminjaman = input("Masukkan ID Peminjaman yang ingin dihapus: ")
    for idx, peminjaman in enumerate(peminjaman_list):
        if peminjaman[0] == id_peminjaman:
            del peminjaman_list[idx]
            print("Data peminjaman berhasil dihapus!")
            return
    print("Data peminjaman dengan ID tersebut tidak ditemukan.")

def main():
    peminjaman_list = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_peminjaman(peminjaman_list)
        elif pilihan == "2":
            lihat_semua_peminjaman(peminjaman_list)
        elif pilihan == "3":
            perbarui_peminjaman(peminjaman_list)
        elif pilihan == "4":
            hapus_peminjaman(peminjaman_list)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem peminjaman buku.")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
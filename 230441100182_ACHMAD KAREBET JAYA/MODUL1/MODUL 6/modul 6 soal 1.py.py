def buat_karyawan(nip, nama, alamat, departemen, jabatan):
    return {
        'nip': nip,
        'nama': nama,
        'alamat': alamat,
        'departemen': departemen,
        'jabatan': jabatan
    }

def tambah_karyawan(karyawan_list, karyawan):
    karyawan_list.append(karyawan)

def cari_karyawan(karyawan_list, atribut, nilai):
    hasil_cari = []
    for karyawan in karyawan_list:
        if (
            (atribut == 'nip' and karyawan['nip'] == nilai) or
            (atribut == 'nama' and karyawan['nama'].lower() == nilai.lower()) or
            (atribut == 'alamat' and karyawan['alamat'].lower() == nilai.lower()) or
            (atribut == 'departemen' and karyawan['departemen'].lower() == nilai.lower()) or
            (atribut == 'jabatan' and karyawan['jabatan'].lower() == nilai.lower())
        ):
            hasil_cari.append(karyawan)
    return hasil_cari

def tampilkan_karyawan(karyawan_list):
    if not karyawan_list:
        print("\nTidak ada data karyawan. Silakan tambahkan data terlebih dahulu.")
    else:
        print("\nData Karyawan:")
        for karyawan in karyawan_list:
            print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, "
                  f"Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")

# Main Program
karyawan_list = []

# Menambahkan minimal 5 data karyawan
for i in range(5):
    print(f"\nInput Data Karyawan ke-{i+1}")
    while True:
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")

        if nip and nama and alamat and departemen and jabatan:
            break
        else:
            print("\nData tidak lengkap. Silakan isi semua data kembali.")

    karyawan = buat_karyawan(nip, nama, alamat, departemen, jabatan)
    tambah_karyawan(karyawan_list, karyawan)

# Menampilkan seluruh data karyawan
tampilkan_karyawan(karyawan_list)

# Fitur pencarian
while True:
    if not karyawan_list:
        print("\nTidak ada data karyawan. Silakan isi data baru.")
        while True:
            nip = input("NIP: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            departemen = input("Departemen: ")
            jabatan = input("Jabatan: ")

            if nip and nama and alamat and departemen and jabatan:
                break
            else:
                print("\nData tidak lengkap. Silakan isi semua data kembali.")

        karyawan = buat_karyawan(nip, nama, alamat, departemen, jabatan)
        tambah_karyawan(karyawan_list, karyawan)
        continue  # Mengulangi untuk menampilkan data dan melanjutkan

    print("\nCari Karyawan Berdasarkan Atribut:")
    atribut = input("Masukkan atribut (nip, nama, alamat, departemen, jabatan): ").lower()
    nilai = input(f"Masukkan nilai untuk {atribut}: ")

    hasil = cari_karyawan(karyawan_list, atribut, nilai)

    if hasil:
        print("\nHasil Pencarian:")
        for karyawan in hasil:
            print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, "
                  f"Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")
    else:
        print("\nTidak ada data karyawan yang sesuai.")

    lanjut = input("Apakah ingin mencari lagi? (y/n): ").lower()
    if lanjut != 'y':
        break
# Data mahasiswa
nama_jaka = "Jaka"
nama_ida = "Ida"
skor_jaka = 1120
ipk_jaka = 3.5
skor_ida = 1000
ipk_ida = 3.5

# Persyaratan beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Mengecek apakah Jaka memenuhi syarat beasiswa
if skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_jaka} memenuhi syarat beasiswa.")
else:
    print(f"{nama_jaka} tidak memenuhi syarat beasiswa.")

# Mengecek apakah Ida memenuhi syarat beasiswa
if skor_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print(f"{nama_ida} memenuhi syarat beasiswa.")
else:
    print(f"{nama_ida} tidak memenuhi syarat beasiswa.")

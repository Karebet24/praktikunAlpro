# Input nilai
nilai = int(input("Masukkan nilai: "))

# Proses seleksi kondisi
if 100 >= nilai >= 81:
    grade = "A"
elif 80 >= nilai >= 71:
    grade = "B"
elif 70 >= nilai >= 61:
    grade = "C"
elif 60 >= nilai >= 41:
    grade = "D"
elif 40 >= nilai >= 0:
    grade = "E"
else:
    grade = "Nilai tidak valid"

# Output hasil
print(f"Nilai: {nilai}, Grade: {grade}")
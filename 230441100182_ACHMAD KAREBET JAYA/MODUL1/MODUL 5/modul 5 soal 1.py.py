def calculate_discount(total_belanja, keanggotaan):
    # Determine membership discount rate
    if keanggotaan.lower() == "gold":
        diskon_keanggotaan = 0.15
    elif keanggotaan.lower() == "silver":
        diskon_keanggotaan = 0.10
    elif keanggotaan.lower() == "bronze":
        diskon_keanggotaan = 0.05
    else:
        diskon_keanggotaan = 0.0

    # Determine additional discount if total_belanja exceeds the threshold
    diskon_tambahan = 0.05 if total_belanja > 1000000 else 0.0

    # Calculate total discount rate and discount amount
    total_diskon = diskon_keanggotaan + diskon_tambahan
    jumlah_diskon = total_belanja * total_diskon
    total_bayar = total_belanja - jumlah_diskon
    
    # Return both discount amount and total to be paid
    return jumlah_diskon, total_bayar

# User input
total_belanja = float(input("Masukkan total belanja: "))
keanggotaan = input("Masukkan jenis keanggotaan (Gold, Silver, Bronze, atau None): ")

# Get discount and total payment
jumlah_diskon, total_setelah_diskon = calculate_discount(total_belanja, keanggotaan)

# Display results
print(f"Jumlah diskon: {jumlah_diskon:.2f}")
print(f"Total yang harus dibayar setelah diskon: {total_setelah_diskon:.2f}")
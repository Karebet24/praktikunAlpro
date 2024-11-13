def cek_palindrom(kata):
    # Mengubah kata menjadi huruf kecil agar case insensitive
    kata = kata.lower()
    # Memeriksa apakah kata sama dengan kebalikannya
    return kata == kata[::-1]
print(cek_palindrom("katak"))  # Output: True
print(cek_palindrom("madam"))  # Output: True
print(cek_palindrom("belajar")) # Output: False
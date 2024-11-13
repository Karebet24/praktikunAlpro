def faktorial(n):
    if n == 0 or n == 1:
        return 1, "1"
    else:
        hasil, langkah = faktorial(n - 1)
        return n * hasil, f"{n} x {langkah}"

n = int(input("Masukkan bilangan : "))
hasil, langkah = faktorial(n)
print(f"{n}! = {langkah} = {hasil}")

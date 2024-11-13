decimal = int(input("Masukkan bilangan desimal: "))

binary = ""
temp = decimal

while temp > 0:
    binary = str(temp % 2) + binary
    temp = temp // 2
    

length = len(binary)
for i in range(1, length + 1):
    print(binary[:i])
Pi = 22/7 # in cm
Panjang_balok = 20  # in cm
lebar_balok = 13  # in cm
tinggi_balok = 7  # in cm
diameter_tabung = 14  # in cm
radius_tabung = diameter_tabung / 2
luas_selimut_tabung = 440  #in cm2
tinggi_tabung = luas_selimut_tabung / (2 * Pi * radius_tabung)
volume_balok = Panjang_balok * lebar_balok * tinggi_balok
volume_tabung = Pi * (radius_tabung ** 2) * tinggi_tabung
print(f"Volume balok:{volume_balok:.2f} cm3")
print(f"Volume tabung:{volume_tabung:.2f} cm3")
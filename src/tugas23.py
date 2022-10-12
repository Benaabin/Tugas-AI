list_angka = [13,26,32,48,60,73,142,221]
hasil = list(filter(lambda i: (i % 13 == 0),list_angka))
print("Angka yang habis dibagi 13 adalah :",hasil)
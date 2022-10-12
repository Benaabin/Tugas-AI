import itertools,random
kartu = list(itertools.product(range(1,10),['Sekop','Hati','Keriting','Wajik']))
random.shuffle(kartu)
print("Anda mendapatkan:")
for n in range(4):
   print(kartu[n][0], "buah", kartu[n][1])
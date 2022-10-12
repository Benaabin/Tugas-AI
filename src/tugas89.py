bil = 13254
balik = 0

while bil != 0:
    digit = bil % 10
    balik = balik * 10 + digit
    bil //= 10

print("Hasil: " + str(balik))
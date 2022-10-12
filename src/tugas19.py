angka = int(input("Masukan angka :"))
panjang = len(str(angka))
y = 0
x = angka
while x > 0:
   dijit = x % 10
   y += dijit ** panjang
   x //= 10

if angka == y:
   print(angka,"adalah Armstrong number")
else:
   print(angka,"bukan Armstrong number")
x=int(input("Masukan batas bawah : "))
y=int(input("Masukan batas atas : "))
for n in range(x, y + 1):
   panjang = len(str(n))
   var = 0
   x = n
   while x > 0:
       digit = x % 10
       var += digit ** panjang
       x //= 10
       
   if n == var:
       print(n)
n=int(input("Masukan angka: "))
if n< 0:
   print("Masukan bilangan positif")
else:
   var = 0
   while(n > 0):
       var += n
       n -= 1
   print("Hasil :", var)
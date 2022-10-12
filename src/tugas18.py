deret = int(input("Masukan banyak deret :"))

i, j = 0, 1
n = 0

if deret <= 0:
   print("Masukan bilangan positif")
elif deret == 1:
   print("Deret fibonacci",deret,":")
   print(i)
else:
   print("Deret fibonacci:")
   while n < deret:
       print(i)
       x = i + j
       i = j
       j = x
       n += 1
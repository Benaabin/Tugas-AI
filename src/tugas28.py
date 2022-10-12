def fungsi_faktor(n):
   print("Faktor dari",n,":")
   for x in range(1, n + 1):
       if n % x == 0:
           print(x)

bil=int(input("Masukan bilangan: "))
fungsi_faktor(bil)
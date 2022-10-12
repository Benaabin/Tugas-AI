def fungsi_faktorial(a):
   if a == 1:
       return a
   else:
       return a*fungsi_faktorial(a-1)

bil=int(input("Masukan bilangan: "))
if bil < 0:
   print("Harap masukan bilangan postitif")
elif bil == 0:
   print("Faktorial dari 0 adalah 1")
else:
   print("Faktorial dari", bil, "is", fungsi_faktorial(bil))
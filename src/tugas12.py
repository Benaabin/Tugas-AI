tahun= int(input("Masukan tahun : "))
if (tahun % 400 == 0) and (tahun % 100 == 0):
    print(tahun,"adalah tahun kabisat")

elif (tahun % 4 ==0) and (tahun % 100 != 0):
    print(tahun,"adalah tahun kabisat")

else:
    print(tahun,"bukan tahun kabisat")
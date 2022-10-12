def fungsi_lcm(x, y):
    if x > y:
       nilai = x
    else:
        nilai = y

    while(True):
        if((nilai % x == 0) and (nilai % y == 0)):
           id = nilai
           break
        nilai+= 1

    return id

bil1=int(input("Masukan bilangan pertama: "))
bil2=int(input("Masukan bilangan kedua: "))
print("L.C.M. :", fungsi_lcm(bil1, bil2))

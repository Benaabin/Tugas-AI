def function(x, y):
    if x > y:
        nilai = y
    else:
        nilai = x
    for i in range(1, nilai+1):
        if((x % i == 0) and (y % i == 0)):
            var = i 
    return var


bil1=int(input("Masukan bilangan pertama: "))
bil2=int(input("Masukan bilangan kedua: "))
print("H.C.F. : ", function(bil1, bil2))
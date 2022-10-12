def fungsi(x):
    if x <2:
        return x
    else:
        return x + fungsi(x-1)

bil = int(input("Masukan bilangan: "))
if bil <0:
    print("Masukan bilangan positif")
else:
    print("Hasilnya adalah:",fungsi(bil)) 
angka= int(input("Masukan angka : "))
indikator=False
if angka >= 2:
    for n in range(2, angka):
        if (angka % n) == 0:
            indikator = True
            break
    if indikator:
        print(angka, "bukan bilangan prima")
    else:
        print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")
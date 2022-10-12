def konversi(a):
    if a >= 2:
        konversi(a//2)
    print(a % 2,end="")

bil=int(input("Masukan bilangan: "))
konversi(bil)
print()
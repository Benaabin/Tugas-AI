x=int(input("Masukan batas bawah : "))
y=int(input("Masukan batas atas : "))
print("Bilangan prima diantara",x,"sampai",y,"\n")
for angka in range(x,y+1):
    if angka >= 2:
        for bil in range(2,angka):
            if (angka % bil) == 0:
                break
        else:
            print(angka)


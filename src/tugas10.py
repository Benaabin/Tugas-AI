angka1= int(input("Masukan angka pertama : "))
angka2= int(input("Masukan angka kedua   :"))
hasil=angka1-angka2
indikator = hasil % 2
print("Hasil pengurangan adalah",hasil)
if hasil == 0:
    print("BILANGAN NOL")
elif indikator!=0:
    if hasil>0:
        print("BILANGAN GANJIL POSITIF")
    else:
        print("BILANGAN GANJIL NEGATIF")
elif indikator==0:
    if hasil>0:
        print("BILANGAN GENAP POSITIF")
    else:
        print("BILANGAN GENAP NEGATIF")
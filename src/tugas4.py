sisi1= float(input("Masukan sisi ke-1:"))
sisi2= float(input("Masukan sisi ke-2: "))
sisi3= float(input("Masukan sisi ke-3: "))
n=(sisi1+sisi2+sisi3)/2
luas=(n*(n-sisi1)*(n-sisi2)*(n-sisi3))**0.5
print("Luas segitiga tersebut adalah : %.2f" %luas)
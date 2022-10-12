angka1= int(input("Masukan angka pertama : "))
angka2= int(input("Masukan angka kedua   :"))
angka3= int(input("Masukan angka ketiga   :"))
if(angka1>=angka2) and (angka1>=angka3):
    print(angka1,"adalah angka terbesar")
elif(angka2>=angka1) and (angka2>=angka3):
    print(angka2,"adalah angka terbesar")
else:
    print(angka3,"adalah angka terbesar")
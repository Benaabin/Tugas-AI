import cmath
#Mencari akar kuadrat
print("MENCARI AKAR KUADRAT")
angka1=eval(input("masukan angka yang ingin dicari: "))
print("Akar kuadrat dari",angka1,"adalah {0:0.3f}".format(angka1**0.5))

#mencari akar pangkat
print("\nMENCARI AKAR PANGKAT")
angka2=eval(input("masukan angka: "))
pangkat=eval(input("masukan pangkat: "))
print("Akar pangkat {0} dari {1} adalah {2}".format(angka2,pangkat,angka2**pangkat))

#angka complex
print("\nMENCARI AKAR KUADRAT ANGKA COMPLEX")
angka3= 2+3j-5j
hasil=cmath.sqrt(angka3)
print('Akar dari {0} adalah {1:0.3f}+{2:0.3f}j'.format(angka3 ,hasil.real,hasil.imag))


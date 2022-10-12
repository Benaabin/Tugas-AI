import cmath
i= float(input("Masukan angka ke-1: "))
j= float(input("Masukan angka ke-2: "))
k= float(input("Masukan angka ke-3: "))
dis=(j**2)-(4*i*k)
solusi_1 = (-j-cmath.sqrt(dis))/(2*i)
solusi_2 = (-j+cmath.sqrt(dis))/(2*i)
print("Solusinya adalah :\n",solusi_1,"\n",solusi_2)
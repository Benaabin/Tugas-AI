def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    return a / b


print("Pilih operasi:\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian")

while True:
    pil = input("Masukan pilihan operasi: ")

    if pil in ('1', '2', '3', '4'):
        bil1=float(input("Masukan bilangan pertama: "))
        bil2=float(input("Masukan bilangan kedua: "))

        if pil == '1':
            print(bil1, "+", bil2, "=", penjumlahan(bil1, bil2))

        elif pil == '2':
            print(bil1, "-", bil2, "=", pengurangan(bil1, bil2))

        elif pil == '3':
            print(bil1, "*", bil2, "=", perkalian(bil1, bil2))

        elif pil == '4':
            print(bil1, "/", bil2, "=", perkalian(bil1, bil2))
        
        ulang = input("Apakah ingin melakukan operasi lain lagi? (iya/tidak): ")
        if ulang == "tidak":
            break
    
    else:
        print("Invalid Input")
def function(n):
    if n == 1:
        return 1
    else:
        return (n * function(n-1))

angka= int(input("Masukan angka : "))
print ("Faktorial dari",angka,"adalah",function(angka))
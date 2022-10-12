def permutasi(kata, panjang=0):

    if panjang == len(kata):   	 
        print("".join(kata))

    for j in range(panjang, len(kata)):

        var = [n for n in kata]
   
        var[panjang], var[j] = var[j], var[panjang]
   	 
        permutasi(var, panjang + 1)

print(permutasi('helo'))
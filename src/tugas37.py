matriks = [[23,43],[23 ,53],[12 ,51]]

hasil = [[matriks[a][b] for a in range(len(matriks))] for b in range(len(matriks[0]))]

for r in hasil:
   print(r)
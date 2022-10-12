matA = [[32,2,3],
       [4 ,32,6],
       [7 ,8,32]]
matB = [[23,8,1],
       [6,23,3],
       [4,5,23]]

hasil=   [[0,0,0],
         [0,0,0],
         [0,0,0]]
         
for a in range(len(matA)):
   for b in range(len(matA[0])):
       hasil[a][b] = matA[a][b] + matB[a][b]

for n in hasil:
   print(n)
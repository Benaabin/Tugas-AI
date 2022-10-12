huruf = 'aeioubcpklmn'

str = 'Hallo apa kabar adikadiku sekalian?'

str = str.casefold()

hitung = {}.fromkeys(huruf,0)

for char in str:
   if char in hitung:
       hitung[char] += 1

print(hitung)
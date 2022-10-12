str = "Hello ini saya coba tes ya adik adik"
kata = [kata.lower() for kata in str.split()]

kata.sort()


print("Hasil:")
for word in kata:
   print(word)
str = 'umuMumU'
str = str.casefold()
rev_str=reversed(str)
if list(str) == list(rev_str):
   print("Kata tersebut palindrome.")
else:
   print("Kata tersebut tidak palindrome.")
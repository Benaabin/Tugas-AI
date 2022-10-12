var_a=10
var_b=20
print("Sebelum ditukar:\na = 10\nb = 20\n")
var_c=int(input("Masukan nilai c: "))
var_d=int(input("Masukan nilai d: "))
space=var_a
var_a=var_b
var_b=space
var_c=var_c^var_d
var_d=var_c^var_d
var_c=var_c^var_d
print("\nSetelah ditukar:\na = {0}\nb = {1}\nc = {2}\nd = {3}".format(var_a,var_b,var_c,var_d))
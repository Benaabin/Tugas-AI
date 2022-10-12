var = input("INPUT 1: ")
try:
    bil = int(input("INPUT 2: "))
    print(var+bil)
except(TypeError,ValueError) as n:
    print(n)
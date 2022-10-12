def fungsi_fibonaci(x):
    if x <= 1:
       return x
    else:
       return(fungsi_fibonaci(x-1) + fungsi_fibonaci(x-2))

var = int(input("Masukan bilangan : "))

if var <= 0:
    print("Tolong masukan bilangan positif")
else:
    print("Bilangan Fibonaci:")
    for i in range(var):
        print(fungsi_fibonaci(i))
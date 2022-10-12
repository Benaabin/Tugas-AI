listku = [12,11,10,9,8,7,6,5,4,3,2,1]
size = 3
def fungsi(listA,size):
    for n in range(0,len(listA),size):
        yield listA[n:n + size]

print(list(fungsi(listku,size)))
list_1 = [1, 2, 3, 1, 4, 5, 6, 7, 8]
list_2 = [3, 5, 6, 7, 8, 1]

print(list(set(list_1) ^ set(list_2)))
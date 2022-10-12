lib = {5:6,1:1,2:2,4:5}
sorted={key: value for key, value in sorted(lib.items(), key=lambda item: item[1])}
print(sorted)

from turtle import update


file1={1:"I",2:"K"}
file2={1:"L",2:"2",3:"M"}
file3={4:"z"}
new_file = file2.copy()
new_file.update(file1)
new_file.update(file3)
print(new_file)
import pathlib

print(pathlib.Path("file.txt").parent.absolute())
print(pathlib.Path().absolute())
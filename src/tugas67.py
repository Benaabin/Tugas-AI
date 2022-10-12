from distutils import filelist


with open("file.txt")as f:
    fileList = f.readlines()

print(fileList)
fileList=[x.strip() for x in fileList]
print(fileList)
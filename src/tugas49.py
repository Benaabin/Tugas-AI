import os

try:
    os.makedirs("Python\Tugas-AI\dir")
except FileExistsError:
    print("File already exists")
current_dir=os.getcwd()
print(current_dir)
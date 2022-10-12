def isi(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(isi("file.txt"))
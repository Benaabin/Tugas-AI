from pathlib import Path

file = Path('file.txt')
foto = Path('foto.png')
print(file.stat().st_size)
print(foto.stat().st_size)
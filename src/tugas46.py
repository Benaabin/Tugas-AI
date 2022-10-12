import hashlib

def file(namafile):
    location = hashlib.sha1()
    with open(namafile,"rb") as file:
        var=0
        while var != b'':
            var = file.read(1024)
            location.update(var)
    return location.hexdigest()

locate = file("foto.png")
print(locate)
def resolution(filename):
   with open(filename,'rb') as img_file:

       img_file.seek(163)

       a = img_file.read(2)

       tinggi = (a[0] << 8) + a[1]

       a = img_file.read(2)

       lebar = (a[0] << 8) + a[1]

   print("Resolusi dari foto adalah",tinggi,"x",lebar)

resolution("foto.png")
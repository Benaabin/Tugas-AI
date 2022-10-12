import os.path, time

file = 'tugas81.py'
print("Waktu terakhir dirubah: %s" % time.ctime(os.path.getmtime(file)))
print("Waktu terakhir metadata merubah time atau lokasi : %s" % time.ctime(os.path.getctime(file)))
import time

def hitung(detik):
    while detik:
        menit, detik = divmod(detik, 60)
        format = '{:02d}:{:02d}'.format(menit, detik)
        print(format, end='\n')
        time.sleep(1)
        detik -= 1

    print("stop")

hitung(10)
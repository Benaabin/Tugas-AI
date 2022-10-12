with open("judul.txt", 'r', encoding='utf-8') as judul_file:

    with open("isi.txt", 'r', encoding='utf-8') as isi_file:

        isi = isi_file.read()

        for judul in judul_file:
            mail = "Hello " + judul.strip() + "\n" + isi
            with open(judul.strip()+".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)
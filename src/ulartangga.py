import ulartangga_klasik
import ulartangga_strategi
import os

def awal():
    def sub_Main():
        def window():
            os.system('cls')
            print(f"============================== ULAR TANGGA ==============================")
            print(f"                                   Mode                                  ")
            print(f"1. Klasik")
            print(f"2. Strategi")
            print(f"3. Kembali")
            print(f"=========================================================================")
        def input_nama(mode:any):
            while True:
                try:
                    window()
                    print(f"Nama Pemain\n")
                    pemain1 = input(f"Pemain 1: ")
                    if len(pemain1) >= 1 and len(pemain1) <= 11:
                        break
                    else:
                        print(f"Nama harus terdiri dari 1 - 11 karakter")
                except:
                    pass
                input(f"...ENTER...")
            while True:
                try:
                    window()
                    print(f"Nama Pemain\n")
                    print(f"Pemain 1: {pemain1}")
                    pemain2 = input(f"Pemain 2: ")
                    if (len(pemain2) >= 1 and len(pemain2) <= 11) and (pemain1 != pemain2):
                        mode.main(pemain1, pemain2)
                        break
                    if (len(pemain2) >= 1 and len(pemain2) <= 11):
                        print(f"Nama harus berbeda dengan Pemain 1")
                    else:
                        print(f"Nama harus terdiri dari 1 - 11 karakter")
                except:
                    pass
                input(f"...ENTER...")

        while True:
            window()
            try:
                pilih = int(input(f"Pilih: "))
                if pilih == 1:
                    input_nama(ulartangga_klasik)
                    return
                elif pilih == 2:
                    input_nama(ulartangga_strategi)
                    return
                elif pilih == 3:
                    break
                else:
                    pass
            except:
                pass
            input(f"...ENTER...")
        
    def sub_Peraturan():
        while True:
            os.system('cls')
            print(f"============================== ULAR TANGGA ==============================")
            print(f"                                Peraturan                                ")
            print(f"Petunjuk Umum")
            print(f"Tujuan: Pemain akan mulai dari petak 0 untuk mencapai petak 100.         ")
            print(f"        Pemain bergiliran melempar dadu dan melangkah sebanyak nilai     ")
            print(f"        pada mata dadu.                                                  ")
            print(f"Finish: Jika nilai mata dadu melebihi jumlah yang dibutuhkan untuk       ")
            print(f"        mencapai 100, pemain akan mundur kembali sesuai jumlah dadu.     ")
            print(f"        Pemain akan dinyatakn menang ketika tepat di petak ke-100        ")
            print(f"Petak :                                                                  ")
            print(f"x[0]  = Petak NORMAL  > diam di tempat                                   ")
            print(f"x[-x] = Petak ULAR    > turun sebanyak x                                 ")
            print(f"x[x]  = Petak TANGGA  > naik sebanyak x                                  ")
            print(f"\nContoh                                                                 ")
            print(f" Nomor Petak, petak ke-14  v                                             ")
            print(f"                          14[-6]                                         ")
            print(f"                              ^  jenis petak, petak ular, turun 6 langkah")
            print('')
            print(f"Mode Klasik                                                              ")
            print(f"Dadu  : 1 dadu dengan kesempatan seimbang 1/6                            ")
            print('')
            print(f"Mode Strategi                                                            ")
            print(f"Pemain akan mendapatkan pilihan 4 jurus dari 6 jurus yang tersedia.      ")
            print(f"Setelah pemain memilih jurus, jurus itu akan terpakai dan hilang dari    ")
            print(f"opsi(kecuali jurus lempar biasa). Kemudian akan muncul jurus baru secara ")
            print(f"random di opsi terakhir.                                                 ")
            print(f"Jurus yang tersedia:                                                     ")
            print(f"Lempar Biasa        = lempar biasa dengan 2 dadu. (bisa dipakai setiap saat)")
            print(f"Kali Mata Dadu      = lempar biasa dengan 2 dadu, tapi mata dadu dikali. ")
            print(f"Lempar Ulang 1 Dadu = lempar biasa dengan 1 dadu, 1 dadu lainnya tetap,  ")
            print(f"                      kemudian dijumlahkan.                              ")
            print(f"Salin Mata Dadu     = pakai mata dadu yang tampak saat ini, kemudian     ")
            print(f"                      dijumlahkan.                                       ")
            print(f"Mata Kembar         = lempar kedua dadu, tapi pasti dapat angka kembar,  ")
            print(f"                      kemudian dijumlahkan.                              ")
            print(f"Lempar Jitu         = tentukan nilai 1 dadu, 1 dadu lainnya tetap,       ")
            print(f"                      kemudian dijumlahkan.                              ")
            print(f"=========================================================================")

            pilih: input(f"...ENTER...")
            if pilih is True:
                break

    def sub_Statistik():
        def tampilkan_data(file:str):
            with open(file, "r") as f:
                for line in f:
                    nama, skor = line.strip().split(",")

                    panjang = 10 - len(nama)
                    spasi = ' '
                    for i in range(panjang):
                        spasi = spasi + ' '

                    print(f"{nama}{spasi}: {skor}x")
        while True:
            os.system('cls')
            print(f"============================== ULAR TANGGA ==============================")
            print(f"                                Statistik                                ")
            print(f"                           Pemenang Sebelumnya                           ")
            print(f"------------------------------ K L A S I K ------------------------------")
            tampilkan_data('data.txt')
            print(f"---------------------------- S T R A T E G I ----------------------------")
            tampilkan_data('data2.txt')
            print(f"=========================================================================")

            pilih: input(f"...ENTER...")
            if pilih is True:
                break

    def sub_Info():
        while True:
            os.system('cls')
            print(f"============================== ULAR TANGGA ==============================")
            print(f"                                  Info                                   ")
            print(f"Developer                                                                ")
            print(f"Muzakki Abdul Aziz\nD4SM-46-01                                           ")
            print(f"\nHasil pengembangan game ular tangga dari proyek yang disediakan sebagai")
            print(f"pemenuhan Assessment 2 Mata Kuliah Algoritma & Pemerograman, jurusan     ")
            print(f"Teknologi Rekayasa Multimedia, Universitas Telkom 2023.                  ")
            print(f"=========================================================================")

            pilih: input(f"...ENTER...")
            if pilih is True:
                break

    # BAGIAN UTAMA
    while True:
        os.system('cls')
        print(f'============================== ULAR TANGGA ==============================')
        print(f"1. Main")
        print(f"2. Peraturan")
        print(f"3. Statistik")
        print(f"4. Info")
        print(f"5. Keluar")
        print(f'=========================================================================')

        try:
            pilih = int(input(f"Pilih: "))

            if pilih == 1:
                sub_Main()
            elif pilih == 2:
                sub_Peraturan()
            elif pilih == 3:
                sub_Statistik()
            elif pilih == 4:
                sub_Info()
            elif pilih == 5:
                print(f"...Telah Keluar...")
                break

            else:
                pass
        except:
            pass

        input(f"...ENTER...")

while True:
    awal()
    break

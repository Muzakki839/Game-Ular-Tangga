import random
from papan import Papan
from alat import Pion
from alat import Dadu_Ajaib
from alat import save
import os

def main(pemain1:str, pemain2:str):
    papan = Papan(101, 0.015, 0.015, 0.96)
    pion1 = Pion(pemain1, 1)
    pion2 = Pion(pemain2, 2)
    dadu = Dadu_Ajaib()
    giliran = int(1)
    giliran_nama = str()
    putaran = int(1)
    jurus = ['Lempar Biasa', 'Kali Mata Dadu', 'Lempar Ulang 1 Dadu', 'Salin Mata Dadu', 'Mata Kembar', 'Lempar Jitu']
    list_jurus = ['Lempar Biasa']

#=============================================================================================
    def spasi(nama_pemain:str):
        panjang = 10 - len(nama_pemain)
        spasi = ' '
        for i in range(panjang):
            spasi = spasi + ' '
        return spasi
    
    def tampilkan_stat():
        os.system ('cls')
        print('============================== ULAR TANGGA ==============================')
        print('                             S T R A T E G I                             ')
        print('')
        Papan.print_kotak(papan)
        print('', end='\n\n')
        print('================================ POSISI =================================')
        print(f"                              Putaran Ke-{putaran}")
        print(f"{pemain1}{spasi1}: {pion1.get_posisi()}")
        print(f"{pemain2}{spasi2}: {pion2.get_posisi()}")
        print(f"Mata Dadu 1: {dadu.get_mata(1)}         Mata Dadu 2 : {dadu.get_mata(2)}")
        print('=========================================================================')

    def pasca_lempar(old_posisi:int):
        tampilkan_stat()
        print(f"Giliran    : {giliran_nama}")
        print(f"Petak Asal : {old_posisi}         (Butuh [{100 - old_posisi}] langkah menuju 100)")
        print('')

    def log_dadu(posisi_setelah_dadu:int, jenis_dadu:int, kode:int):
        if jenis_dadu == 0: # dadu normal
            print(f"[+{dadu.get_mata(0)}] dari Dadu ke Petak {posisi_setelah_dadu}")

        elif jenis_dadu == 1: # dadu kali
            print(f"[{dadu.get_mata(1)}] Dadu 1 x [{dadu.get_mata(2)}] Dadu 2 = [{dadu.get_mata(1) * dadu.get_mata(2)}]\n")
            print(f"[+{dadu.get_mata(1) * dadu.get_mata(2)}] dari Dadu ke Petak {posisi_setelah_dadu}")

        elif jenis_dadu == 2: # ubah 1 dadu
            if kode == 1:
                print(f"Dadu 1 menjadi [{dadu.get_mata(1)}], Dadu 2 Tetap\n")
            if kode == 2:
                print(f"Dadu 1 Tetap, Dadu 2 menjadi [{dadu.get_mata(2)}]\n")
            print(f"[+{dadu.get_mata(0)}] dari Dadu ke Petak {posisi_setelah_dadu}")
            
        elif jenis_dadu == 3: # salin dadu
            print(f"[{dadu.get_mata(1)}] Dadu 1 & [{dadu.get_mata(2)}] Dadu 2 = [{dadu.get_mata(1) + dadu.get_mata(2)}] Disalin\n")
            print(f"[+{dadu.get_mata(0)}] dari Dadu ke Petak {posisi_setelah_dadu}")

        elif jenis_dadu == 4: # dadu kembar
            print(f"Dadu Kembar bermata [{dadu.get_mata(1)}] \n")
            print(f"[+{dadu.get_mata(0)}] dari Dadu ke Petak {posisi_setelah_dadu}")

    def hitung_posisi(old_posisi:int, posisi_setelah_dadu:int, pion:object, jenis_dadu:int, kode:int):
        # jika dadu + posisi awal > 100, mundur sesuai jmlh lebihnya
        if (posisi_setelah_dadu) > 100:
            # hitung
            lebih = (posisi_setelah_dadu) - 100
            pion.set_posisi(100 - (lebih))

            # log
            pasca_lempar(old_posisi)
            log_dadu(posisi_setelah_dadu, jenis_dadu, kode)
            print(f"Melebihi Petak 100 !!")
            print(f"Mundur [{lebih}] langkah ke Petak {pion.get_posisi()}")
            old_posisi = pion.get_posisi()


        # Ultang pertama (setelah dadu)
        else: 
            # hitung
            posisi_setelah_ultang = pion.get_posisi() + papan.get_kotak(pion.get_posisi())
            pion.set_posisi(posisi_setelah_ultang)

            # Log
            pasca_lempar(old_posisi)
            log_dadu(posisi_setelah_dadu, jenis_dadu, kode)
            if (papan.get_kotak(posisi_setelah_dadu)) <0: #ular
                print(f"[{papan.get_kotak(posisi_setelah_dadu)}] dari Ular ke Petak {posisi_setelah_ultang}")

            if (papan.get_kotak(posisi_setelah_dadu)) >0: #tangga
                print(f"[+{papan.get_kotak(posisi_setelah_dadu)}] dari Tangga ke Petak {posisi_setelah_ultang}")


        # ultang berkelanjutan
        while papan.get_kotak(pion.get_posisi()) != 0: 
            input(f"Belum di Petak Normal, lanjutkan perjalan !")
            
            # old_posisi = pion.get_posisi()
            old_posisi = pion.get_posisi()

            # hitung
            posisi_setelah_ultang = pion.get_posisi() + papan.get_kotak(pion.get_posisi())
            pion.set_posisi(posisi_setelah_ultang)

            # log
            tampilkan_stat()
            print(f"Giliran    : {giliran_nama}")
            print(f"Petak Asal : {old_posisi}         (Butuh [{100 - old_posisi}] langkah menuju 100)")
            print('')
            if (papan.get_kotak(old_posisi)) <0: #ular
                print(f"[{papan.get_kotak(old_posisi)}] dari Ular ke Petak {posisi_setelah_ultang}")

            if (papan.get_kotak(old_posisi)) >0: #tangga
                print(f"[+{papan.get_kotak(old_posisi)}] dari Tangga ke Petak {posisi_setelah_ultang}")

    # ---------------------------------------------------------------------------------------------------
    def lempar_dadu(pion:object, dadu:int):
        input('Lempar Dadu !')
        if (pion.posisi) < 100:
            dadu.lempar()

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + dadu.get_mata(0)
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion, 0, 0)

    def lempar_dadu_kali(pion:object, dadu:int):
        input('Lempar Dadu Perkalian !')
        if (pion.posisi) < 100:
            dadu.lempar()

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + (dadu.get_mata(1) * dadu.get_mata(2))
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion, 1, 0)

    def lempar_1dadu(pion:object, dadu:int):
        input('Lempar 1 Dadu !')
        if (pion.posisi) < 100:
            old_posisi = pion.get_posisi()
            while True:
                try:
                    tampilkan_stat()
                    print(f"Giliran    : {giliran_nama}")
                    print(f"Petak Asal : {old_posisi}         (Butuh [{100 - old_posisi}] langkah menuju 100)")
                    print(f"\nPilih Dadu yang ingin diacak: (1/2)?")
                    pilih_dadu = int(input(f"Pilih                       : "))
                    if pilih_dadu == 1:
                        dadu.lempar1()
                        kode = 1
                        break
                    if pilih_dadu == 2:
                        dadu.lempar2()
                        kode = 2
                        break
                    else:
                        pass
                except:
                    pass

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + dadu.get_mata(0)
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion, 2, kode)

    def salin_dadu(pion:object, dadu:int):
        input('Salin Dadu !')
        if (pion.posisi) < 100:

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + dadu.get_mata(0)
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion, 3, 0)

    def lempar_dadu_kembar(pion:object, dadu:int):
        input('Pasti Dadu Kembar!')
        if (pion.posisi) < 100:
            dadu.lempar()
            while dadu.get_mata(1) != dadu.get_mata(2):
                dadu.lempar()

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + dadu.get_mata(0)
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion, 4, 0)

    def tentukan_1dadu(pion:object, dadu:int):
        input('Tentukan 1 Dadu !')
        if (pion.posisi) < 100:
            old_posisi = pion.get_posisi()
            while True:
                try:
                    tampilkan_stat()
                    print(f"Giliran    : {giliran_nama}")
                    print(f"Petak Asal : {old_posisi}         (Butuh [{100 - old_posisi}] langkah menuju 100)")
                    print(f"\nPilih Dadu yang ingin ditentukan: (1/2)?")
                    pilih_dadu = int(input(f"Pilih                           : "))
                    if pilih_dadu == 1:
                        try:
                            ubah = int(input(f"Dadu 1 = "))
                            if (ubah >= 1) and (ubah <= 6):
                                dadu.set_mata(1, ubah)
                                kode = 1
                                break
                            else:
                                input(f"Masukkan angka 1 - 6")
                        except:
                            pass
                    if pilih_dadu == 2:
                        try:
                            ubah = int(input(f"Dadu 2 = "))
                            if (ubah >= 1) and (ubah <=6):
                                dadu.set_mata(2, ubah)
                                kode = 2
                                break
                            else:
                                input(f"Masukkan angka 1 - 6")
                        except:
                            pass
                    else:
                        pass
                except:
                    pass

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + dadu.get_mata(0)
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion, 2, kode)
# --------------------------------------------------------------------------------------------

    def atur_tambah_opsi(max_opsi:int):
        while len(list_jurus) != max_opsi:
            acak = random.randint(1, 5)
            if acak == 1:
                list_jurus.append(jurus[1])
            elif acak == 2:
                list_jurus.append(jurus[2])
            elif acak == 3:
                list_jurus.append(jurus[3])
            elif acak == 4:
                list_jurus.append(jurus[4])
            elif acak == 5:
                list_jurus.append(jurus[5])

    def print_opsi(list_jurus:list):
        print(f"Pilih Jurus:")
        for i, list_jurus in enumerate(list_jurus):
            print(f"{i + 1}. {list_jurus}")

    def pilih_opsi(pion:object, list_jurus:list):
        def sesuaikan_jurus():
            if terpilih == jurus[0]:
                lempar_dadu(pion, dadu)
            elif terpilih == jurus[1]:
                lempar_dadu_kali(pion, dadu)
            elif terpilih == jurus[2]:
                lempar_1dadu(pion, dadu)
            elif terpilih == jurus[3]:
                salin_dadu(pion, dadu)
            elif terpilih == jurus[4]:
                lempar_dadu_kembar(pion, dadu)
            elif terpilih == jurus[5]:
                tentukan_1dadu(pion, dadu)
        while True:
            try:
                old_posisi = pion.get_posisi()

                tampilkan_stat()
                print(f"Giliran    : {giliran_nama}")
                print(f"Petak Asal : {old_posisi}         (Butuh [{100 - old_posisi}] langkah menuju 100)")
                print('')
                atur_tambah_opsi(4)
                print_opsi(list_jurus)
                pilih = int(input("\nPilih: "))
                if pilih < 1 or pilih > len(list_jurus):
                    pass
                else:
                    terpilih = list_jurus[pilih - 1]

                    if terpilih == list_jurus[0]:
                        sesuaikan_jurus()
                    elif terpilih == list_jurus[1]:
                        sesuaikan_jurus()
                    elif terpilih == list_jurus[2]:
                        sesuaikan_jurus()
                    elif terpilih == list_jurus[3]:
                        sesuaikan_jurus()
                    elif terpilih == list_jurus[4]:
                        sesuaikan_jurus()
                    elif terpilih == list_jurus[5]:
                        sesuaikan_jurus()

                    if terpilih == list_jurus[0]:
                        pass
                    else:
                        # pass
                        del list_jurus[pilih - 1]

                    break                    
            except:
                pass           

# --------------------------------------------------------------------------------------------
    spasi1 = spasi(pemain1)
    spasi2 = spasi(pemain2)

    while True:
        tampilkan_stat()
        
        if pion1.id == giliran:
            giliran_nama = (pion1.get_nama())
            print(f"Giliran    : {giliran_nama}")

            pilih_opsi(pion1, list_jurus)

            putaran += 1

            if (dadu.get_mata(1)) == (dadu.get_mata(2)) == 6:
                input(f"\n... Jalan Lagi !! ...")
            else:
                giliran = pion2.id
                input('\n...ENTER...')

            tampilkan_stat()

            if (pion1.posisi) == 100:
                break

        if pion2.id == giliran:
            giliran_nama = (pion2.get_nama())
            print(f"Giliran    : {giliran_nama}")
            
            pilih_opsi(pion2, list_jurus)

            putaran += 1

            if (dadu.get_mata(1)) == (dadu.get_mata(2)) == 6:
                input(f"\n... Jalan Lagi !! ...")
            else:
                giliran = pion1.id
                input('\n...ENTER...')

            tampilkan_stat()

            if (pion2.posisi) == 100:
                break
#==========================================================================================
    if pion1.posisi == 100:
        pemenang = pion1.nama
    elif pion2.posisi == 100:
        pemenang = pion2.nama

    save('data2.txt', pemenang)

    def tampilkan_pemenang():
        if pion1.posisi == 100:
            print(f"Pemenangnya: {pion1.nama} !!")
        if pion2.posisi == 100:
            print(f"Pemenangnya: {pion2.nama} !!")
        
    tampilkan_stat()
    tampilkan_pemenang()

    while True:
        try:
            kembali = input('Kembali ke Menu Utama? (y/n) ')
            if kembali == 'y':
                break
            else:
                tampilkan_stat()
                tampilkan_pemenang()
        except:
            tampilkan_stat()
            tampilkan_pemenang()
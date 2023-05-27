from papan import Papan
from alat import Pion
from alat import Dadu
from alat import save
import os


def main(pemain1:str, pemain2:str):
    papan = Papan(101, 0.015, 0.015, 0.96)
    pion1 = Pion(pemain1, 1)
    pion2 = Pion(pemain2, 2)
    dadu = Dadu()
    giliran = int(1)
    giliran_nama = str()
    putaran = int(1)

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
        print('                               K L A S I K                               ')
        print('')
        Papan.print_kotak(papan)
        print('', end='\n\n')
        print('================================ POSISI =================================')
        print(f"                              Putaran Ke-{putaran}")
        print(f"{pemain1}{spasi1}: {pion1.get_posisi()}")
        print(f"{pemain2}{spasi2}: {pion2.get_posisi()}")
        print(f"Mata Dadu  : {dadu.get_mata()}")
        print('=========================================================================')

    def pasca_lempar(old_posisi:int):
        tampilkan_stat()
        print(f"Giliran    : {giliran_nama}")
        print(f"Petak Asal : {old_posisi}         (Butuh [{100 - old_posisi}] langkah menuju 100)")
        print('')

    def log_dadu(posisi_setelah_dadu:int):
        print(f"[+{dadu.get_mata()}] dari Dadu ke Petak {posisi_setelah_dadu}")

    def hitung_posisi(old_posisi:int, posisi_setelah_dadu:int, pion:object):
        # jika dadu + posisi awal > 100, mundur sesuai jmlh lebihnya
        if (posisi_setelah_dadu) > 100:
            # hitung
            lebih = (posisi_setelah_dadu) - 100
            pion.set_posisi(100 - (lebih))

            # log
            pasca_lempar(old_posisi)
            log_dadu(posisi_setelah_dadu)
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
            log_dadu(posisi_setelah_dadu)
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

    def lempar_dadu(pion:object, dadu:int):
        input('Lempar Dadu !')
        if (pion.posisi) < 100:
            dadu.lempar()

            old_posisi = pion.get_posisi()
            # hitung normal
            posisi_setelah_dadu = pion.get_posisi() + dadu.get_mata()
            pion.set_posisi(posisi_setelah_dadu)

            # hitung ultang
            hitung_posisi(old_posisi, posisi_setelah_dadu, pion)

# =============================================================================================

    spasi1 = spasi(pemain1)
    spasi2 = spasi(pemain2)

    while True:
        tampilkan_stat()
        
        if pion1.id == giliran:
            giliran_nama = pion1.get_nama()
            print(f"Giliran    : {giliran_nama}")
            lempar_dadu(pion1, dadu)
            
            putaran += 1

            input('\n...ENTER...')
            giliran = pion2.id
            tampilkan_stat()

            if (pion1.posisi) == 100:
                break

        if pion2.id == giliran:
            giliran_nama = pion2.get_nama()
            print(f"Giliran    : {giliran_nama}")
            lempar_dadu(pion2, dadu)

            putaran += 1

            input('\n...ENTER...')
            giliran = pion1.id
            tampilkan_stat()

            if (pion2.posisi) == 100:
                break
    #==========================================================================================

    if pion1.posisi == 100:
        pemenang = pion1.nama
    elif pion2.posisi == 100:
        pemenang = pion2.nama

    save('data.txt', pemenang)

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
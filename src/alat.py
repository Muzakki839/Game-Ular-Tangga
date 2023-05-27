from audioop import reverse
import random
import os

class Pion:
    def __init__(self, nama: str, id: int):
        self.nama = nama
        self.id = id
        self.posisi = int(0)

    def set_posisi (self, posisi: int):
        self.posisi = posisi

    def get_posisi (self):
        return self.posisi

    def get_nama (self):
        return self.nama

    def get_id (self):
        return self.id

class Dadu:
    def __init__(self):
        self.mata = int
        self.lempar()

    def lempar (self):
        self.mata = random.randint(1, 6)

    def get_mata (self):
        return self.mata

class Dadu_Ajaib:
    def __init__(self):
        self.mata = int
        self.mata1 = int
        self.mata2 = int
        self.lempar()

    def lempar (self):
        self.lempar1()
        self.lempar2()
        self.mata = self.mata1 + self.mata2

    def lempar1 (self):
        self.mata1 = random.randint (1, 6)

    def lempar2 (self):
        self.mata2 = random.randint (1, 6)

    def set_mata(self, dadu_ke:int, ubah:int):
        if dadu_ke == 0:
            self.mata = ubah
            return self.mata
        elif dadu_ke == 1:
            self.mata1 = ubah
            return self.mata1
        elif dadu_ke == 2:
            self.mata2 = ubah
            return self.mata2
        else:
            print(f"Terjadi kesalahan sistem!")

    def get_mata (self, dadu_ke:int):
        if dadu_ke == 0:
            self.mata = self.mata1 + self.mata2
            return self.mata
        elif dadu_ke == 1:
            return self.mata1
        elif dadu_ke == 2:
            return self.mata2
        else:
            print(f"Terjadi kesalahan sistem!")

def save(filename:str, pemenang:str):
    data_pemenang = {}
    with open(filename, 'a'):
        pass
    
    with open(filename, "r") as f:
        for line in f:
            nama, skor = line.strip().split(",")
            data_pemenang[nama] = int(skor)

    if pemenang in data_pemenang:
        data_pemenang[pemenang] += 1
    else:
        data_pemenang[pemenang] = 1

    with open(filename, "w") as f:
        for nama, skor in sorted(data_pemenang.items(), key=lambda x:x[1], reverse=True):
            f.write(f"{nama}, {skor}\n")


import random

class Papan:
    def __init__ (self, jumlah_kotak: int, prob_ular:float, prob_tangga:float, prob_normal:float):
        self.jumlah_kotak = jumlah_kotak
        self.kotak = {}
        self.buat_papan(prob_ular, prob_tangga, prob_normal)

    def buat_papan (self, prob_ular:float, prob_tangga:float, prob_normal:float):
        for i in range(self.jumlah_kotak):
            result = self.rand_ultang(prob_ular, prob_tangga, prob_normal)

            self.kotak[i] = result #meletakkan ultang ke kotak

            # fixing supaya gk ada ular yg ujungnya di bwh 0
            while result <= i and i <= 10:
                result = self.rand_ultang(prob_ular, prob_tangga, prob_normal)
                self.kotak[i] = result
                if result >= i or result == 0:
                    break

            # fixing supaya gk ada tangga yg ujungnya lebih dari 100(jumlah_kotak)
            while ((result + i) >= (self.jumlah_kotak-1)):
                result = self.rand_ultang(prob_ular, prob_tangga, prob_normal)
                self.kotak[i] = result
                if ((result + i) < (self.jumlah_kotak-1)) or result == 0:
                    break
        
            # fixing supaya gk ada loop dari kombinasi ultang, misal 11[1] dan 12[-1]
            while result + self.kotak.get(i + result, 0) == 0:
                result = self.rand_ultang(prob_ular, prob_tangga, prob_normal)

        # fixing supaya start n finish gk ada ultang
        self.kotak[0] = 0 #awal
        self.kotak[self.jumlah_kotak - 1] = 0 #akhir

    def print_kotak(self):
        i = 11
        for x, y in self.kotak.items():
            if x >= i:
                print('\n')
                print(f"{x}[{y}]  ", end='')
                i = i + 10
            else:
                print(f"{x}[{y}]  ", end='')

    def get_kotak(self, nomor:int):
        return self.kotak[nomor]

    def rand_ultang(self, prob_ular:float, prob_tangga:float, prob_normal:float): # nanti yg float diisi probabilitas
        # jenis kotak
        ular = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
        tangga = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        normal = [0]
        ultang = ular + normal + tangga

        # probabilitas jenis kotak
        prob_ultang = [prob_ular] * len(ular) + [prob_normal] * len(normal) + [prob_tangga] * len(tangga)
        result = random.choices(ultang, weights=prob_ultang)[0]
        return result

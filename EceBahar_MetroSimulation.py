from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx, ad, hat):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular = []

    def komsu_ekle(self, diger, sure):
        self.komsular.append((diger, sure))


class MetroAgi:
    def __init__(self):
        self.istasyonlar = {}
        self.hatlar = {}

    def istasyon_ekle(self, kod, ad, hat):
        if kod not in self.istasyonlar:
            yeni = Istasyon(kod, ad, hat)
            self.istasyonlar[kod] = yeni
            if hat not in self.hatlar:
                self.hatlar[hat] = []
            self.hatlar[hat].append(yeni)

    def baglanti_ekle(self, kod1, kod2, sure):
        i1 = self.istasyonlar[kod1]
        i2 = self.istasyonlar[kod2]
        i1.komsu_ekle(i2, sure)
        i2.komsu_ekle(i1, sure)


if __name__ == "__main__":
    metro = MetroAgi()

    metro.istasyon_ekle("S1", "Harput", "Sarı Hat")
    metro.istasyon_ekle("S2", "Çaydaçıra", "Sarı Hat")
    metro.istasyon_ekle("S3", "Öğretmenevi", "Sarı Hat")
    metro.istasyon_ekle("S4", "Abdullahpaşa", "Sarı Hat")

   
    metro.istasyon_ekle("M1", "Üniversite", "Mavi Hat")
    metro.istasyon_ekle("M2", "Öğretmenevi", "Mavi Hat")
    metro.istasyon_ekle("M3", "Hilalkent", "Mavi Hat")
    metro.istasyon_ekle("M4", "Doğukent", "Mavi Hat")

   
    metro.istasyon_ekle("Y1", "Abdullahpaşa", "Yeşil Hat")
    metro.istasyon_ekle("Y2", "Hilalkent", "Yeşil Hat")
    metro.istasyon_ekle("Y3", "Sanayi", "Yeşil Hat")
    metro.istasyon_ekle("Y4", "Havalimanı", "Yeşil Hat")

   
    metro.baglanti_ekle("S1", "S2", 5)
    metro.baglanti_ekle("S2", "S3", 4)
    metro.baglanti_ekle("S3", "S4", 6)

    metro.baglanti_ekle("M1", "M2", 7)
    metro.baglanti_ekle("M2", "M3", 5)
    metro.baglanti_ekle("M3", "M4", 6)

    metro.baglanti_ekle("Y1", "Y2", 5)
    metro.baglanti_ekle("Y2", "Y3", 7)
    metro.baglanti_ekle("Y3", "Y4", 8)

    metro.baglanti_ekle("S3", "M2", 2)
    metro.baglanti_ekle("S4", "Y1", 2)
    metro.baglanti_ekle("M3", "Y2", 3)



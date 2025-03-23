from collections import deque
import heapq

class Istasyon:
    def __init__(self, idx, ad):
        self.idx = idx
        self.ad = ad
        self.komsular = []

    def komsu_ekle(self, diger, sure):
        self.komsular.append((diger, sure))

    def __lt__(self, other):
        return self.idx < other.idx

class MetroAgi:
    def __init__(self):
        self.istasyonlar = {}

    def istasyon_ekle(self, kod, ad):
        if kod not in self.istasyonlar:
            self.istasyonlar[kod] = Istasyon(kod, ad)

    def baglanti_ekle(self, kod1, kod2, sure):
        i1 = self.istasyonlar[kod1]
        i2 = self.istasyonlar[kod2]
        i1.komsu_ekle(i2, sure)
        i2.komsu_ekle(i1, sure)

    def en_az_aktarma_bul(self, baslangic_id, hedef_id):
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        ziyaret_edilen = set()
        kuyruk = deque()
        kuyruk.append((baslangic, [baslangic.ad]))

        while kuyruk:
            mevcut, yol = kuyruk.popleft()

            if mevcut.idx == hedef.idx:
                return yol

            ziyaret_edilen.add(mevcut.idx)

            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edilen:
                    kuyruk.append((komsu, yol + [komsu.ad]))

        return None

    def en_hizli_rota_bul(self, baslangic_id, hedef_id):
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = []
        heapq.heappush(pq, (0, [baslangic]))
        ziyaret_edilen = {}

        while pq:
            toplam_sure, yol = heapq.heappop(pq)
            mevcut = yol[-1]

            if mevcut.idx == hedef.idx:
                return [ist.ad for ist in yol], toplam_sure

            if mevcut.idx in ziyaret_edilen and ziyaret_edilen[mevcut.idx] <= toplam_sure:
                continue

            ziyaret_edilen[mevcut.idx] = toplam_sure

            for komsu, sure in mevcut.komsular:
                heapq.heappush(pq, (toplam_sure + sure, yol + [komsu]))

        return None

metro = MetroAgi()

metro.istasyon_ekle("A", "AŞTİ")
metro.istasyon_ekle("K", "Kızılay")
metro.istasyon_ekle("U", "Ulus")
metro.istasyon_ekle("D", "Demetevler")
metro.istasyon_ekle("O", "OSB")
metro.istasyon_ekle("B", "Batıkent")
metro.istasyon_ekle("G", "Gar")
metro.istasyon_ekle("S", "Sıhhiye")
metro.istasyon_ekle("K2", "Keçiören")

metro.baglanti_ekle("A", "K", 7)
metro.baglanti_ekle("K", "U", 5)
metro.baglanti_ekle("U", "D", 6)
metro.baglanti_ekle("D", "O", 7)
metro.baglanti_ekle("B", "D", 8)
metro.baglanti_ekle("D", "G", 6)
metro.baglanti_ekle("G", "K2", 7)
metro.baglanti_ekle("G", "S", 4)
metro.baglanti_ekle("S", "K", 3)

print("\n=== Test Senaryoları ===\n")

print("1. AŞTİ'den OSB'ye:")
rota = metro.en_az_aktarma_bul("A", "O")
print("En az aktarmalı rota:", " ➡️ ".join(rota))
rota, sure = metro.en_hizli_rota_bul("A", "O")
print(f"En hızlı rota ({sure} dakika):", " ➡️ ".join(rota))

print("\n2. Batıkent'ten Keçiören'e:")
rota = metro.en_az_aktarma_bul("B", "K2")
print("En az aktarmalı rota:", " ➡️ ".join(rota))
rota, sure = metro.en_hizli_rota_bul("B", "K2")
print(f"En hızlı rota ({sure} dakika):", " ➡️ ".join(rota))

print("\n3. Keçiören'den AŞTİ'ye:")
rota = metro.en_az_aktarma_bul("K2", "A")
print("En az aktarmalı rota:", " ➡️ ".join(rota))
rota, sure = metro.en_hizli_rota_bul("K2", "A")
print(f"En hızlı rota ({sure} dakika):", " ➡️ ".join(rota))


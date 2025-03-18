from collections import defaultdict, deque
import heapq

class Istasyon:
    def __init__(self, idx, ad, hat):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular = []

    def komsu_ekle(self, diger, sure):
        self.komsular.append((diger, sure))

    def __lt__(self, other):
        return self.idx < other.idx


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

    def en_az_aktarma_bul(self, baslangic_id, hedef_id):
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        ziyaret_edilen = set()
        kuyruk = deque()
        kuyruk.append((baslangic, [baslangic]))

        while kuyruk:
            mevcut, yol = kuyruk.popleft()

            if mevcut.idx == hedef.idx:
                return yol

            ziyaret_edilen.add(mevcut.idx)

            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edilen:
                    kuyruk.append((komsu, yol + [komsu]))

        return None

    def en_hizli_rota_bul(self, baslangic_id, hedef_id):
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        pq = []
        heapq.heappush(pq, (0, [baslangic]))
        ziyaret_edilen = {}

        while pq:
            toplam_sure, yol = heapq.heappop(pq)
            mevcut = yol[-1]

            if mevcut.idx == hedef.idx:
                return yol, toplam_sure

            if mevcut.idx in ziyaret_edilen and ziyaret_edilen[mevcut.idx] <= toplam_sure:
                continue

            ziyaret_edilen[mevcut.idx] = toplam_sure

            for komsu, sure in mevcut.komsular:
                heapq.heappush(pq, (toplam_sure + sure, yol + [komsu]))

        return None


def rota_duzenle(rota):
    duzenli = []
    for i in range(len(rota)):
        if i == 0 or rota[i].ad != rota[i - 1].ad:
            duzenli.append(rota[i])
    return duzenli


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

    print("\n=== Test Senaryoları ===\n")

    print("1. Harput'tan Havalimanı'na")
    print("------------------------------")
    rota = metro.en_az_aktarma_bul("S1", "Y4")
    if rota:
        rota = rota_duzenle(rota)
        print("En az aktarmalı rota:\n ", " ➡️ ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("S1", "Y4")
    if sonuc:
        rota, sure = sonuc
        rota = rota_duzenle(rota)
        print(f"En hızlı rota ({sure} dakika):\n ", " ➡️ ".join(i.ad for i in rota))

    print("\n2. Üniversite'den Abdullahpaşa'ya")
    print("------------------------------")
    rota = metro.en_az_aktarma_bul("M1", "S4")
    if rota:
        rota = rota_duzenle(rota)
        print("En az aktarmalı rota:\n ", " ➡️ ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "S4")
    if sonuc:
        rota, sure = sonuc
        rota = rota_duzenle(rota)
        print(f"En hızlı rota ({sure} dakika):\n ", " ➡️ ".join(i.ad for i in rota))

    print("\n3. Havalimanı'ndan Çaydaçıra'ya")
    print("------------------------------")
    rota = metro.en_az_aktarma_bul("Y4", "S2")
    if rota:
        rota = rota_duzenle(rota)
        print("En az aktarmalı rota:\n ", " ➡️ ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("Y4", "S2")
    if sonuc:
        rota, sure = sonuc
        rota = rota_duzenle(rota)
        print(f"En hızlı rota ({sure} dakika):\n ", " ➡️ ".join(i.ad for i in rota))

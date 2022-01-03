class Çalışan():
    personel = []
    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()
    @classmethod
    def personel_sayısını_görüntüle(cls):
        print(len(cls.personel))
    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))
    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls.personel:
            print(kişi)
    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

a = Çalışan("emre")
b = Çalışan("cemre")
c = Çalışan("demre")

Çalışan.personel_sayısını_görüntüle()


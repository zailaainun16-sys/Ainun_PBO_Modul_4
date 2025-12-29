from abc import ABC, abstractmethod
import math

# Class abstrak
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


# Class Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


# Class Persegi Panjang
class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


# Contoh penggunaan
lingkaran = Lingkaran(5)
persegi_panjang = PersegiPanjang(4, 3)

print(f"Luas Lingkaran: {lingkaran.luas():.2f}")
print(f"Keliling Lingkaran: {lingkaran.keliling():.2f}")
print(f"Luas Persegi Panjang: {persegi_panjang.luas()}")
print(f"Keliling Persegi Panjang: {persegi_panjang.keliling()}")

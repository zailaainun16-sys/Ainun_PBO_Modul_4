from abc import ABC, abstractmethod
import math

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari

class PersegiPanjang(Bentuk):
    # d. Tambahkan parameter 'warna'
    def __init__(self, panjang, lebar, warna):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna # Atribut warna

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

# b. Tambahkan class Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

# Contoh penggunaan
l = Lingkaran(5)
# d. Tambahkan argumen warna saat instansiasi PersegiPanjang
p = PersegiPanjang(4, 3, "Merah")
# c. Instansiasi objek Persegi
s = Persegi(6)

print(f"--- Info Lingkaran ---")
print(f"Luas Lingkaran: {l.luas():.2f}")
print(f"Keliling Lingkaran: {l.keliling():.2f}")

print(f"\n--- Info Persegi Panjang ---")
print(f"Luas Persegi Panjang: {p.luas()}")
print(f"Keliling Persegi Panjang: {p.keliling()}")
# d. Tampilkan warnanya
print(f"Warna Persegi Panjang: {p.warna}")

print(f"\n--- Info Persegi ---")
# c. Tampilkan luas dan keliling Persegi
print(f"Luas Persegi: {s.luas()}")
print(f"Keliling Persegi: {s.keliling()}")

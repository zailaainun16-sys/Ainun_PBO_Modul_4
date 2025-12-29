class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    # a. Representasi string (print(obj)) - Sudah ada
    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    # b. Tambahkan method __len__ (len(obj))
    def __len__(self):
        return len(self.nama)

    # Overload untuk operator > (greater than)
    def __gt__(self, other):
        return self.nilai > other.nilai

    # Overload untuk operator + (addition)
    def __add__(self, other):
        # Mengembalikan total nilai
        return self.nilai + other.nilai

    # Overload untuk operator * (multiplication)
    def __mul__(self, faktor):
        # Mengembalikan nilai dikalikan faktor
        return self.nilai * faktor
    
    # c. Implementasikan method __eq__ (equality)
    def __eq__(self, other):
        # Dua mahasiswa dianggap sama jika nilainya sama
        return self.nilai == other.nilai

# d. Buat minimal 2 objek Mahasiswa
m1 = Mahasiswa("ainun", 95)
m2 = Mahasiswa("hasan", 90)
m3 = Mahasiswa("herdi", 85)

list_mahasiswa = [m1, m2, m3]

print("--- Data Mahasiswa ---")
# Representasi string (print(obj))
print(f"Mahasiswa 1: {m1}")
print(f"Mahasiswa 2: {m2}")
print(f"Mahasiswa 3: {m3}")
print("-" * 25)

# b. Tampilkan panjang nama
print(f"Panjang Nama ainun (len(m1)): {len(m1)}")
print("-" * 25)

# c. Perbandingan kesetaraan nilai menggunakan == (memanggil __eq__)
print(f"Apakah Nilai ainun sama dengan hasan (m1 == m2)? {m1 == m2}")
print(f"Apakah Nilai ainun sama dengan herdi (m1 == m3)? {m1 == m3}")
print("-" * 25)

# Operasi matematika (memanggil __add__ dan __mul__)
print(f"Total Nilai ainun + hasan (m1 + m2): {m1 + m2}")
print(f"Nilai hasan x 2 (m2 * 2): {m2 * 2}")
print("-" * 25)

# Pengurutan menggunakan sorted()
print("Daftar Mahasiswa Sebelum Diurutkan:")
for m in list_mahasiswa:
    print(f"- {m.nama} ({m.nilai})")

# Urutkan berdasarkan nilai (d. menggunakan sorted)
# Lambda function mengambil atribut 'nilai' dari setiap objek Mahasiswa
mahasiswa_terurut = sorted(list_mahasiswa, key=lambda x: x.nilai)

print("\nDaftar Mahasiswa Setelah Diurutkan:")
for m in mahasiswa_terurut:
    print(f"- {m.nama} ({m.nilai})")
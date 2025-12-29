class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

# Contoh penggunaan Mahasiswa
a = Mahasiswa("Pouster", 80)
b = Mahasiswa("Ahmad", 90)

print("--- Contoh Operator Overloading ---")
print(a)
print(b)

if b > a:
    print(f"{b.nama} memiliki nilai lebih tinggi")

print("Total nilai:", a + b)
print("Nilai Ahmad x 2 =", b * 2)
print("-" * 35)


def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # validasi input tidak boleh kosong
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong")

        a = float(x)
        b = float(y)

        # validasi bilangan harus positif
        if a < 0 or b < 0:
            raise ValueError("Hanya angka positif yang diperbolehkan")

        if pilihan == "1":
            # PEMBAGIAN
            hasil = a / b  # dapat memunculkan ZeroDivisionError
        elif pilihan == "2":
            # PERKALIAN
            hasil = a * b
        else:
            raise ValueError("Pilihan operasi tidak valid. Gunakan 1 atau 2.")

    except ValueError as ve:
        print("Input salah:", ve)

    except ZeroDivisionError:
        print("Penyebut tidak boleh nol pada operasi pembagian!")

    except Exception as e:
        print("Terjadi kesalahan:", e)

    else:
        # hanya berjalan jika tidak ada error
        print(f"Hasil operasi: {hasil}")

    finally:
        print("Selesai memproses input.")


if __name__ == "__main__":
    operasi()
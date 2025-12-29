from abc import ABC, abstractmethod


# ===== Custom Exception =====
class PoinTidakValidError(Exception):
    """Exception untuk poin tidak valid (negatif)."""
    pass


# ===== Abstraction =====
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# ===== Class Turunan =====
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    # Implementasi abstract method
    def akses(self):
        return "Hak akses Member: dapat mengakses fitur member."

    # Special method __str__
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    # Special method __add__
    def __add__(self, other):
        return self.poin + other.poin

    # Special method __len__
    def __len__(self):
        return len(self.nama)


# ===== Program Utama =====
if __name__ == "__main__":
    try:
        # Input poin dari user
        input_poin = input("Masukkan poin member kedua: ").strip()

        # Validasi input kosong
        if input_poin == "":
            raise ValueError("Input poin tidak boleh kosong!")

        poin_user = int(input_poin)

        # Validasi poin negatif
        if poin_user < 0:
            raise PoinTidakValidError("Poin tidak boleh negatif!")

        # Membuat 2 objek Member
        m1 = Member("Ainun", 50)
        m2 = Member("Hasan", poin_user)

        # Menampilkan info
        print("\n--- Info Member ---")
        print(m1)
        print(m2)

        # Menampilkan hak akses
        print("\nHak Akses:")
        print(m1.akses())

        # Operasi poin
        print("\nJumlah Poin:", m1 + m2)

        # Panjang nama
        print("Panjang nama m1:", len(m1))

    except ValueError as ve:
        print("Error Input:", ve)

    except PoinTidakValidError as pe:
        print("Error Poin:", pe)
        
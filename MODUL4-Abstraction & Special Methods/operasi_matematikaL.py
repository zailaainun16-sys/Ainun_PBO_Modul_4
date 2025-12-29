def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    pilihan = input("Masukkan pilihan (1/2): ").strip()
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # b. Validasi input kosong
        if x == "" or y == "":
            raise ValueError("Input kosong! Silakan masukkan angka.")

        a = float(x)
        b = float(y)

        # c. Validasi angka positif
        if a < 0 or b < 0:
            raise ValueError("Input harus berupa angka positif.")

        if pilihan == "1":
            # Pembagian
            hasil = a / b
        elif pilihan == "2":
            # Perkalian
            hasil = a * b
        else:
            raise ValueError("Pilihan tidak valid. Gunakan 1 atau 2.")

    except ValueError as ve:
        print("Error:", ve)

    except ZeroDivisionError:
        print("Error: Penyebut tidak boleh nol.")

    else:
        # d. Hanya dijalankan jika tidak terjadi exception
        print(f"Hasil operasi: {hasil}")

    finally:
        # e. Selalu dijalankan
        print("Selesai memproses input.")


if __name__ == "__main__":
    operasi()


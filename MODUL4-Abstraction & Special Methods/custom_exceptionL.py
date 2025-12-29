# ===== Custom Exceptions =====
class UmurTerlaluMudaError(Exception):
    """Exception jika umur terlalu muda (< 5)."""
    pass


class UmurTerlaluTuaError(Exception):
    """Exception jika umur melebihi batas maksimum (> 100)."""
    pass


class AkunTidakDiizinkanError(Exception):
    """Exception jika umur tidak memenuhi syarat pendaftaran akun."""
    pass


# ===== Fungsi Validasi Umur =====
def set_umur(umur):
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda. Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua. Maksimal 100 tahun.")
    return umur

# ===== Fungsi Pendaftaran Akun =====
def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError(
            "Pendaftaran akun hanya untuk umur 18 tahun ke atas."
        )
    return "Akun berhasil didaftarkan."


# ===== Program Utama =====
if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur_valid = set_umur(u)
            print("Umur valid:", umur_valid)

            # Cek pendaftaran akun
            hasil = daftar_akun(umur_valid)
            print(hasil)
            break  # Keluar dari loop jika semua valid

        except ValueError:
            print("Error: Input harus berupa bilangan bulat.")

        except UmurTerlaluMudaError as e:
            print("Error:", e)

        except UmurTerlaluTuaError as e:
            print("Error:", e)

        except AkunTidakDiizinkanError as e:
            print("Error:", e)

        finally:
            print("Proses input selesai.\n")


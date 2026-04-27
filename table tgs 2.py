
# Bagian 1: Validasi Nama (Sesuai contoh di gambar)
while True:
    nama_input = input("Masukan nama anda : ")

    # Memeriksa apakah nama yang dimasukkan adalah "fitria"
    if nama_input.lower() == "fitria":
        print("Jika benar akan lanjut ke program selanjutnya")
        print("-" * 20) # Garis pembatas
        break # Keluar dari perulangan jika nama benar
    else:
        print("silahkan coba lagi")
        print("-" * 20) # Garis pembatas

# Bagian 2: Menampilkan Tabel Perkalian
print("\nBuat program yang menampilkan tabel perkalian dari angka yang dimasukkan user (1 sampai 10).\n")
print("Contoh:\n")

# Meminta input angka dari user (disertai penanganan kesalahan jika input bukan angka)
while True:
    try:
        angka = int(input("Masukkan angka: "))
        break # Berhenti jika input adalah angka yang valid
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

# Menampilkan tabel perkalian 1 sampai 10 menggunakan perulangan for
for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")
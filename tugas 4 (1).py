# Aplikasi Manajemen Nilai Mahasiswa
# Penyimpanan data menggunakan list
data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

def tampilkan_data():
    """Menampilkan semua data mahasiswa"""
    if not data_mahasiswa:
        print("\nBelum ada data mahasiswa.")
        return

    print("\n====================================")
    print("          DAFTAR MAHASISWA          ")
    print("====================================")
    print("No | Nama Mahasiswa | Nilai")
    print("------------------------------------")
    for i, mahasiswa in enumerate(data_mahasiswa, 1):
        print(f"{i:2d} | {mahasiswa[0]:14s} | {mahasiswa[1]:5d}")
    print("====================================\n")

def tambah_data():
    """Menambahkan data mahasiswa baru"""
    nama = input("\nMasukkan nama mahasiswa: ").strip()
    try:
        nilai = int(input("Masukkan nilai mahasiswa: "))
        if 0 <= nilai <= 100:
            data_mahasiswa.append([nama, nilai])
            print(f"Data {nama} berhasil ditambahkan!")
        else:
            print("Nilai harus antara 0 - 100!")
    except ValueError:
        print("Nilai harus berupa angka!")
    print()

def ubah_data():
    """Mengubah data mahasiswa berdasarkan nomor urut"""
    tampilkan_data()
    if not data_mahasiswa:
        return

    try:
        nomor = int(input("Masukkan nomor data yang akan diubah: "))
        if 1 <= nomor <= len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ").strip()
            nilai_baru = int(input("Masukkan nilai baru: "))
            if 0 <= nilai_baru <= 100:
                data_mahasiswa[nomor-1] = [nama_baru, nilai_baru]
                print("Data berhasil diubah!")
            else:
                print("Nilai harus antara 0 - 100!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan nomor yang benar!")
    print()

def hapus_data():
    """Menghapus data mahasiswa berdasarkan nomor urut"""
    tampilkan_data()
    if not data_mahasiswa:
        return

    try:
        nomor = int(input("Masukkan nomor data yang akan dihapus: "))
        if 1 <= nomor <= len(data_mahasiswa):
            data_hapus = data_mahasiswa.pop(nomor-1)
            print(f"Data {data_hapus[0]} berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan nomor yang benar!")
    print()

def cari_data():
    """Mencari data mahasiswa berdasarkan nama"""
    nama_cari = input("\nMasukkan nama yang dicari: ").strip().lower()
    ditemukan = False

    print("\n====================================")
    print("          HASIL PENCARIAN           ")
    print("====================================")
    for mahasiswa in data_mahasiswa:
        if nama_cari in mahasiswa[0].lower():
            print(f"Nama : {mahasiswa[0]}")
            print(f"Nilai: {mahasiswa[1]}")
            print("------------------------------------")
            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan!")
    print()

def urutkan_data():
    """Mengurutkan data dari nilai tertinggi ke terendah"""
    if not data_mahasiswa:
        print("\nBelum ada data untuk diurutkan.\n")
        return

    # Mengurutkan berdasarkan nilai (indeks ke-1) secara terbalik
    data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
    print("\nData berhasil diurutkan dari nilai tertinggi!")
    tampilkan_data()

def hitung_rata_rata():
    """Menghitung rata-rata nilai seluruh mahasiswa"""
    if not data_mahasiswa:
        print("\nBelum ada data mahasiswa.\n")
        return

    total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
    jumlah_mhs = len(data_mahasiswa)
    rata_rata = total_nilai / jumlah_mhs

    print(f"\nTotal nilai        : {total_nilai}")
    print(f"Jumlah mahasiswa   : {jumlah_mhs}")
    print(f"Rata-rata nilai    : {rata_rata:.2f}\n")

# Program Utama
while True:
    print("====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA ")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")

    try:
        pilihan = int(input("Pilih menu 1-8: "))
        print()

        if pilihan == 1:
            tampilkan_data()
        elif pilihan == 2:
            tambah_data()
        elif pilihan == 3:
            ubah_data()
        elif pilihan == 4:
            hapus_data()
        elif pilihan == 5:
            cari_data()
        elif pilihan == 6:
            urutkan_data()
        elif pilihan == 7:
            hitung_rata_rata()
        elif pilihan == 8:
            print("Terima kasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1-8.\n")

    except ValueError:
        print("Masukkan angka yang benar!\n")
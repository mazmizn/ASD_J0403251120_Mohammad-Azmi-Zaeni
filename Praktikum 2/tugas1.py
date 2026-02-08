#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas          : Tugas Hands On
#Nama           : Mohammad Azmi Zaeni
#NIM            : J0403251120
#===============================================================


#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 0        : Membuat Fungsi Load Data
#===============================================================


#1) Menu 1 : Tampilkan semua barang.
#Menampilkan seluruh data stok barang (kode, nama, stok).
#2) Menu 2 : Cari barang berdasarkan kode
#Input kode barang dan tampilkan data jika ditemukan. Jika tidak ditemukan,
#tampilkan pesan 'Barang tidak ditemukan'.
#3) Menu 3 : Tambah barang baru
#Input kode, nama, stok awal. Jika kode sudah ada, tampilkan pesan 'Kode
#sudah digunakan'.
#4) Menu 4 : Update stok barang
#Input kode barang, pilih tambah stok atau kurangi stok. Stok tidak boleh negatif.
#5) Menu 5 : Simpan ke file
#Simpan seluruh data terbaru ke stok_barang.txt.
#6) Menu 0 : Keluar
#Keluar dari program dan tampilkan pesan 'Program selesai.'
#===============================================================



#variabel menyimpan data file
nama_file = 'data_barang.txt'

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            kode, nama, stok = baris.split(',') #ambil data per item data
            data_dict[kode] = {'Nama': nama, 'Stok': int(stok)} #memasukkan dalam dictionary
    return data_dict
buka_data = baca_data(nama_file)
#print("jumlah data terbaca: ", len(buka_data))

#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 1        : Membuat Fungsi Menampilkan Data
#===============================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'KODE': <10} | {'Nama': <20} | {'Stok': >5}")
    '''
    {'KODE': <10} artinya kode rata kiri dengan lebar kolom 10 karakter
    {'Nama': <20} artinya nama rata kiri dengan lebar kolom 20 karakter
    {'Stok': >5} artinya stok rata kanan lebar kolom 5 karakter
    '''
    print("-"*35) #membuat garis

    #meanampilkan isi datanya
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]['Nama']
        stok = data_dict[kode]['Stok']
        print(f"{kode: <10} | {nama: <20} | {stok: >5}")
#tampilkan_data(buka_data) # memanggil fungsi untuk menampilkan data
#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 2        : Membuat Fungsi Mencari Data
#===============================================================

def cari_data(data_dict):
    kode_cari = input("Masukkan KODE barang yang ingin dicari: ").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]['Nama']
        stok = data_dict[kode_cari]['Stok']

        print("\n===== Data Barang Ditemukan =====")
        print(f"Kode    : {kode_cari}")
        print(f"Nama    : {nama}")
        print(f"Stok    : {stok}")
    else:
        print("Barang tidak ditemukan.")

#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 3        : Membuat Fungsi Tambah Data
#===============================================================

def tambah_data(data_dict):
    kode = input("Masukkan KODE barang baru: ").strip()

    if kode in data_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan NAMA barang: ").strip()
    
    try:
        stok = int(input("Masukkan STOK awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka. Penambahan dibatalkan.")
        return

    data_dict[kode] = {'Nama': nama, 'Stok': stok}
    print(f"Barang {kode} berhasil ditambahkan.")

#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 4        : Membuat Fungsi Update Stok
#===============================================================

def update_stok(data_dict):
    kode = input("Masukkan KODE barang yang ingin diupdate: ").strip()

    if kode not in data_dict:
        print("Kode barang tidak ditemukan. Update dibatalkan.")
        return

    print("\n1. Tambah Stok")
    print("2. Kurangi Stok")
    pilihan = input("Pilih operasi (1-2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka. Update dibatalkan.")
        return

    stok_lama = data_dict[kode]['Stok']

    if pilihan == '1':
        data_dict[kode]['Stok'] += jumlah
        print(f"Stok {kode} bertambah dari {stok_lama} menjadi {data_dict[kode]['Stok']}.")
    elif pilihan == '2':
        if stok_lama - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
        else:
            data_dict[kode]['Stok'] -= jumlah
            print(f"Stok {kode} berkurang dari {stok_lama} menjadi {data_dict[kode]['Stok']}.")
    else:
        print("Pilihan tidak valid.")

#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 5        : Membuat Fungsi Simpan Data
#===============================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]['Nama']
            stok = data_dict[kode]['Stok']
            file.write(f"{kode},{nama},{stok}\n")

#===============================================================
#Praktikum 2    : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas 6        : Membuat Menu Interaktif
#===============================================================

def main():
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU STOK BARANG ===")
        print("1. Tampilkan Data Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == '1':
            tampilkan_data(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            tambah_data(buka_data)
        elif pilihan == '4':
            update_stok(buka_data)
        elif pilihan == '5':
            simpan_data(nama_file, buka_data)
            print("Data Berhasil Disimpan")
        elif pilihan == '0':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

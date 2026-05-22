#===============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#===============================================================

print("===Membuka file dalam satu string===")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print("Tipe Data", type(isi_file))

#===============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Membaca seluruh isi file data per baris
#===============================================================

print("\n===Membuka file per baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris += 1
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir
        nim, nama, nilai = baris.split(",") #Memisahkan data berdasarkan koma

        print("Baris ke-", jumlah_baris, ":", baris)
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {nilai}") #Memampilkan data terpisah
        print("Tipe Data:", type(baris))


#===============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca Data dan Menyimpan ke Struktur Data List
#===============================================================

data_list = [] #Inisialisasi list kosong untuk menyimpan data

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir
        nim, nama, nilai = baris.split(",") #Memisahkan data satuan dan simpan ke variabel berdasarkan koma
        data_list.append((nim, nama, nilai)) #Menambahkan tuple data ke dalam List
print("===Menampilkan List===")
print(data_list)
print("Contoh record ke-1:", data_list[0])
print("Contoh record ke-2:", data_list[1])
print("Jumlah Record", len(data_list))


#===============================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca Data dan Menyimpan ke Struktur Data Dictionary
#===============================================================

data_dict= {} #Inisialisasi dictionary

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir
        nim, nama, nilai = baris.split(",") #Memisahkan data berdasarkan koma
        data_dict[nim] = {
            "nama": nama,
            "nilai": int(nilai)
        }
print("===Menampilkan Data Dictionary===")
print(data_dict)
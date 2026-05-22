# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index = 0): # Fungsi rekursif mencari nilai terbesar dalam list 

    # Base case (Kondisi Terminal)
    if index == len(data) - 1: # Berhenti jika indeks mencapai elemen terakhir list 
        return data[index] # Mengembalikan elemen terakhir untuk mulai dibandingkan 
 
    # Recursive case
    maks_sisa = cari_maks(data, index + 1) # Fase Winding: mencari nilai maks di sisa list (indeks selanjutnya) 
    # Fase Unwinding (Pengecekan Balik)
    if data[index] > maks_sisa: # Bandingkan elemen saat ini dengan nilai terbesar dari sisa list 
        return data[index] # Jika lebih besar, maka inilah nilai maksimum sementara
    else:
        return maks_sisa # Jika tidak, gunakan nilai maksimum yang ditemukan sebelumnya
    
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 

"""
Base Case (Kondisi Terminal):
Terletak pada baris if index == len(data) - 1. Ini berfungsi sebagai titik henti agar rekursi tidak berjalan selamanya (infinite recursion). Fungsi akan berhenti dan mengembalikan nilai terakhir saat indeks mencapai ujung list.

Recursive Call:
Terletak pada baris cari_maks(data, index + 1). Fungsi memanggil dirinya sendiri dengan menaikkan nilai indeks untuk memecah masalah besar menjadi pencarian di sisa list yang lebih kecil.

Alur Program:
- Fase Winding (Stacking): Program "masuk" menumpuk pemanggilan fungsi ke dalam memori (call stack) hingga mencapai elemen terakhir.
- Fase Unwinding (Unwinding): Setelah mencapai base case, program "keluar" dari tumpukan memori satu per satu sambil membandingkan angka saat ini dengan angka terbesar dari sisa list
- Logika Perbandingan: Nilai yang lebih besar akan terus dioper ke atas (dikembalikan) hingga kembali ke pemanggilan awal sebagai hasil akhir
"""
# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ==========================================================

def biner(n, hasil=""):
    #  Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: 
        print(hasil) 
        return
    
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 

    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") 
biner(3)

"""
Alur:
1. Fungsi biner dipanggil dengan n=3 dan hasil="".
2. Karena panjang hasil (0) tidak sama dengan n (3), fungsi memanggil dirinya sendiri dua kali:
   - Pertama dengan hasil="0"
   - Kedua dengan hasil="1"
3. Pada pemanggilan kedua, panjang hasil menjadi 1, dan fungsi kembali memanggil dirinya sendiri dua kali:
   - Pertama dengan hasil="00"
   - Kedua dengan hasil="01"
4. Proses ini terus berlanjut hingga panjang hasil mencapai n=3, lalu mencetak semua kombinasi biner yang mungkin.
"""
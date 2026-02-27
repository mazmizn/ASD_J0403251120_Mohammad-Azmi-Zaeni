# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0): 
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti 
    if jumlah_1 > batas: 
        return 
 
    # Base case 
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    # Pilih '0' 
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1' 
  
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) 

biner_batas(4, 2)

"""
Alur:
1. Fungsi biner_batas dipanggil dengan n=4, batas=2, hasil="", dan jumlah_1=0.
2. Karena jumlah_1 (0) tidak melebihi batas (2), fungsi terus berjalan.
3. Karena panjang hasil (0) tidak sama dengan n (4), fungsi memanggil dirinya sendiri dua kali:
   - Pertama dengan hasil="0" dan jumlah_1 tetap 0
   - Kedua dengan hasil="1" dan jumlah_1 menjadi 1
4. Proses ini terus berlanjut hingga panjang hasil mencapai n=4, tetapi hanya mencetak kombinasi yang memiliki jumlah '1' tidak melebihi batas 2.
"""
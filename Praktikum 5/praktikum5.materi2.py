# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ==========================================================

def hitung(n): 
    # Base case 
    if n == 0: 
        print("Selesai") 
        return 
    
    print("Masuk:", n)      # fase stacking
    hitung(n - 1)           # pemanggilan rekursif
    print("Keluar:", n)     # fase unwinding

hitung(3) 

"""
Alur:
1. Fungsi hitung dipanggil dengan n = 3.
2. Karena n tidak sama dengan 0, program mencetak "Masuk: 3" dan memanggil hitung(2).
3. Fungsi hitung dipanggil dengan n = 2.
4. Karena n tidak sama dengan 0, program mencetak "Masuk: 2" dan memanggil hitung(1).
5. Fungsi hitung dipanggil dengan n = 1.
6. Karena n tidak sama dengan 0, program mencetak "Masuk: 1" dan memanggil hitung(0).
7. Fungsi hitung dipanggil dengan n = 0.
8. Karena n sama dengan 0, program mencetak "Selesai" dan kembali ke pemanggilan sebelumnya.
9. Program kembali ke pemanggilan hitung(1), mencetak "Keluar: 1".
10. Program kembali ke pemanggilan hitung(2), mencetak "Keluar: 2".
11. Program kembali ke pemanggilan hitung(3), mencetak "Keluar: 3".
"""
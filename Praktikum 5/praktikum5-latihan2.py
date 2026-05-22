# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n): # Mendefinisikan fungsi rekursif dengan parameter n
    if n == 0: # Base Case (Kondisi Terminal): Titik di mana rekursi harus berhenti
        print("Selasa") # Mencetak pesan akhir saat mencapai kondisi terminal 
        return # Keluar dari fungsi dan memulai fase balik atau unwinding 

    print("Masuk", n) # Fase Winding/Stacking: Mencetak angka sebelum memanggil dirinya sendiri
    countdown(n-1) # Recursive Case: Memanggil fungsi yang sama dengan nilai n yang diperkecil 
    print("Keluar", n) # Fase Unwinding: Dieksekusi saat fungsi kembali dari tumpukan (stack) 

# Pemanggilan awal fungsi untuk memulai rangkaian rekursi
countdown(3) # Memulai proses rekursi dari angka 3 


"""
Mengapa output 'Keluar' muncul terbalik? 
Karena dalam rekursi, setiap pemanggilan fungsi disimpan dalam stack. Ketika fungsi mencapai base case (n == 0), maka proses kembali ke pemanggilan sebelumnya satu per satu. Dalam hal ini, ketika countdown(3) dipanggil, maka countdown(2) dipanggil, lalu countdown(1), dan akhirnya countdown(0). Setelah countdown(0) selesai, maka proses kembali ke countdown(1), lalu countdown(2), dan akhirnya countdown(3). Dengan demikian, output "Keluar" muncul dalam urutan terbalik dari urutan "Masuk".

"""
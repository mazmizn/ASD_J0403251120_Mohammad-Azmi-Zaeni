# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil = ""): # Fungsi pencarian solusi dengan teknik backtracking 

    # Base case (Kondisi Berhenti)
    if len(hasil) == 6: # Berhenti jika panjang string sudah mencapai target (di sini 6)
        print(hasil) # Mencetak satu kombinasi lengkap yang berhasil ditemukan 
        return # Keluar dari fungsi untuk kembali ke langkah sebelumnya atau backtrack [
    
    # Recursive case (Choose + Explore)
    kombinasi(n, hasil + "A") # Pilih 'A' dan lanjut jelajahi kemungkinan karakter berikutnya 
    kombinasi(n, hasil + "B") # Pilih 'B' untuk mencoba jalur lain setelah jalur 'A' selesai

# Pemanggilan awal
kombinasi(2) # Memulai proses (Catatan: variabel 'n' di sini tidak terpakai karena base case dikunci di angka 6)

"""
Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.
Jumlah kombinasi yang dihasilkan adalah 64. Hal ini karena setiap posisi dalam string dapat diisi dengan dua pilihan karakter ('A' atau 'B').
Dengan panjang string 6, jumlah total kombinasi dapat dihitung dengan rumus 2^n, di mana n adalah panjang string. Dalam hal ini, n = 6, sehingga jumlah kombinasi adalah 2^6 = 64
"""


# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Latihan 5: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang: # Base case
        print("PIN:", hasil) #Mencetak PIN yang sudah lengkap
        return # Keluar dari fungsi untuk kembali ke langkah sebelumnya atau backtrack
    
    for angka in ["0", "1", "2"]: #Racursive case: Pilih setiap angka dari 0,1,2 dan lanjutkan membangun PIN
        buat_pin(panjang, hasil + angka) # Memanggil fungsi dengan menambahkan angka yang dipilih ke hasil saat ini
buat_pin(3)

"""
Bagaimana cara mencegah angka yang sama muncul berulang? 
Dengan menambahkan logika : if angka not in hasil
"""
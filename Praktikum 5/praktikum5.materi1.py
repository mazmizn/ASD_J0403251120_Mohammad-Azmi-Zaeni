# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Contoh Rekursi 1: Faktorial
# ==========================================================

def faktorial(n): # Mendefinisikan fungsi faktorial dengan parameter n
    # Base case: berhenti ketika n = 0
    if n == 0:
        return 1
    #Recursive case: masalah diperkecil menjadi faktorial (n-1)
    return n * faktorial(n-1)
print(faktorial(5)) # Output: 120
 

"""
Alur:
1. Fungsi faktorial dipanggil dengan n = 5.
2. Karena n != 0, fungsi mengembalikan 5 * faktorial(4).
3. Fungsi faktorial dipanggil dengan n = 4.
4. Karena n != 0, fungsi mengembalikan 4 * faktorial(3).
5. Fungsi faktorial dipanggil dengan n = 3.
6. Karena n != 0, fungsi mengembalikan 3 * faktorial(2).
7. Fungsi faktorial dipanggil dengan n = 2.
8. Karena n != 0, fungsi mengembalikan 2 * faktorial(1).
9. Fungsi faktorial dipanggil dengan n = 1.
10. Karena n != 0, fungsi mengembalikan 1 * faktorial(0).
11. Fungsi faktorial dipanggil dengan n = 0.
12. Karena n == 0, fungsi mengembalikan nilai 1 (base case).
13. Nilai kembali dihitung: 1 * 1 * 2 * 3 * 4 * 5 = 120.
"""
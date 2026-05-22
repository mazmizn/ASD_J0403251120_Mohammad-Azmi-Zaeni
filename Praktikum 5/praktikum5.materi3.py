# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0): 
    # Base case: jika index sudah mencapai panjang list 
    if index == len(data): 
        return 0 
    # Recursive case: elemen sekarang + jumlah elemen setelahnya 
    return data[index] + jumlah_list(data, index + 1) 

print(jumlah_list([2, 4, 6, 8]))  # Output: 20 

"""
Alur:
1. Fungsi jumlah_list dipanggil dengan data=[2,4,6,8] dan index=0.
2. Karena index != len(data), fungsi mengembalikan 2 + jumlah_list([2,4,6,8], 1).
3. Fungsi jumlah_list dipanggil dengan data=[2,4,6,8] dan index=1.
4. Karena index != len(data), fungsi mengembalikan 4 + jumlah_list([2,4,6,8], 2).
5. Fungsi jumlah_list dipanggil dengan data=[2,4,6,8] dan index=2.
6. Karena index != len(data), fungsi mengembalikan 6 + jumlah_list([2,4,6,8], 3).
7. Fungsi jumlah_list dipanggil dengan data=[2,4,6,8] dan index=3.
8. Karena index == len(data), fungsi mengembalikan 0 (base case).
9. Nilai kembali dihitung: 0 + 8 + 6 + 4 + 2 = 20.
"""
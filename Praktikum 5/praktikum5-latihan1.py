# ========================================================== 
# Nama: Mohammad Azmi Zaeni
# NIM : J0403251120
# Kelas: A
# Latihan 1: Rekursi Pangkat 
# ========================================================== 

def pangkat (a, n): #Mendefiniskan fungsi pangkat, a (bilangan) dan n (pangkat)
    #Base case
    if n == 0: #Jika n (pangkat) = 0, fungsi akan mengembalikan nilai 1
        return 1
    #Recursive case
    else:
        return a *pangkat(a, n-1) #Jika n (pangkat) tidak sama dengan 0, fungsi memanggil dirinya sendiri sampai ke base case.

print(pangkat(2, 4)) # Output: 16

"""
Penjelasan:
Alur program pada fungsi pangkat (a, n), base case, dan recursive call adalah sebagai berikut:
1. Fungsi menerima dua parameter, yaitu a (baris) dan n (pangkat).
2. Fungsi memeriksa apakah n sama dengan 0. Jika ya, maka fungsi mengembalikan nilai 1 (base case).
3. Jika n tidak sama dengan 0, fungsi akan memanggil dirinya sendiri dengan parameter n yang dikurangi 1 (n-1) dan mengalikan hasilnya dengan a (recursive case).
4. Proses ini akan terus berulang hingga n mencapai 0, pada saat itu fungsi akan mulai mengembalikan nilai dan menghitung hasil akhir dari a pangkat n.

Base case: Ketika n sama dengan 0, fungsi mengembalikan nilai 1. Ini karena setiap bilangan pangkat 0 adalah 1.
Recursive case: Ketika n tidak sama dengan 0, fungsi memanggil dirinya sendiri dengan n yang dikurangi 1 dan mengalikan hasilnya dengan a. Ini memungkinkan fungsi untuk menghitung a pangkat n secara bertahap hingga mencapai base case.
"""
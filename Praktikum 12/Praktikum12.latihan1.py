# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

#Jawaban Analisis:
'''
1. Total bobot jalur **A -> B -> D** adalah:

   * A → B = 4
   * B → D = 5
   * Total = **9**

2. Total bobot jalur **A -> C -> D** adalah:

   * A → C = 2
   * C → D = 1
   * Total = **3**

3. Jalur yang dipilih sebagai jalur terpendek adalah:
   **A -> C -> D**
   karena memiliki total bobot lebih kecil, yaitu **3**.

4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena setiap edge memiliki bobot yang berbeda.
   Sebuah jalur dengan edge lebih banyak bisa saja memiliki total bobot lebih kecil dibanding jalur dengan edge lebih sedikit.

   Contoh pada kode:

   * Jalur A → B → D memiliki total bobot 9
   * Jalur A → C → D memiliki total bobot 3

   Walaupun kedua jalur memiliki jumlah edge yang sama, yang menentukan jalur terpendek adalah **total bobot**, bukan banyaknya edge.
'''
# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : A
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# LATIHAN 2: Implementasi Algoritma Kruskal
# ==========================================================
# Tujuan: Menjalankan algoritma Kruskal untuk mencari MST
#         dan memahami urutan pemilihan edge berdasarkan bobot
# ==========================================================

#  Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] 
total_weight = 0 
connected = set() 

for weight, u, v in edges: 
    # Memilih edge yang tidak membentuk cycle sederhana 
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 
        connected.add(u) 
        connected.add(v) 

print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight)


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================
 
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1. Ini adalah edge dengan bobot
#    paling kecil dari seluruh daftar edge sehingga dipilih
#    pertama oleh algoritma Kruskal.
 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena tujuan MST adalah mendapatkan total bobot MINIMUM.
#    Dengan selalu memilih edge terkecil terlebih dahulu (greedy),
#    kita memastikan bahwa setiap penambahan edge ke MST memberikan
#    kontribusi biaya sekecil mungkin. Ini adalah strategi
#    "greedy" (serakah tapi pintar) yang terbukti menghasilkan MST.
 
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 1 + 2 + 3 = 6
#    (C-D=1) + (A-C=2) + (B-D=3) = 6
 
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (bobot 4) tidak dipilih karena ketika giliran A-B
#    diproses, KEDUA node A dan B sudah berada dalam MST.
#    Menambahkan A-B akan membentuk cycle: A-C-D-B-A.
#    Edge A-D (bobot 5) juga tidak dipilih karena A dan D
#    sudah terhubung (lewat A-C-D), menambahkannya akan cycle.
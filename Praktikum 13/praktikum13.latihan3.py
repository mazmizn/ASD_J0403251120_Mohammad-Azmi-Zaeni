# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : A
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# LATIHAN 3: Implementasi Algoritma Prim
# ==========================================================
# Tujuan: Menjalankan algoritma Prim untuk mencari MST
#         dan memahami cara kerja Prim yang bertahap dari node awal
# ==========================================================


import heapq 

graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start): 
    visited = set([start]) 
    edges = [] 
    
    # Memasukkan semua edge dari node awal ke dalam heap
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
        
    mst = [] 
    total_weight = 0 
    
    while edges: 
        weight, u, v = heapq.heappop(edges) 
        
        if v not in visited: 
            visited.add(v) 

            mst.append((u, v, weight)) 
            total_weight += weight 
            
            # Memasukkan edge dari tetangga baru ke dalam heap
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
                    
    return mst, total_weight 

# Menjalankan fungsi
mst, total = prim(graph, 'A') 

print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 
    
print("Total bobot =", total)


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================
 
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A'. Node ini bisa diganti
#    ke node mana saja - hasilnya tetap MST dengan total bobot
#    yang sama, meski urutan edge yang dipilih bisa berbeda.
 
# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2. Dari node A, ada 3 kandidat:
#    A-B(4), A-C(2), A-D(5). Yang terkecil adalah A-C(2),
#    maka Prim memilih A-C sebagai edge pertama.
 
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menggunakan priority queue (min-heap) untuk selalu
#    mengambil edge dengan bobot TERKECIL dari semua edge yang
#    menghubungkan node yang SUDAH dikunjungi ke node yang
#    BELUM dikunjungi. Setiap kali node baru ditambahkan,
#    semua edge dari node baru tersebut dimasukkan ke kandidat.
 
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 2 + 1 + 3 = 6
#    (A-C=2) + (C-D=1) + (D-B=3) = 6
 
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - PRIM: Bekerja berbasis NODE. Mulai dari 1 node, lalu
#      memperluas area ke tetangga terdekat. Seperti "api menyebar"
#      dari satu titik. Cocok untuk DENSE GRAPH (banyak edge).
#
#    - KRUSKAL: Bekerja berbasis EDGE. Mengurutkan semua edge
#      secara global dari terkecil ke terbesar, lalu memilih
#      satu per satu. Tidak peduli posisi node. Cocok untuk
#      SPARSE GRAPH (sedikit edge).
#
#    Keduanya menghasilkan total bobot MST yang SAMA!
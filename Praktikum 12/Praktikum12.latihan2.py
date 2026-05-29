# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    # Selama masih ada node dalam priority queue
    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan jarak baru ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma Dijkstra dari node A
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


#Jawaban Analisis:
'''
1. Jarak terpendek dari A ke B adalah: 4
2. Jarak terpendek dari A ke C adalah: 2
3. Jarak terpendek dari A ke D adalah: 3 melalui jalur A -> C -> D
4. Jarak A ke D lebih kecil melalui C dibandingkan melalui B karena:
Jalur A → B → D = 4 + 5 = 9
Jalur A → C → D = 2 + 1 = 3
Total bobot melalui C lebih kecil, sehingga dipilih sebagai jalur terpendek.

5. Fungsi priority_queue dalam algoritma Dijkstra adalah:
Untuk menyimpan node berdasarkan jarak terkecil yang akan diproses terlebih dahulu.
Dengan begitu, algoritma dapat bekerja lebih efisien dalam mencari jalur terpendek.

6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena:
Algoritma Dijkstra mengasumsikan bahwa jarak terpendek yang sudah dipilih tidak akan berubah lagi.
Pada graph berbobot negatif, bisa muncul jalur baru dengan total jarak lebih kecil setelah proses selesai, sehingga hasil Dijkstra bisa menjadi salah.
'''
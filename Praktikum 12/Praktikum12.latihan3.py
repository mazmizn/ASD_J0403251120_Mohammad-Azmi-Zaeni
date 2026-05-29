# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if (
                    distances[node] != float('inf')
                    and distances[node] + weight < distances[neighbor]
                ):
                    distances[neighbor] = distances[node] + weight

    return distances


# Menjalankan algoritma Bellman-Ford dari node A
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung dari A ke B adalah 5.

# 2. Berapa total bobot jalur A -> C -> B?
#    A -> C = 4
#    C -> B = -2
#    Total bobot = 4 + (-2) = 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A -> C -> B menghasilkan jarak lebih kecil,
#    karena total bobotnya 2, sedangkan jalur langsung A -> B memiliki bobot 5.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Karena Bellman-Ford memeriksa dan memperbarui jarak
#    secara berulang melalui proses relaksasi edge,
#    sehingga tetap dapat menemukan jarak terpendek
#    meskipun terdapat bobot negatif.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi edge adalah proses memeriksa apakah
#    suatu jalur baru menghasilkan jarak yang lebih kecil.
#    Jika lebih kecil, maka nilai jarak diperbarui.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    - Bellman-Ford dapat menangani bobot negatif,
#      sedangkan Dijkstra tidak.
#    - Dijkstra lebih cepat dibanding Bellman-Ford
#      pada graph dengan bobot positif.
#    - Bellman-Ford menggunakan relaksasi semua edge
#      sebanyak (jumlah node - 1) kali.
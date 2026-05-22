# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Program Mencari Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# ----------------------------------------------------------
# Representasi weighted graph menggunakan dictionary
# Bobot menunjukkan jarak antar kota
# ----------------------------------------------------------
graph = {
    'Bogor': {
        'Jakarta': 5,
        'Depok': 2
    },

    'Depok': {
        'Jakarta': 2,
        'Bandung': 6
    },

    'Jakarta': {
        'Bandung': 7
    },

    'Bandung': {}
}


# ----------------------------------------------------------
# Fungsi Dijkstra
# Untuk mencari jarak terpendek dari node awal
# ke seluruh node lainnya
# ----------------------------------------------------------
def dijkstra(graph, start):

    # Membuat semua jarak awal menjadi tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan:
    # (jarak, node)
    priority_queue = [(0, start)]

    # Proses selama queue masih memiliki isi
    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari data tersimpan,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil,
            # maka update jaraknya
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                # Masukkan data baru ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ----------------------------------------------------------
# Menentukan node awal
# ----------------------------------------------------------
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)


# ----------------------------------------------------------
# Menampilkan hasil jarak terpendek
# ----------------------------------------------------------
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah Bogor.

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Node dengan jarak paling kecil adalah Bogor sendiri
#    dengan jarak 0.
#
#    Jika selain node awal:
#    Depok memiliki jarak paling kecil yaitu 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Bandung memiliki jarak paling besar yaitu 8.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Algoritma Dijkstra bekerja dengan memilih node
#    yang memiliki jarak paling kecil terlebih dahulu,
#    kemudian memperbarui jarak ke node tetangganya.
#
#    Pada kasus ini:
#    - Dari Bogor, algoritma memeriksa Jakarta dan Depok.
#    - Jalur ke Depok lebih kecil yaitu 2.
#    - Dari Depok ditemukan jalur lebih pendek ke Jakarta:
#      Bogor -> Depok -> Jakarta = 4
#      dibanding jalur langsung Bogor -> Jakarta = 5.
#    - Dari Depok juga ditemukan jalur ke Bandung:
#      Bogor -> Depok -> Bandung = 8.
#
#    Dengan proses tersebut, algoritma berhasil
#    menemukan jalur terpendek ke semua kota.
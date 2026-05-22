# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue untuk menyimpan node yang akan diproses
    priority_queue = [(0, start)]

    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari data yang tersimpan, lewati
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma Dijkstra dari Gerbang
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Lokasi yang paling dekat dari Gerbang adalah Kantin
#    dengan waktu tempuh 2 menit.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jalur tercepat:
#    Gerbang -> Kantin -> Lab -> Aula
#    Total waktu:
#    2 + 4 + 1 = 7 menit

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu.
#    Jalur tidak langsung bisa memiliki total bobot
#    yang lebih kecil dibanding jalur langsung.
#    Pada kasus ini:
#    - Gerbang -> Kantin -> Aula = 2 + 7 = 9 menit
#    - Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit
#    Jalur melalui Lab lebih cepat.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Karena semua bobot pada graph bernilai positif
#    dan Dijkstra sangat efisien untuk mencari
#    jalur tercepat pada graph berbobot positif,
#    seperti waktu tempuh antar lokasi kampus.
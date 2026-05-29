def bellman_ford(graph, start):
    # Membuat dictionary untuk menyimpan jarak terpendek
    # dari titik awal ke setiap node.
    # Awalnya semua jarak diatur tak hingga (infinity).
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Proses relaksasi dilakukan sebanyak (jumlah node - 1) kali
    # karena pada algoritma Bellman-Ford, jarak terpendek
    # maksimal melewati sebanyak (V - 1) sisi.
    for _ in range(len(graph) - 1):

        # Menelusuri setiap node pada graph
        for node in graph:

            # Menelusuri semua tetangga (neighbor)
            # beserta bobot jalurnya
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini ditambah bobot edge
                # lebih kecil daripada jarak yang tersimpan
                # ke neighbor, maka update jaraknya.
                if distances[node] + weight < distances[neighbor]:

                    # Memperbarui jarak terpendek ke neighbor
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil jarak terpendek dari node awal
    return distances
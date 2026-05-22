#Nama: Mohammad Azmi Zaeni
#NIM: J0403251120
#Kelas: TPL A1
#==============================

# Fungsi menerima matrix sebagai input, bukan edges
def createGraph(matrix):

    # Buat adjacency list sebanyak jumlah baris matrix
    adj = [[] for _ in range(len(matrix))]

    # Loop setiap baris (vertex asal)
    for i in range(len(matrix)):

        # Loop setiap kolom (vertex tujuan)
        for j in range(len(matrix[i])):

            # Kalau nilainya 1, berarti ada edge dari i ke j
            if matrix[i][j] == 1:
                adj[i].append(j)

    return adj

if __name__ == "__main__":

    # Matrix sebagai input utama
    matrix = [
        [0,1,1,0],
        [1,0,1,0],
        [1,1,0,1],
        [0,0,1,0]
    ]

    # Build the graph dari matrix
    adj = createGraph(matrix)

    print("Adjacency List Representation:")
    for i in range(len(adj)):

        # Print vertex
        print(f"{i}:", end=" ")
        for j in adj[i]:

            # Print tetangganya
            print(j, end=" ")
        print()
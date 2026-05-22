#Nama: Mohammad Azmi Zaeni
#NIM: J0403251120
#Kelas: TPL A1
#==============================

# Praktikum 4 - Studi Kasus Dunia Nyata
# Studi Kasus: Media Sosial (Directed Graph)
# Digit akhir NIM: 0 → Media Sosial

# ── LANGKAH 1 & 2: Node dan Edge ──────────────────────────────
# Node  : user media sosial
# Edge  : hubungan follow (satu arah / directed)
#
# Desain graph:
#   Yusuf  → Adit, Hanif, Haidar
#   Adit   → Yusuf, Pakdeh
#   Hanif  → Yusuf, Haidar
#   Haidar → Pakdeh
#   Pakdeh → Yusuf, Adit
# ──────────────────────────────────────────────────────────────

# ── LANGKAH 4A: Adjacency List ────────────────────────────────
def createAdjList(edges):
    # Inisialisasi dictionary dengan semua node
    adj = {
        "Yusuf":  [],
        "Adit":   [],
        "Hanif":  [],
        "Haidar": [],
        "Pakdeh": []
    }

    # Tambahkan setiap edge ke adjacency list
    # Directed: hanya satu arah (u → v), tidak perlu adj[v].append(u)
    for u, v in edges:
        adj[u].append(v)

    return adj

# ── LANGKAH 4B: Adjacency Matrix ──────────────────────────────
def createAdjMatrix(nodes, edges):
    n = len(nodes)

    # Buat matrix n x n berisi 0 semua
    matrix = [[0] * n for _ in range(n)]

    # Buat mapping nama → index
    index = {node: i for i, node in enumerate(nodes)}

    # Isi matrix: jika ada edge u → v, set matrix[u][v] = 1
    for u, v in edges:
        matrix[index[u]][index[v]] = 1

    return matrix

# ── MAIN ───────────────────────────────────────────────────────
if __name__ == "__main__":

    # Daftar node
    nodes = ["Yusuf", "Adit", "Hanif", "Haidar", "Pakdeh"]

    # Daftar edge (directed: u → v)
    edges = [
        ("Yusuf",  "Adit"),
        ("Yusuf",  "Hanif"),
        ("Yusuf",  "Haidar"),
        ("Adit",   "Yusuf"),
        ("Adit",   "Pakdeh"),
        ("Hanif",  "Yusuf"),
        ("Hanif",  "Haidar"),
        ("Haidar", "Pakdeh"),
        ("Pakdeh", "Yusuf"),
        ("Pakdeh", "Adit"),
    ]

    # ── Tampilkan Adjacency List ───────────────────────────────
    adj = createAdjList(edges)

    print("=" * 40)
    print("   ADJACENCY LIST - Media Sosial")
    print("=" * 40)
    for user, following in adj.items():
        print(f"{user} → {following}")

    # ── Tampilkan Adjacency Matrix ─────────────────────────────
    matrix = createAdjMatrix(nodes, edges)

    print()
    print("=" * 40)
    print("   ADJACENCY MATRIX - Media Sosial")
    print("=" * 40)

    # Header kolom
    print(f"{'':>8}", end="")
    for node in nodes:
        print(f"{node:>8}", end="")
    print()

    # Baris matrix
    for i, node in enumerate(nodes):
        print(f"{node:>8}", end="")
        for j in range(len(nodes)):
            print(f"{matrix[i][j]:>8}", end="")
        print()

    # ── Tampilkan Hubungan Antar Node ──────────────────────────
    print()
    print("=" * 40)
    print("   HUBUNGAN ANTAR NODE")
    print("=" * 40)
    for u, v in edges:
        print(f"  {u} mengikuti {v}")
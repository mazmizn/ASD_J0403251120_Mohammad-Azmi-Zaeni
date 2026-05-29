# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : A
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# LATIHAN 1: Memahami Konsep Spanning Tree
# ==========================================================
# Tujuan: Menampilkan edge graph, spanning tree yang valid,
#         jumlah edge graph awal, dan jumlah edge spanning tree.
# Graph yang digunakan memiliki 4 node: A, B, C, D
# ==========================================================

# Daftar semua edge pada graph awal (belum ada bobot, hanya koneksi)
edges = [
    ('A', 'B'),  # A terhubung ke B
    ('A', 'C'),  # A terhubung ke C
    ('A', 'D'),  # A terhubung ke D (edge diagonal)
    ('C', 'D'),  # C terhubung ke D
    ('B', 'D'),  # B terhubung ke D
]

# Contoh spanning tree yang valid dari graph di atas
# Dipilih agar semua node terhubung tanpa membentuk siklus
spanning_tree = [
    ('A', 'B'),  # Menghubungkan A ke B
    ('A', 'C'),  # Menghubungkan A ke C
    ('C', 'D'),  # Menghubungkan C ke D
]

# Menampilkan semua edge pada graph awal
print("=" * 40)
print("       GRAPH AWAL")
print("=" * 40)
print("Edge pada graph:")
for edge in edges:
    print(f"  {edge[0]} -- {edge[1]}")

# Menampilkan spanning tree yang valid
print("\n" + "=" * 40)
print("       SPANNING TREE")
print("=" * 40)
print("Contoh spanning tree yang valid:")
for edge in spanning_tree:
    print(f"  {edge[0]} -- {edge[1]}")

# Menampilkan jumlah edge
print("\n" + "=" * 40)
print("       STATISTIK")
print("=" * 40)
print(f"Jumlah node            : 4 (A, B, C, D)")
print(f"Jumlah edge graph awal : {len(edges)}")
print(f"Jumlah edge spanning tree : {len(spanning_tree)}")
print(f"Rumus edge ST = node - 1 = 4 - 1 = {4 - 1}")

# Validasi: apakah jumlah edge spanning tree = node - 1
nodes = {'A', 'B', 'C', 'D'}
expected_edges = len(nodes) - 1
print(f"\nValidasi: {len(spanning_tree)} == {expected_edges} ? {len(spanning_tree) == expected_edges}")


# ==========================================================
# JAWABAN ANALISIS
# ==========================================================

# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki LEBIH BANYAK edge (5 edge) dan
#    mengandung cycle (siklus/lingkaran). Contohnya, A-B-D-A
#    membentuk lingkaran. Sedangkan spanning tree hanya memiliki
#    3 edge (N-1 = 4-1 = 3), menghubungkan semua node tanpa
#    membentuk siklus sama sekali.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena cycle berarti ada edge yang BERLEBIHAN dan tidak perlu.
#    Misalnya jika A sudah terhubung ke B lewat C-D, maka edge
#    langsung A-B menjadi sia-sia dan hanya menambah biaya.
#    Dalam dunia nyata: bayangkan jaringan kabel - kabel yang
#    membentuk lingkaran tidak menambah koneksi baru, hanya
#    membuang biaya.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya memakai tepat N-1 edge untuk
#    menghubungkan N node. Ini adalah jumlah MINIMUM edge yang
#    dibutuhkan agar semua node terhubung. Lebih sedikit dari N-1
#    berarti ada node yang terputus. Lebih banyak dari N-1
#    berarti pasti ada cycle.
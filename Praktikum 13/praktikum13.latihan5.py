# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : A
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# LATIHAN 5: Tugas Mandiri - MST dengan Kasus Baru
# ==========================================================
# Kasus yang dipilih: KASUS 2 - Jaringan Komputer
#
# Deskripsi: Sebuah jaringan komputer terdiri dari beberapa
#            router yang perlu saling terhubung dengan biaya
#            kabel/koneksi minimum.
#
# Data koneksi antar router:
#   RouterA - RouterB = 3
#   RouterA - RouterC = 2
#   RouterB - RouterD = 5
#   RouterC - RouterD = 1
#   RouterB - RouterC = 4
#
# Algoritma: PRIM (dipilih karena ingin mencoba kedua algoritma)
# ==========================================================
 
import heapq  # library untuk priority queue
 
# ==========================================================
# REPRESENTASI WEIGHTED GRAPH
# Format adjacency dict: {router: {tetangga: biaya_koneksi}}
# ==========================================================
graph_router = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1},
}
 
# ==========================================================
# IMPLEMENTASI ALGORITMA PRIM
# ==========================================================
def prim_jaringan(graph, start):
    """
    Fungsi Prim untuk mencari MST jaringan komputer.
    Parameter:
        graph : dict - representasi weighted graph router
        start : str  - router awal yang dijadikan titik mulai
    Return:
        mst          - daftar koneksi dalam MST
        total_biaya  - total biaya koneksi minimum
    """
    visited = set([start])     # router yang sudah masuk MST
    candidates = []            # priority queue kandidat koneksi
    mst = []                   # hasil MST
    total_biaya = 0            # total biaya
 
    # Masukkan semua koneksi dari router awal ke priority queue
    for tetangga, biaya in graph[start].items():
        heapq.heappush(candidates, (biaya, start, tetangga))
 
    print(f"  Node awal: {start}")
    print(f"  Kandidat awal: {[(b, u, v) for b, u, v in candidates]}\n")
 
    step = 1
    while candidates:
        # Ambil koneksi dengan biaya terkecil
        biaya, router_asal, router_tujuan = heapq.heappop(candidates)
 
        # Jika router tujuan belum dikunjungi
        if router_tujuan not in visited:
            visited.add(router_tujuan)
            mst.append((router_asal, router_tujuan, biaya))
            total_biaya += biaya
 
            print(f"  Langkah {step}: PILIH {router_asal} → {router_tujuan} (biaya: {biaya})")
            print(f"             Router aktif: {sorted(visited)}")
            step += 1
 
            # Tambah koneksi-koneksi baru dari router yang baru bergabung
            for tetangga, b in graph[router_tujuan].items():
                if tetangga not in visited:
                    heapq.heappush(candidates, (b, router_tujuan, tetangga))
        else:
            print(f"             LEWATI {router_asal} → {router_tujuan} (sudah terhubung)")
 
    return mst, total_biaya
 
 
# ==========================================================
# JUGA IMPLEMENTASI KRUSKAL SEBAGAI PERBANDINGAN
# ==========================================================
def kruskal_jaringan(edges):
    """
    Fungsi Kruskal sebagai pembanding hasil Prim.
    """
    edges_sorted = sorted(edges)
    mst = []
    total = 0
    connected = set()
 
    for biaya, u, v in edges_sorted:
        if u not in connected or v not in connected:
            mst.append((u, v, biaya))
            total += biaya
            connected.add(u)
            connected.add(v)
 
    return mst, total
 
 
# ==========================================================
# MENJALANKAN PROGRAM
# ==========================================================
print("=" * 55)
print("    JARINGAN KOMPUTER - KONEKSI ROUTER MINIMUM")
print("=" * 55)
print("\nData koneksi yang tersedia:")
print(f"  {'Koneksi':<30} {'Biaya':>6}")
print("  " + "-" * 36)
koneksi_list = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC'),
]
for b, u, v in sorted(koneksi_list):
    print(f"  {u+' ↔ '+v:<30} {b:>6}")
 
# --- Jalankan Prim ---
print("\n" + "=" * 55)
print("  [ALGORITMA PRIM] - mulai dari RouterA")
print("=" * 55)
mst_prim, total_prim = prim_jaringan(graph_router, 'RouterA')
 
print("\nHasil MST dengan Prim:")
for u, v, b in mst_prim:
    print(f"  ✓ {u} ↔ {v}  biaya: {b}")
print(f"  Total biaya = {total_prim}")
 
# --- Jalankan Kruskal sebagai verifikasi ---
print("\n" + "=" * 55)
print("  [ALGORITMA KRUSKAL] - verifikasi hasil")
print("=" * 55)
mst_kruskal, total_kruskal = kruskal_jaringan(koneksi_list)
 
print("Hasil MST dengan Kruskal:")
for u, v, b in mst_kruskal:
    print(f"  ✓ {u} ↔ {v}  biaya: {b}")
print(f"  Total biaya = {total_kruskal}")
 
# --- Kesimpulan ---
print("\n" + "=" * 55)
print("  KESIMPULAN")
print("=" * 55)
print(f"  Total bobot Prim    : {total_prim}")
print(f"  Total bobot Kruskal : {total_kruskal}")
print(f"  Sama hasilnya? {'YA ✓' if total_prim == total_kruskal else 'TIDAK ✗'}")
print(f"\n  Dengan biaya minimum Rp {total_prim}, semua router")
print(f"  sudah terhubung dalam satu jaringan!")
 
 
# ==========================================================
# JAWABAN ANALISIS
# ==========================================================
 
# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer - menghubungkan 4 router
#    (RouterA, RouterB, RouterC, RouterD) dengan biaya
#    koneksi kabel minimum.
 
# 2. Algoritma apa yang digunakan?
#    PRIM sebagai algoritma utama, dan KRUSKAL sebagai
#    verifikasi. Keduanya dijalankan untuk membuktikan bahwa
#    total bobot MST yang dihasilkan SAMA meski caranya beda.
 
# 3. Edge mana saja yang dipilih dalam MST?
#    - RouterA ↔ RouterC : biaya 2  (terkecil dari RouterA)
#    - RouterC ↔ RouterD : biaya 1  (terkecil dari C atau D)
#    - RouterA ↔ RouterB : biaya 3  (menghubungkan B ke jaringan)
#    Total: 3 koneksi = 4 router - 1 ✓
 
# 4. Berapa total bobot MST?
#    Total bobot = 2 + 1 + 3 = 6
#    Ini adalah biaya MINIMUM untuk menghubungkan semua router.
 
# 5. Mengapa edge tertentu tidak dipilih?
#    - RouterB ↔ RouterC (biaya 4): Tidak dipilih karena
#      ketika diproses, RouterB dan RouterC sudah terhubung
#      lewat jalur RouterA-RouterC. Menambahkannya hanya
#      membuat cycle.
#    - RouterB ↔ RouterD (biaya 5): Tidak dipilih karena
#      RouterB dan RouterD sudah terhubung lewat jalur
#      RouterA-RouterC-RouterD. Edge ini paling mahal pula.
#
# Kesimpulan tambahan:
#    MST sangat relevan untuk kasus jaringan komputer karena
#    administrator jaringan perlu menghubungkan semua router
#    dengan kabel fisik seminimal mungkin untuk menghemat
#    biaya infrastruktur tanpa mengorbankan konektivitas.
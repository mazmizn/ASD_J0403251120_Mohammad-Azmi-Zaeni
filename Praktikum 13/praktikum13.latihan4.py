# Nama  : Mohammad Azmi Zaeni
# NIM   : J0403251120
# Kelas : A
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# LATIHAN 4: Studi Kasus - Jaringan Kabel Antar Gedung
# ==========================================================
# Deskripsi: Sebuah kampus ingin membangun jaringan internet
#            antar gedung dengan biaya minimum.
#
# Data hubungan antar gedung dan biaya kabelnya:
#   GedungA - GedungB = 4 (juta rupiah)
#   GedungA - GedungC = 2
#   GedungB - GedungD = 3
#   GedungC - GedungD = 1
#   GedungA - GedungD = 5
#
# Algoritma yang digunakan: KRUSKAL
# Alasan: Data tersedia dalam bentuk daftar edge (sparse graph)
# ==========================================================
 
# Representasi weighted graph dalam bentuk daftar edge
# Format: (biaya, gedung_asal, gedung_tujuan)
edges_gedung = [
    (4, 'GedungA', 'GedungB'),  # Kabel A-B biaya 4 juta
    (2, 'GedungA', 'GedungC'),  # Kabel A-C biaya 2 juta
    (3, 'GedungB', 'GedungD'),  # Kabel B-D biaya 3 juta
    (1, 'GedungC', 'GedungD'),  # Kabel C-D biaya 1 juta
    (5, 'GedungA', 'GedungD'),  # Kabel A-D biaya 5 juta
]
 
# ==========================================================
# IMPLEMENTASI ALGORITMA KRUSKAL
# ==========================================================
 
def kruskal(edges):
    """
    Fungsi Kruskal untuk mencari Minimum Spanning Tree.
    Parameter:
        edges : list - daftar edge (bobot, node1, node2)
    Return:
        mst          - edge-edge dalam MST
        total_weight - total biaya minimum
    """
    # Langkah 1: Urutkan edge dari biaya terkecil
    edges_sorted = sorted(edges)
 
    mst = []           # daftar edge yang masuk MST
    total_weight = 0   # total biaya minimum
    connected = set()  # gedung yang sudah terhubung
 
    print("Urutan koneksi setelah diurutkan berdasarkan biaya:")
    print(f"{'No':<4} {'Koneksi':<30} {'Biaya':>8}")
    print("-" * 45)
    for i, (w, u, v) in enumerate(edges_sorted, 1):
        print(f"{i:<4} {u+' - '+v:<30} {w:>5} juta")
 
    print("\nProses pemilihan kabel (Algoritma Kruskal):")
    print("-" * 55)
 
    for biaya, gedung1, gedung2 in edges_sorted:
        # Cek apakah penambahan kabel ini aman (tidak cycle)
        if gedung1 not in connected or gedung2 not in connected:
            mst.append((gedung1, gedung2, biaya))
            total_weight += biaya
            connected.add(gedung1)
            connected.add(gedung2)
            print(f"  ✓ PASANG kabel {gedung1} ↔ {gedung2} (Rp {biaya} juta)")
            print(f"    Gedung terhubung: {sorted(connected)}")
        else:
            print(f"  ✗ SKIP   kabel {gedung1} ↔ {gedung2} → sudah terhubung semua")
 
    return mst, total_weight
 
 
# Jalankan Kruskal
print("=" * 55)
print("   SISTEM JARINGAN KABEL KAMPUS - BIAYA MINIMUM")
print("=" * 55)
print(f"\nTotal gedung: 4 (A, B, C, D)")
print(f"Total opsi koneksi: {len(edges_gedung)}\n")
 
mst_result, total_biaya = kruskal(edges_gedung)
 
# Tampilkan hasil akhir
print("\n" + "=" * 55)
print("   HASIL: JARINGAN KABEL OPTIMAL (MST)")
print("=" * 55)
print("\nKabel yang harus dipasang:")
for i, (g1, g2, biaya) in enumerate(mst_result, 1):
    print(f"  {i}. {g1} ↔ {g2}  →  Rp {biaya} juta")
 
print(f"\n{'='*40}")
print(f"  TOTAL BIAYA MINIMUM : Rp {total_biaya} juta")
print(f"{'='*40}")
print(f"\nDengan anggaran Rp {total_biaya} juta, SEMUA gedung")
print(f"sudah terhubung internet tanpa pemborosan!")
 
 
# ==========================================================
# JAWABAN ANALISIS
# ==========================================================
 
# 1. Algoritma apa yang digunakan?
#    Algoritma KRUSKAL. Dipilih karena data sudah tersedia
#    dalam bentuk daftar edge (hubungan antar gedung beserta
#    biayanya), sehingga Kruskal lebih natural dan efisien
#    digunakan. Graph ini juga termasuk sparse graph (sedikit
#    koneksi relatif terhadap jumlah gedung).
 
# 2. Edge mana saja yang dipilih?
#    - GedungC ↔ GedungD : Rp 1 juta  (biaya terkecil)
#    - GedungA ↔ GedungC : Rp 2 juta  (biaya terkecil berikutnya)
#    - GedungB ↔ GedungD : Rp 3 juta  (menghubungkan B ke jaringan)
#    Total: 3 edge = 4 gedung - 1 ✓
 
# 3. Berapa total biaya minimum?
#    Total biaya = 1 + 2 + 3 = Rp 6 juta
#    Ini adalah biaya MINIMUM yang diperlukan untuk
#    menghubungkan semua 4 gedung.
 
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST sangat cocok untuk kasus ini karena:
#    a) Tujuannya adalah menghubungkan SEMUA gedung (bukan
#       hanya sebagian) - ini sesuai sifat spanning tree.
#    b) Kita ingin biaya MINIMUM - ini sesuai sifat MST.
#    c) Tidak perlu ada koneksi redundant (cycle) karena
#       koneksi berlebih hanya membuang biaya tanpa manfaat.
#    d) Analogi nyata: seperti memasang kabel listrik atau
#       pipa air - lebih hemat tanpa lingkaran berlebih.
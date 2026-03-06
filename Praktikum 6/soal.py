def quickSort(data):
    quickSortHelper(data, 0, len(data) - 1)

def quickSortHelper(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)
        quickSortHelper(data, first, splitpoint - 1)
        quickSortHelper(data, splitpoint + 1, last)

def partition(data, first, last):
    pivotvalue = data[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        # Mencari nilai yang LEBIH KECIL dari pivot untuk pindah ke kanan (Descending)
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        # Mencari nilai yang LEBIH BESAR dari pivot untuk pindah ke kiri (Descending)
        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            data[leftmark], data[rightmark] = data[rightmark], data[leftmark]

    data[first], data[rightmark] = data[rightmark], data[first]
    return rightmark

# Data dari soal
skor_pelamar = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Eksekusi Quick Sort
quickSort(skor_pelamar)

print("Hasil pengurutan descending:", skor_pelamar)
print("-" * 30)
print("1. Skor 5 kandidat tertinggi (dari tinggi ke rendah):", skor_pelamar[:5])
print("2. Skor kandidat yang lolos:", skor_pelamar[:5])
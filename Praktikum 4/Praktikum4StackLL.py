#===============================================================
#Nama   : Mohammad Azmi Zaeni
#NIM    : J0403251120
#Kelas  : A1
#===============================================================

#===============================================================
#Implementasi Dasar : Stack
#===============================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada List
        self.next = None #pointer ini merujuk ke node berikutnya (awal=none)

#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top merujuk ke node paling atas (awalnya kosong)
    
    def is_empty(self):
        return self.top is None #mengembalikan true jika stack kosong (top = none)

    def push(self, data):
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru


    def pop(self): #mengambil/menghapus node paling atas (top/head)

        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        def_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next #geser top ke node berikutnya (top lama dihapus)
        return def_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            print("Stack kosong, tidak bisa peek")
            return None
        return self.top.data


    def tampilkan(self):
        #Top -> A -> B -> C -> None
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
print("\nPeek (Lihat Top):", s.peek())
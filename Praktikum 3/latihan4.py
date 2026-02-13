
# Kelas Node merepresentasikan satu simpul pada linked list
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data
        self.next = None  # Menyimpan referensi ke node berikutnya



# Kelas LinkedList untuk mengelola operasi pada linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Head menunjuk ke node pertama

    # Menambahkan node baru di akhir linked list
    def insert_at_end(self, data):
        new_node = Node(data)  # Membuat node baru
        if not self.head:
            self.head = new_node  # Jika list kosong, node baru jadi head
            return
        
        temp = self.head
        while temp.next:  # Menelusuri hingga node terakhir
            temp = temp.next
        temp.next = new_node  # Menyambungkan node baru di akhir

    # Menggabungkan linked list lain ke akhir linked list ini
    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head  # Jika list pertama kosong, langsung ambil list kedua
            return
        
        temp = self.head
        while temp.next:  # Menelusuri hingga node terakhir
            temp = temp.next

        temp.next = other_list.head  # Menyambungkan list kedua di akhir list pertama


    # Menampilkan seluruh isi linked list
    def display(self):
        if not self.head:
            print("kosong")  # Jika list kosong
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")  # Menampilkan data node
            temp = temp.next
        print("null")  # Penanda akhir linked list



# Fungsi untuk membuat linked list dari input user
def buat_linked_list_dari_input(pesan):
    ll = LinkedList()
    data = input(pesan)  # Input data dari user (dipisah spasi)

    if data.strip() == "":  # Jika input kosong, kembalikan linked list kosong
        return ll

    angka = data.split()  # Memisahkan input menjadi list string angka

    for x in angka:
        ll.insert_at_end(int(x))  # Menambah setiap angka ke linked list

    return ll



# Contoh penggunaan: Membuat dan menggabungkan dua linked list
ll1 = buat_linked_list_dari_input("Masukkan elemen untuk Linked List 1: ")  # Input list 1
ll2 = buat_linked_list_dari_input("Masukkan elemen untuk Linked List 2: ")  # Input list 2

print("\nLinked List 1:")
ll1.display()  # Tampilkan list 1

print("Linked List 2:")
ll2.display()  # Tampilkan list 2

ll1.merge(ll2)  # Gabungkan list 2 ke list 1

print("\nLinked List setelah digabungkan:")
ll1.display()  # Tampilkan hasil penggabungan

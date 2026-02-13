
# Kelas Node merepresentasikan satu simpul pada circular linked list
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data
        self.next = None  # Menyimpan referensi ke node berikutnya



# Kelas CircularSinglyLinkedList untuk mengelola circular singly linked list
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None  # Head menunjuk ke node pertama
        self.tail = None  # Tail menunjuk ke node terakhir

    # Menambahkan node baru di akhir circular linked list
    def insert_at_end(self, data):
        new_node = Node(data)  # Membuat node baru

        if not self.head:
            # Jika list kosong, node baru jadi head dan tail
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular: tail.next menunjuk ke head
        else:
            self.tail.next = new_node  # Tail lama menunjuk ke node baru
            self.tail = new_node       # Update tail ke node baru
            self.tail.next = self.head # Circular: tail.next menunjuk ke head

    # Mencari elemen dengan nilai tertentu dalam circular linked list
    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return

            temp = temp.next  # Lanjut ke node berikutnya

            if temp == self.head:  # Jika sudah kembali ke head, berhenti
                break


        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")  # Jika tidak ditemukan



# Contoh penggunaan CircularSinglyLinkedList
cll = CircularSinglyLinkedList()
cll.insert_at_end(3)   # Menambah 3 ke list
cll.insert_at_end(7)   # Menambah 7 ke list
cll.insert_at_end(12)  # Menambah 12 ke list
cll.insert_at_end(19)  # Menambah 19 ke list
cll.insert_at_end(25)  # Menambah 25 ke list

key = int(input("Masukkan elemen yang ingin dicari: "))  # Input elemen yang dicari
cll.search(key)  # Cari elemen dalam list
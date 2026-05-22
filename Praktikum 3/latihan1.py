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

    # Menghapus node pertama yang datanya sama dengan key
    def delete_node(self, key):
        temp = self.head

        # Jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None  # (opsional, Python akan garbage collect)
            return

        prev = None
        # Menelusuri node sampai menemukan data yang dicari
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Data tidak ditemukan")  # Jika data tidak ditemukan
            return

        prev.next = temp.next  # Menghapus node dari rantai linked list
        temp = None  # (opsional)


    # Menampilkan seluruh isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")  # Menampilkan data node
            temp = temp.next
        print("null")  # Penanda akhir linked list



# Contoh penggunaan LinkedList
ll = LinkedList()
ll.insert_at_end(3)  # Menambah 3 ke list
ll.insert_at_end(5)  # Menambah 5 ke list
ll.insert_at_end(7)  # Menambah 7 ke list
ll.insert_at_end(9)  # Menambah 9 ke list

print("Sebelum hapus:")
ll.display()  # Menampilkan isi list

ll.delete_node(7)  # Menghapus node dengan data 7

print("Sesudah hapus:")
ll.display()  # Menampilkan isi list setelah penghapusan

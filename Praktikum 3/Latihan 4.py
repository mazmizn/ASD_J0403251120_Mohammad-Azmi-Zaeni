class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = other_list.head

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


def buat_linked_list_dari_input(pesan):
    ll = LinkedList()
    data = input(pesan)

    if data.strip() == "":
        return ll

    angka = data.split()

    for x in angka:
        ll.insert_at_end(int(x))

    return ll


# INPUT USER
ll1 = buat_linked_list_dari_input("Masukkan elemen untuk Linked List 1: ")
ll2 = buat_linked_list_dari_input("Masukkan elemen untuk Linked List 2: ")

print("\nLinked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

ll1.merge(ll2)

print("\nLinked List setelah digabungkan:")
ll1.display()

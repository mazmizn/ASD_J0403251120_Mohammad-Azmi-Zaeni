#===============================================================
#Nama   : Mohammad Azmi Zaeni
#NIM    : J0403251120
#Kelas  : A1
#===============================================================

#===============================================================
#Implementasi Dasar : Node pada Linked List
#===============================================================



class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini merujuk ke node berikutnya (awal=none)

#1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mengubah Node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : Menelusuri mode dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ii
    current=current.next #pindah ke node berikutnya
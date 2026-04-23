#1
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def append(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return

        # Cari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Hubungkan node terakhir dengan node baru
        current.next = new_node
        new_node.prev = current

    # Menambah node di awal
    def prepend(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Menghapus node berdasarkan data
    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                # Jika node pertama
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                    current.prev.next = current.next

                    if current.next:
                      # Menghubungkan node berikutnya dengan node sebelumnya
                        current.next.prev = current.prev
                return

            current = current.next

    # Menampilkan dari depan ke belakang
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Menampilkan dari belakang ke depan
    def display_backward(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next

        # Tampilkan mundur
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

parkiran = DoubleLinkedList()

def tambah_kendaraan (plat):
    parkiran.append(plat)
    print(f"{plat}")

def tampilkan_maju():
    print ("Antrian kendaraan maju: ")
    parkiran.display_forward()

def tampilkan_mundur():
    print ("Antrian kendaraan mundur: ")
    parkiran.display_backward()

#3
def hapus_kendaraan(plat):
    parkiran.delete(plat)

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def append(self, data):
        new_node = Node(data)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Sambungkan node terakhir ke node baru
        current.next = new_node
        new_node.next = self.head

antrian_valet = CircularLinkedList()

def tambah_petugas(nama):
    antrian_valet.append(nama)

def giliran_petugas(n):
    if not antrian_valet.head:
        print ("Antrian kosong.")

    current = antrian_valet.head
    for i in range(1, n+1):
        print(f"Giliran {i}: {current.data}")
        current = current.next

#1
print ("_"*31)
tambah_kendaraan("BM 00 N")
tambah_kendaraan("B 1234 ABC")
tambah_kendaraan("D 5678 XYZ")
tambah_kendaraan("A 9999 TUV")

print ("== Menampilkan Data Maju ==")
tampilkan_maju()

print ("== Menampilkan Data Mundur ==")
tampilkan_mundur()

#2
print("sebelum: ")
tampilkan_maju()

hapus_kendaraan("B 1234 ABC")

print ("sesudah: ")
tampilkan_mundur()

#3
tambah_petugas("Jamal")
tambah_petugas("Andi")
tambah_petugas("Budi")
tambah_petugas("Citra")
tambah_petugas("Dewi")

giliran_petugas(6)
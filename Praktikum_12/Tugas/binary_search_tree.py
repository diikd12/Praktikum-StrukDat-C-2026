class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__ (self):
        self.root = None
        self.count = 0

    def insert_recursive (self, current_node, id_buku, judul):
        if id_buku < current_node.id:
            if current_node.left is None:
                current_node.left = Node(id_buku, judul)
                print (f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self.insert_recursive(current_node.left, id_buku, judul)
        elif id_buku > current_node.id:
            if current_node.right is None:
                current_node.right = Node(id_buku, judul)
                print (f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self.insert_recursive(current_node.right, id_buku, judul)

    def insert (self, id_buku, judul):
        if self.root is None:
            self.root = Node (id_buku , judul)
            print (f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self.insert_recursive(self.root, id_buku, judul)

    def search_recursive (self, current_node, id_buku):
        if current_node is None or current_node.id == id_buku:
            return current_node
        if id_buku < current_node.id:
            return self.search_recursive(current_node.left, id_buku)
        return self.search_recursive(current_node.right, id_buku)

    def search (self, id_buku):
        result = self.search_recursive(self.root, id_buku)
        if result is not None:
            print (f"[SEARCH] Mencari {id_buku}... Ditemukan! Judul: {result.judul}")
        else:
            print (f"[SEARCH] Mencari {id_buku}... Data tidak ditemukan")

    def inorder_recursive (self, current_node):
        if current_node is not None:
            self.inorder_recursive(current_node.left)
            print (f"{self.counter}. ID: {current_node.id} - {current_node.judul}")
            self.counter += 1
            self.inorder_recursive(current_node.right)

    def traversal_inorder (self):
        self.counter = 1
        self.inorder_recursive (self.root)

    def get_min (self):
        current = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current.id
    
    def get_max (self):
        current = self.root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current.id
    
    def height_recursive (self, current_node):
        if current_node is None:
            return -1
        else:
            l_height = self.height_recursive(current_node.left)
            r_height = self.height_recursive(current_node.right)
            return max(l_height, r_height) +1
        
    def height (self):
        return self.height_recursive(self.root)
    
def main():
    print ('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
    print ('='*35)

    katalog = BinarySearchTree()
    katalog.insert(50, "Dasar Pemrograman")
    katalog.insert(30, "Struktur Data")
    katalog.insert(70, "Kecerdasan Buatan")
    katalog.insert(20, "Matematika Diskrit")
    katalog.insert(40, "Basis Data")
    katalog.insert(60, "Jaringan Komputer")
    katalog.insert(80, "Sistem Operasi")
    
    print('')

    print ("[INFO]  Koleksi Buku (In-Order Traversal):")
    katalog.traversal_inorder()

    print ('')

    katalog.search(60)
    katalog.search(100)

    print ('')

    print (f"[STATISTIK] ID Terkecil: {katalog.get_min()}")
    print (f"[STATISTIK] ID Terbesar: {katalog.get_max()}")
    print (f"[INFO] Tinggi (height) Tree: {katalog.height()}")
    print ('='*35)
    
    print ("Simulasi selesai!")

main()
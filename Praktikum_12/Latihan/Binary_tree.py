class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__ (self):
        self.root = None

    def insert_manual(self):
        self.root = node('A')
        self.root.left = node('B')
        self.root.right = node('C')

        self.root.left.left = node('D')
        self.root.left.right = node('E')

        self.root.right.left = node('F')

    def traverse_preorder(self, node, result = None):
        if result is None:
            result = []
        
        if node:
            result.append(node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)
            return result
        
    def traverse_inorder(self, node, result = None):
        if result is None:
            result = []

        if node:
            self.traverse_inorder(node.left, result)
            result.append (node.data)
            self.traverse_inorder(node.right, result)
            return result
    
    def traverse_postorder(self, node, result = None):
        if result is None:
            result = []
        
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)
            return result
        
    def get_leaf_nodes(self, node, result = None):
        if result is None:
            result = []

        if node:
            if node.left is None and node.right is None:
                result.append(node.data)

            self.get_leaf_nodes(node.left, result)
            self.get_leaf_nodes(node.right, result)
        return result

def main():
    print ('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
    print ("="*50)

    print ("[INFO] Membangun Struktur Gudang...")
    tree = BinaryTree()
    tree.insert_manual()
    
    print ("[INFO] Struktur berhasil dibuat.")
    
    print ('')

    print ("HASIL AUDIT: ")
    print (f"1. pre_order :  {tree.traverse_preorder(tree.root)}")
    print (f"2. in_order  : {tree.traverse_inorder(tree.root)}")
    print (f"3. post_order: {tree.traverse_postorder(tree.root)}")
    
    leaf = tree.get_leaf_nodes(tree.root)
    print('')
    print (f"[DATA] Gudang Ujung (Leaf Nodes): {', '.join(leaf)}")
    print ("="*50)
    print ("Audit Selesai!")

main()
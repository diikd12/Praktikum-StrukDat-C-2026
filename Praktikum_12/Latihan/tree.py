class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
                self.root = None

    def insert_root(self,data):
          self.root = node(data)

    def insert_left(self, parent, data):
          if parent.left is None:
                parent.left = node(data)
          else:
                new_node = node(data)
                new_node.left = parent.left
                parent.left = new_node
    
    def insert_right(self, parent, data):
          if parent.right is None:
                parent.right = node(data)

          else:
                new_node = node(data)
                new_node.right = parent.right
                parent.right = new_node

pohon = BinaryTree()

def main():
    print(f"{pohon.insert_root(10)}")
    print(f"{pohon.insert_left(pohon.root, 5)}")
    print(f"{pohon.insert_right(pohon.root, 15)}")

main()
#hasilnya none
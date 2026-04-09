class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sisipkan_VIP(head, plat_baru, plat_target):
   newNode = Node(plat_baru)
   if head.data == plat_target:
      newNode.next = head
      return newNode
   currentNode = head
   while currentNode.next and currentNode.next.data != plat_target:
      currentNode = currentNode.next
      if currentNode.next is None:
         return head
      newNode.next = currentNode.next
      currentNode.next = newNode
      return head

def tampilkanAntrean (head):
   currentNode = head
   while currentNode:
      print(currentNode.data, end = " => ")
      currentNode = currentNode.next
      print ("Null")

plat1 = Node("B 1234 ABC")
plat2 = Node("D 8888 XYZ")
plat3 = Node("A 111 TUV")
plat4 = Node("B 2022 EFG")

plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

print ("Daftar plat kendaraan yang terdaftar: ")
traverseAndPrint(plat1)
plat_baru = "BM 2225 REA"
plat1 = sisipkan_VIP(plat1, plat_baru, 3)
print ("Daftar plat setelah melakukan penyisipan VIP: ")
traverseAndPrint(plat1)
      
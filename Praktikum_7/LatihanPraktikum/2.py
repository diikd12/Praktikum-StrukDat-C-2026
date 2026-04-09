class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def TraverseAndPrint(head):
    current = head
    while current is not None:
        print (current.data, end=" => ")
        current = current.next
    print("Null")

def tambahKendaraan(head, newPlat, position):
  if position == 1:
    newPlat.next = head
    return newPlat

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newPlat.next = currentNode.next
  currentNode.next = newPlat
  return head

def hapusKendaraan(head, platDelete):
  if head is None:
    return head

  if head.data == platDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != platDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head
 
plat1 = Node("B 1234 ABC")
plat2 = Node("D 8888 XYZ")
plat3 = Node("A 111 TUV")
plat4 = Node("B 2022 EFG")

plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

print ("Daftar plat kendaraan yang terdaftar: ")
TraverseAndPrint(plat1)

newPlat = Node ("BM 1716 REA")
plat1 = tambahKendaraan(plat1, newPlat, 5)
print ("Daftar plat setelah melakukan penambahan: ")
TraverseAndPrint(plat1)

platDelete = hapusKendaraan(plat1, plat3)
print ("Daftar plat setelah melakukan penghapusan: ")
TraverseAndPrint(plat1)
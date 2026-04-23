#Soal nomor 2
class Node:
    def __init__(self, url):
        self.url = url

        self.next = None
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def isEmpty(self):
        return self.count == 0
    
    def Visit(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count +=1
    
    def Back(self):
        self.pop()
        return self.peek()

    def pop(self):
        if self.isEmpty():
            return "Stack's Empty!"
        pop_node = self.top
        self.top = self.top.next
        self.count -= 1
        return pop_node.url
    
    def peek(self):
        if self.isEmpty():
            return "Stack's Empty!"
        return self.top.url
    
    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" => ")
            currentNode = currentNode.next
        print()
    
stackku2 = StackLinkedList()

stackku2.Visit('https://www.youtube.com/')
stackku2.Visit('https://www.w3schools.com/python/python_dsa_stacks.asp')
stackku2.Visit('https://www.assettoworld.com/')

print("="*25)
print("     Soal nomor 2")
print("="*25)
print("Visit: ", end="")
stackku2.traverseAndPrint()
print(f"Back: {stackku2.Back()}")
print(f"Peek: {stackku2.peek()}")
print(f"Pop: {stackku2.pop()}")
print("Visit setelah Pop: ", end="")
stackku2.traverseAndPrint()
print(f"Empty: {stackku2.isEmpty()}")
print(f"Size: {stackku2.size()}")

#Soal nomor 1
class StackList:
    def __init__(self):
        self.items = [] 
        
    def is_empty(self):
        return len(self.items) == 0
    
    def visit(self, url):
        self.items.append(url)
    
    def back(self):
        self.pop()
        return self.peek()

    def pop(self):
        if self.is_empty():
            return "Stack's empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack's empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
stackku = StackList()

stackku.visit('https://www.w3schools.com/python/python_dsa_stacks.asp')
stackku.visit('https://www.youtube.com/')
stackku.visit('https://www.assettoworld.com/')

print("="*25)
print("     Soal nomor 1")
print("="*25)
print(f"Visit: {stackku.items}")
print(f"Pop: {stackku.pop()}")
print(f"Stack setelah pop: {stackku.items}")
print(f"Back: {stackku.back()}")
print(f"Peek: {stackku.peek()}")
print(f"Empty: {stackku.is_empty()}")
print(f"Size: {stackku.size()}")
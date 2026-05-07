class hashTable:
    def __init__ (self):
        self.size = 10
        self.table = [[] for _ in range (self.size)]

    def hash_function (self, key):
        total = 0

        for char in str (key):
            total += ord (char)

        return total % self.size

    def insert (self, key, value):
        index = self.hash_function (key)
        bucket = self.table[index]
    
        for i, (k, v) in enumerate (bucket):
            if k == key:
                bucket[i] = (key, value)
                print (f"Data dengan key '{key}' berhasil update")
                return
        
        bucket.append ((key, value))

        print (f"Data '{key}' berhasil ditambahkan!")

    def get (self, key):
        index = self.hash_function (key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete (self, key):
        index = self.hash_function (key)
        bucket = self.table[index]
        for i, (k, v) in enumerate (bucket):
            if k == key:
                del bucket[i]

                print (f"Data dengan key '{key}' berhasil dihapus!")
                return True
        print (f"Key '{key}' tidak ditemukan.")
        return False
    
    def search (self, key):
        index = self.hash_function (key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                print (f"Key '{key}' ditemukan.")
                return True
        print (f"Key '{key}' tidak ditemukan.")
        return False

    def display (self):
        print ("\n===== ISI HASH TABLE =====")
        for index, bucket in enumerate (self.table):
            print (f"Index {index}: {bucket}")
    
        print ("="*30)

ht = hashTable()

ht.insert ("BK111", "Mahir C++ Dalam Satu Jam")
ht.insert ("BK222", "Python Dasar")
ht.insert ("BK333", "Matematika Diskrit")
ht.insert ("BK444", "Atomic Habits")
    
ht.display()
ht.insert ("BK045", "Mein Kampf")
ht.insert ("BK111", "Bumi Manusia")
ht.display()

ht.search ("BK222")
ht.search ("BK001")

ht.delete ("BK333")
ht.display()
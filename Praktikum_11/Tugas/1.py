class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class PoliUmum:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan}")
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return "[PANGGIL] Antrian kosong"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
            
        print(f"[SELESAI] {temp.nama} selesai dengan keluhan: {temp.keluhan}")
        return f"{temp.nama} keluhan: {temp.keluhan}"

    def peekFront(self):
        if self.is_empty():
            return "[PANGGIL] Antrian kosong"
        return f"{self.front.nama} keluhan: {self.front.keluhan}"

    def info(self, kata_tambahan=""):
        print(f"[INFO] Jumlah pasien {kata_tambahan}menunggu: {self.length} orang")

    def is_empty(self):
        return self.length == 0

    def tampilkan_antrian(self):
        print("\n[ANTRIAN SAAT INI]")
        temp = self.front
        urutan = 1
        while temp:
            print(f"{urutan}. {temp.nama.upper()} -> {temp.keluhan}")
            temp = temp.next
            urutan += 1
        print()

    def jumlah_antrian(self):
        print(f"jumlah Antrian: {self.length}")

    def clear(self):
        self.front = None
        self.rear = None
        self.length = 0


def main():
    print("="*50)
    print("SISTEM ANTRIAN POLI UMUM")
    print("RS Sehat Bersama")
    print("="*50)
    print()

    antreanPoliUmum = PoliUmum()

    if antreanPoliUmum.is_empty():
        print("[CEK] YA, antrian masih kosong.")
    else:
        print("[CEK] TIDAK, antrian tidak kosong.")
    print()

    antreanPoliUmum.enqueue("Budi", "Demam tinggi")
    antreanPoliUmum.enqueue("Ani", "Sakit kepala")
    antreanPoliUmum.enqueue("Citra", "Batuk dan pilek")
    print()

    print(f"[PEEK] Pasien selanjutnya: {antreanPoliUmum.peekFront()}")
    print()
    
    antreanPoliUmum.dequeue()
    antreanPoliUmum.enqueue("Dodi", "Sakit perut")
    
    antreanPoliUmum.tampilkan_antrian()
    antreanPoliUmum.jumlah_antrian()
    
    print(f"[PEEK] Pasien selanjutnya: {antreanPoliUmum.peekFront()}")
    print()
    
    antreanPoliUmum.dequeue()
    antreanPoliUmum.info("masih ")

    antreanPoliUmum.clear()
    print("[CLEAR] Antrian dikosongkan.")
    
    if antreanPoliUmum.is_empty():
        print("[CEK] YA, antrian sudah kosong.")
    print()

    print("========================================")
    print("Simulasi Selesai!")
    print("========================================")


main()
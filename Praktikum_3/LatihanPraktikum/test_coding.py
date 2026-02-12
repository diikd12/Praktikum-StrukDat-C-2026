class buku:
    def __init__ (self, Judul, Tahun):
        self.Judul = Judul
        self.Tahun = Tahun

    def Judul_Buku (self):
        print (f'Ini buku dengan judul {self.Judul}')
    
    def Tahun_Buku (self):
        print (f'buku ini di rilis pada tahun {self.Tahun}')

Buku1 = buku("myKisah", 1945)
Buku2 = buku('ayam goyeng', 2020)

print (Buku1.Judul)

Buku1.Tahun_Buku()
Buku2.Judul_Buku()
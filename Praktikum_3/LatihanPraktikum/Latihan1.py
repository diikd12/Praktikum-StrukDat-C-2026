class HandPhone:
    def __init__ (self, Brand, Jenis, Tipe):
        self.Brand = Brand
        self.Jenis = Jenis
        self.Tipe = Tipe

    def know_Brand (self):
        print (f'ini adalah brand {self.Brand}')

    def know_Jenis (self):
        print (f'Jenis dari Brand HP {self.Brand} adalah {self.Jenis}')

    def know_Tipe (self):
        print (f'ini tipenya {self.Tipe}')

#cara buat / ubah yang baru
    def new_Tipe (self, new_Tipe):
        self.Tipe = new_Tipe
        print (f'dan ini adalah tipe barunya {self.Tipe}')

Brand1 = HandPhone('Iphone', 'ipad mini 7', 898989)
Brand2 = HandPhone('Infinix', 'Inf Note 30 Pro', 'IFXX90908')

Brand1.know_Brand()
Brand1.know_Jenis()
Brand1.know_Tipe()
Brand1.new_Tipe(909091)


Brand2.know_Brand()
Brand2.know_Jenis()
Brand2.know_Tipe()

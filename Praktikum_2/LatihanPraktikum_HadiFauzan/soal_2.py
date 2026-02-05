#nomor-1
barang = ("B001", "Laptop Gaming", 15000000)
print(barang[2])

#nomor-2
barang = ("B001", "Laptop Gaming", 15000000)
barang[2] # =14000000
print (barang)  # akan menghasilkan error karena tuple bersifat immutable
#peError: 'tuple' object does not support item assignment

#nomor-3 
barang = ("B001", "Laptop Gaming", 15000000)
kode_barang, nama, harga = barang
print (kode_barang)
print (nama)
print (harga)


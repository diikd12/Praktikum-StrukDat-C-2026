stok_barang = [15, 40, 30, 10 , 25]
index = stok_barang.index(10)
stok_barang[index] = 50
print (stok_barang)

stok_barang.append(5)
stok_barang.sort(reverse = True)
print (stok_barang)

total = sum(stok_barang)
print (total)

rata_rata = sum(stok_barang)/len(stok_barang)
keterangan = "stok aman" if rata_rata > 20 else "WASPADA LAH"
print (keterangan)
gudang_pc = [
 {"item": "Monitor", "harga": 1500000, "stok": 5},
 {"item": "Keyboard", "harga": 400000, "stok": 12},
 {"item": "Mouse", "harga": 250000, "stok": 20}
]
newKey = {"kategori" : "Aksesoris"}
gudang_pc[1].update(newKey)
print (gudang_pc[1])

gudang_pc.append({"item" : "headset", "harga" : 350000, "stok" : 8})
print (gudang_pc)

for total in gudang_pc:
    aset = total["harga"]*total["stok"]
    print (f'Item : {total["item"]} | Total Aset : Rp.{aset}')
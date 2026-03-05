stok_gadget = [
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

def filter_harga(data, min_harga, max_harga):
    hasil_filter = []
    for gadget in data:
        if min_harga <= gadget ['harga'] <= max_harga:
            hasil_filter.append (gadget)
    return hasil_filter 

print ("---=== FILTER GADGET BERDASARKAN HARGA ===---")
batas_atas = int (input('Masukkan max harga: '))
batas_bawah = int (input('Masukkan min harga: '))
gadget_finding = filter_harga (stok_gadget, batas_bawah, batas_atas)

print ("\nHasil pencarian Gadget:")
if len (gadget_finding) > 0:
    for item in gadget_finding:
        print (f"-{item['merk']} {item['tipe']} : Rp {item['harga']}")
    else:
        print ('\nGadget tidak dapat ditemukan')
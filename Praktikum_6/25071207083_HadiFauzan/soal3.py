katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok':2},
            {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

def update_stok (data, sn_cari, jumlah_tambah):
    finded = False
    
    for gadget in data:
        if gadget ['sn'] == sn_cari:
            finded = True
            if 'stok' in gadget:    
                gadget ['stok'] += jumlah_tambah
            else:
                gadget ['stok'] = jumlah_tambah
            print (f"Berhasil menambahkan stok {gadget['merk']} ditambah {jumlah_tambah}. Total stok sekarang: {gadget['stok']}")
            break

    if not finded:
        print (f'Gadget dengan SN {sn_cari} tidak ditemukan.')

print ('--==== UPDATE STOK GADGET ===--')

update_stok(katalog, 'SAM01', 3)
update_stok(katalog, 'OPP01', 5)
update_stok(katalog, 'IPH01', 8) #contoh SN yang tidak ada di dalam katalog

daftar_merk = set()

for gadget in katalog:
    daftar_merk.add(gadget['merk'])

print ('\nDaftar merk gadget yang tersedia:')
print (daftar_merk)

print ('\nDaftar katalog terbaru:')
for produk in katalog:
    print (produk)
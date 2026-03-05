def registrasi_gadget (merk, tipe, harga, sn):
    if harga < 1000000:
        print ("Input harga tidak valid / kurang dari 1.000.000!")
        return None
    elif len (sn) < 5:
        print ("Input Serial Number tidak valid!")
        return None
    else:
        format_harga = f"Rp {harga:,.2f}"
        return {'merk':merk, 'tipe':tipe, 'harga':format_harga, 'sn':sn, 'stok':0, 'status': "Tersedia"}
    
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

def hitung_komisi (total_penjualan, skema, index=0):
    if total_penjualan >= skema [index][0]:
        return skema[index][1]
    else:
        return hitung_komisi (total_penjualan, skema, index+1)
    
inventaris = [
    {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok':2},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
]

skema_komisi = (
 (100000000, 10),
 (50000000, 5), 
 (20000000, 2), 
 (0, 0) 
)

while True:
    print("\n=== PyGadget Hub ===")
    print("1. Tambah Gadget")
    print("2. Daftar Inventaris")
    print("3. Update Stok")
    print("4. Cek Komisi")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        print("\n-- Tambah Gadget --")
        input_merk = input("Merk: ")
        input_tipe = input("Tipe: ")
        input_harga = float(input("Harga: "))
        input_sn = input("Serial Number (SN): ")
        
        hasil = registrasi_gadget(input_merk, input_tipe, input_harga, input_sn)
        if hasil is not None:
            inventaris.append(hasil)
            print("-> Gadget berhasil didaftarkan!")
            
    elif pilihan == '2':
        print("\n-- Daftar Inventaris --")
        print(f"{'Merk':<10} | {'Tipe':<10} | {'Harga':<12} | {'SN':<8} | {'Stok':<5}")
        print("-" * 55)
        
        for item in inventaris:
            harga = item.get('harga', 0)
            stok = item.get('stok', 0)
            print(f"{item['merk']:<10} | {item['tipe']:<10} | {harga:<12.0f} | {item['sn']:<8} | {stok:<5}")
            
    elif pilihan == '3':
        print("\n-- Update Stok --")
        sn_target = input("Masukkan SN Gadget: ")
        jumlah = int(input("Jumlah penambahan stok: "))
        update_stok(inventaris, sn_target, jumlah)
        
    elif pilihan == '4':
        print("\n-- Cek Komisi --")
        nama = input("Nama Sales: ")
        total_jual = float(input("Total Penjualan: Rp "))
        
        persen = hitung_komisi(total_jual, skema_komisi)
        nominal = total_jual * persen / 100
        
        print(f"-> Sales {nama} mendapat komisi {persen}% (Rp {nominal:,.0f})")
        
    elif pilihan == '5':
        print("\nTerima kasih telah menggunakan sistem PyGadget Hub. Sampai jumpa!")
        break
        
    else:
        print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 5.")
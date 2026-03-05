def registrasi_gadget (merk, tipe, harga, sn):
    if harga < 1000000:
        print ("Input harga tidak valid / kurang dari 1.000.000!")
        return None
    elif len (sn) < 5:
        print ("Input Serial Number tidak valid!")
        return None
    else:
        format_harga = f"Rp {harga:,.2f}"
        return {
            'merk' : merk,
            'tipe' : tipe,
            'harga' : format_harga,
            'Serial Number' : sn,
            'stok' : 0,
            'status' : "Tersedia"
        }
    
Inventaris = []

for i in range (1):
    print (f"Masukkan data gadget ke-{i+1}")
    Input_merk = input ("merk: ")
    Input_tipe = input ("tipe: ")
    Input_harga = float(input ("harga: Rp."))
    Input_sn = input ("Serial Number: ")

    gadget = registrasi_gadget (Input_merk, Input_tipe, Input_harga, Input_sn)
    if gadget is not None:
        Inventaris.append (gadget)
        print ("Gadget berhasil ditambahkan ke inventaris!")

print ("\n---=== Daftar Inventaris Gadget ===---")
for produk in Inventaris:
    print (produk)
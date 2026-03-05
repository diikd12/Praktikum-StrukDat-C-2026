skema_komisi = (
 (100000000, 10), # Penjualan >= 100jt -> Komisi 10%
 (50000000, 5), # Penjualan >= 50jt -> Komisi 5%
 (20000000, 2), # Penjualan >= 20jt -> Komisi 2%
 (0, 0) # Di bawah 20jt -> Tidak ada komisi
)

def hitung_komisi (total_penjualan, skema, index=0):
    if total_penjualan >= skema [index][0]:
        return skema[index][1]
    else:
        return hitung_komisi (total_penjualan, skema, index+1)
    
print ("---=== HITUNG KOMISI PENJUALAN GADGET ===---")

nama_sales = input("Masukkan nama sales: ")
total_jual = float(input("Masukkan total penjualan: "))

persen = hitung_komisi (total_jual, skema_komisi)

nominal_komisi = total_jual * persen / 100

print (f"\n--- Rincian Komisi {nama_sales} ---")
print (f"Total penjualan: Rp {total_jual:,.2f}")
print (f"Presentase komisi: {persen}%")
print (f"Nominal komisi: Rp {nominal_komisi:,.2f}")
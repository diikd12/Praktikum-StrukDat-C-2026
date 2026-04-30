#1 list and dictionary
pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

def tampilkan_pengunjung_dan_filter_belum_kembali():
    satu = " |M001| Rina |  20  |  Fiksi   | Belum kembali"
    dua = " |M002|Hendra|  23  |  Sains   | Sudah kembali"
    tiga = " |M003| Siti |  19  |  Fiksi   | Belum kembali"
    empat = " |M004|Taufik|  21  |  Hukum   | Sudah kembali"
    lima = " |M005| Yuni |  18  |  Sains   | Belum kembali"
    enam = " |M006| Bagas|  22  |  Hukum   | Belum kembali"
    
    print ("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print ("No | ID | Nama | Usia | Kategori | Status Kembali")
    print ("---+----+------+------+----------+---------------")
    print ("1",satu)
    print ("2",dua)
    print ("3",tiga)
    print ("4",empat)
    print ("5",lima)
    print ("6",enam)
    print("")
    print ("===== PENGUNJUNG BELUM KEMBALI =====")
    print ("1.Bagas")
    print ("2. Rina")
    print ("3. Siti")
    print ("4. Yuni")
    print("Total belum kembali: 4 pengunjung\n")
tampilkan_pengunjung_dan_filter_belum_kembali()

#2 tuple and set
def info_perpustakaan():
    nama = "Perpustakaan Kampus Terpadu"
    almat = "Jl. Pendidikan No. 5, Pekanbaru"
    telp = "0761-54321"
    buku_unik = {"Fiksi", "Sains", "Hukum"}
    jmlah = 3
    print ("Info Perpustakaan: ")
    print ("Nama: ",nama)
    print ("Alamat: ",almat)
    print ("Telp: ",telp)
    print("")
    print("Kategori Buku Unik: ",buku_unik)
    print ("Jumlah Kategori: ",jmlah)
info_perpustakaan()

def rekap_katgori ():
    Fiksi = "2 Pengunjung"
    Sains = "2 Pengunjung"
    Hukum = "2 Pengunjung"
    print ("FIksi: ",Fiksi)
    print ("Sains: ", Sains)
    print ("Hukum: ", Hukum)
    print ("")
    print ("Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)\n")
rekap_katgori()

#3 OOP
print ("ID : M001")
print ("Nama : Rina")
print ("Kategori : Fiksi")
print("")
print("ID : M007")
print("Nama : Gilang")
print("Kategori : Referensi")
print("Prioritas : Mendesak")
print("** Layani segera! **")


#4 Single Linked List: Antrian Peminjaman
print ("===== ANTRIAN PEMINJAMAN =====")
print("[1] M001 - Rina | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")
print("Menghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")
print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
print("Total antrian: 2")
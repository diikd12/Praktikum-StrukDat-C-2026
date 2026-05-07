class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, namaKota):
        if namaKota not in self.graph:
            self.graph[namaKota] = []

    def tambah_jalan(self, u, v, jarak):
        print (f"[INPUT] Menambahkan Jalan: {u} - {v} ({jarak} KM.)")
        self.tambah_kota(u)
        self.tambah_kota(v)
        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

    def tampilkan_graph(self):
        print (f"\n[INFO] Struktur Jaringan Distribusi")
        for kota, tetangga_list in self.graph.items():
            tetangga_str = ", ".join([f"{t[0]} ({t[1]})" for t in tetangga_list])
            print (f"{kota} terhubung ke: {tetangga_str}")
        print()

    def dijkstra(self, kota_asal):
        print (f"[PROSES] Menghitung rute terpendek dari: {kota_asal}...\n")
        jarak_terpendek = {kota: float('inf') for kota in self.graph}
        jarak_terpendek[kota_asal] = 0
        kota_dikunjungi = set()

        while len(kota_dikunjungi) < len(self.graph):
            kota_sekarang = None
            min_jarak = float('inf')

            for kota in self.graph:
                if kota not in kota_dikunjungi and jarak_terpendek[kota] < min_jarak:
                    min_jarak = jarak_terpendek[kota]
                    kota_sekarang = kota
            if kota_sekarang is None:
                break
            kota_dikunjungi.add(kota_sekarang)

            for tetangga, bobot in self.graph[kota_sekarang]:
                if tetangga not in kota_dikunjungi:
                    jarak_baru = jarak_terpendek[kota_sekarang] + bobot
                    if jarak_baru < jarak_terpendek[tetangga]:
                        jarak_terpendek[tetangga] = jarak_baru
    
        print(f"[HASIL] Jarak Terpendek dari {kota_asal}:")
        no = 1
        for kota, jarak in jarak_terpendek.items():
            if kota != kota_asal:
                print(f"{no}. Ke {kota}: {jarak} KM")
                no += 1
        print("Simulasi Navigasi Selesai!")


logistik = Graph()

logistik.tambah_jalan("Jakarta", "Bandung", 150)
logistik.tambah_jalan("Jakarta", "Cirebon", 200)
logistik.tambah_jalan("Bandung", "Tasikmalaya", 100)
logistik.tambah_jalan("Bandung", "Cirebon", 130)
logistik.tambah_jalan("Cirebon", "Semarang", 250)
logistik.tambah_jalan("Tasikmalaya", "Semarang", 200)


logistik.tampilkan_graph()

logistik.dijkstra("Jakarta")


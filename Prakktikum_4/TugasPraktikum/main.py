from kurs import mata_uang_kurs
from konverter import konversi
from tabulate import tabulate

def tampilkan_kurs():
    table = []
    for kode, nilai in mata_uang_kurs.items():
        table.append ([kode, f'{nilai:,}'.replace(',', '.')])
    print ("=== KONVERTER MATA UANG ===")    
    print (tabulate(table, headers = ["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_kurs()

    Pertama = input ("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    Kedua = input ("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    hasil = konversi(jumlah, Pertama, Kedua, mata_uang_kurs)

    print(f'\nRp {jumlah:,.0f} = {hasil:,.2f} {Kedua}'.replace(',', '.'))

if __name__ == "__main__":
    main()
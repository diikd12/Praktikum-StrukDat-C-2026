platKendaraan = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

arrPlat = platKendaraan[0].split(" ")
angkaAkhirPlat = int(arrPlat[1])
for plat in platKendaraan:
    arrPlat = plat.split(" ")
    angkaAkhirPlat = int(arrPlat[1])
    if angkaAkhirPlat %2 == 0:
        print(f"{plat} adalah plat genap")
    else:
        print(f"{plat} adalah plat ganjil")
    
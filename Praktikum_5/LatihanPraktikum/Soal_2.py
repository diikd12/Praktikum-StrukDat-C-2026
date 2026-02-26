data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

for data, poin in data_aktivitas:
    if poin > 80:
        print (f"{data} mendapatkan predikat gold")
    elif poin >= 50:
        print (f"{data} mendapatkan predikat silver")
    else:
        print (f"{data} mendapatkan predikat bronze")
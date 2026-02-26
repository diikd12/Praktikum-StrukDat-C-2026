def konversi (hasil, Pertama, Kedua, kurs_data):
    if Pertama == Kedua:
        return hasil
    
    if Kedua == "IDR":
        return hasil*kurs_data[Pertama]
    
    if Pertama == "IDR":
        return hasil/kurs_data[Kedua]
    
    KeduaIDR = hasil * kurs_data[Pertama]
    return KeduaIDR/kurs_data[Kedua]
#soal-1 
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}
keahlianKeduaTim = tim_frontend.intersection(tim_backend)
print ('keahlian yang dimiliki oleh kedua tim tersebut adalah =',keahlianKeduaTim)

#soal-2

tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

keahlianBackend = tim_backend.difference(tim_frontend)
print ('keahlian yang hanya dimiliki oleh tim backend adalah =',keahlianBackend)

#soal-3

im_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

totalKeahlian = tim_frontend.union(tim_backend)
print ('daftar total keahlian unik yang tersedia di perusahaan adalah =',totalKeahlian)
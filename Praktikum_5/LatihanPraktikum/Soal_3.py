ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

di_coding = ukm_coding.difference(ukm_robotik)
print(di_coding)

seluruh_ukm = ukm_coding.union(ukm_robotik)
print(seluruh_ukm)

ada = "Andi" in ukm_robotik
print (ada)
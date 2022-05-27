# Birinchi mashinaning tezligini kiritib olamiz
v_birinchi = int(input(" Birinchi mashina tezligini kiriting = "))
# Ikkinchi mashinaning tezligini kiritib olamiz
v_ikkinchi = int(input(" Ikkinchi mashina tezligini kiriting = "))
# Ular orasidagi masofani kiriting
s = int(input(" Masofani kiriting"))
# Vaqtni kiriting
t = int(input(" Vqtni kiriting = "))
masofa = s - ( v_birinchi + v_ikkinchi ) * t
# Masofani ekranga chiqaramiz
print(" Ular orasidagi" ,masofa ," km  masofa qolgan")
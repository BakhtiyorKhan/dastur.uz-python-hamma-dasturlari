# Qayiqning tezligini kiritib olamiz
v_qayiq = int(input(" Qayiqning tezligini kiriting = "))
# Daryo oqimining tezligini kiritib olamiz
u_oqim = int(input(" Daryo oqimining tezligi kiriting = "))
# Daryo oqimini bo'yicha vaqtni kiriting
t_oqim_boyicha = int(input(" Oqim bo'yicha vaqti = "))
# Daryo oqiminiga qarshi vaqtni kiritib olamiz
t_oqim_qarshi = int(input(" Oqimga qarshi vaqti = "))
# Yurgan masofasini aniqlaymiz
masofa = ( v_qayiq + u_oqim ) * t_oqim_boyicha + ( v_qayiq - u_oqim ) * t_oqim_qarshi
# Masofa ekranga chiqaramiz
print(" Masofasi = ",masofa)
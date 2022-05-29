# If 4 masalasi

bir_son = int(input(" Birinchi sonni kiriting = "))
ikki_son = int(input(" Ikkinchi sonni kiriting = "))
uch_son = int(input(" Uchinchi sonni kiriting = "))

# Sonlarning nechtasi musbatligini aniqlash bu o'zgaruvchini kiritamiz musbat bo'lsa qiymati bittaga oshadi
musbatlar_soni = 0

# Sonlarning nechtasi musbatligini aniqlaymiz
if bir_son > 0:
    musbatlar_soni +=1
if ikki_son > 0:
    musbatlar_soni +=1
if uch_son > 0:
    musbatlar_soni +=1

print(f" Uchta sonning {musbatlar_soni} tasi musbat")
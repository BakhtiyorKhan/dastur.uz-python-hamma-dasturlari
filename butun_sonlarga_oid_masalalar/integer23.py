# Integer 23 masalasi

sekund = int(input(" Kun boshidan beri sekundni kiriting = "))

# Soatni aniqlaymiz
soat = sekund // 3600

# Minutni aniqlaymiz
minut = sekund % 3600 // 60

# Sekundni aniqlaymiz
sekund = sekund % 60

print(f" Kun boshidan beri  {soat:02}:{minut:02}:{sekund:02} vaqt o'tgan")
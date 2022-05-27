# Integer 21 masalasi

sekund = int(input(" Kun boshidan beri sekundni kiriting = "))

# Minutni aniqlaymiz
minut = sekund // 60

# Sekundni aniqlaymiz
sekund = sekund % 60

print(f" Kun boshidan beri  {minut:02}:{sekund:02} vaqt o'tgan")
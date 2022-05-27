# Integer 22 masalasi

sekund = int(input(" Kun boshidan beri sekundni kiriting = "))

# Soatni aniqlaymiz
soat = sekund // 3600


# Sekundni aniqlaymiz
sekund = sekund % 3600

print(f" Kun boshidan beri  {soat:02} soat {sekund:02} sekund o'tgan")
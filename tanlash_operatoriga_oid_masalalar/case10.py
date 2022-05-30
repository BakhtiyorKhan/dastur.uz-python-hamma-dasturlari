# Case 10 masalasi

print("-----------Yo'nalishlar-----------")
print("s-shimol, j-janub, q-sharq, g-g'arb")
yonalish = input(" Yo'nalishni tnalang = ")
print("-----------Burilishlar-----------")
print("0-harakatni davom ettirish, 1-chapga burilish, 2-o'nga burilish")
burilish = input(" Burilishni tanlang = ")

# Oyni aniqlaymiz
qutb = {
    's': "Shimolga",
    'j': "Janubga",
    'q': "Sharqga",
    'g': "G'arbga",
}
kamonda = {
    '0': " harakatni davom ettir",
    '1': " chapga burilish kerak",
    '2': " o'nga burilish kerak",
}

print(f" {qutb[yonalish]}{kamonda[burilish]}")
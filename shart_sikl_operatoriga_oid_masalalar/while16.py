# While 16 masala

foiz = int(input(" Foizni kiriting = "))

yugurish = 10
kun = 0

while yugurish < 200:
    yugurish = yugurish + yugurish * (foiz / 100)
    kun +=1

print(" Sportchi 200 kmni yugurib o'tish uchun ",kun," kun sarflagan")
print(" Masofa = ",int(yugurish))
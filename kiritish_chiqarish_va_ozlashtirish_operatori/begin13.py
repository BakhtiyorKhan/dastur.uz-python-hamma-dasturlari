#  Birinchi aylananing radiusi ikkinchi aylananing radiusidan katta
#   Birinchi aylananing radiusini  kiritib olyapmiz
radiusi_bir = int(input(" Birinchi aylananing radiusini kiriting = "))
#   Ikkinchi aylananing radiusini  kiritib olyapmiz
radiusi_ikki = int(input(" Ikkinchi aylananing radiusini kiriting = "))
# O'zgarmasni kiritamiz
PI = 3.14
# Birinchi aylananing yuzasini hisoblaymiz
yuza_bir = PI * radiusi_bir ** 2
# Ikkinchi aylananing yuzasini hisoblaymiz
yuza_ikki = PI * radiusi_ikki ** 2
# Ikkita aylananing yuzalari ayirmasi hisoblaymiz
yuza_ayirmasi = yuza_bir - yuza_ikki
# Birinchi aylananing yuzasini ekranga chiqaring
print(" Birinchi aylananing yuzasi = ",yuza_bir)
# Ikkinchi aylananing yuzasini ekranga chiqaring
print(" Ikkinchi aylananing yuzasi = ",yuza_ikki)
# Ikki aylananing yuzasining ayirmasi
print(" Ikki aylananing yuzasi ayirmasi = ",yuza_ayirmasi)

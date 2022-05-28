# Boolean 20 masala

a = int(input(" Uch xonali sonni kiriting = "))

# Sonning raqamlari har xil ekanligini  aniqlaymiz
har_xil = a // 100 != a % 100 // 10 and a // 100 != a % 10 and a % 100 // 10 != a % 10

# True chiqsa har xil sonlar False har xil son emas
print(har_xil)
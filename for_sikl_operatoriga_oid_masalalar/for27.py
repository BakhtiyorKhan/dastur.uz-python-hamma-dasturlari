# For 27 masalasi

n = int(input(" n ni kiriting = "))
x = float(input(" x ning qiymatini kiriting = "))

sum = x
surat = 1
maxraj = x
daraja = 1

# Yig'indini hisoblaymiz
if x != 0:
  for i in range (1,n+1):
      daraja *= x * x
      maxraj *= 2 * i
      surat *= 2 * i - 1

      sum += daraja * surat / (maxraj * (2 * i + 1))
else:
    sum = 1


print(f" Yig'indi = {sum}")
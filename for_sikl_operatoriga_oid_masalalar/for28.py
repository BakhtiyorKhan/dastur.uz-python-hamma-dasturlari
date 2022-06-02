# For 28 masalasi

n = int(input(" n ni kiriting = "))
x = float(input(" x ning qiymatini kiriting = "))

sum = 1 + x /2
surat = 1
maxraj = 2
daraja = x

# Yig'indini hisoblaymiz
if x != 0:
  for i in range (2,n+1):
      daraja *= (-1) * x
      maxraj *= 2 * i
      surat *= 2 * i - 3

      sum += daraja * surat / maxraj
else:
    sum = 1


print(f" Yig'indi = {sum}")
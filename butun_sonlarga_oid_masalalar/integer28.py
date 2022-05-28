# Integer 28 masalasi

k = int(input(" 1-365 orasidagi sonni kiriting = "))
n = int(input(" Haftaning nechinchi kuni ekani kiriting = "))

# Kunni aniqlaymiz
kun = ( k + n - 2 ) % 7 + 1

print(" Haftaning kuni = ",kun)
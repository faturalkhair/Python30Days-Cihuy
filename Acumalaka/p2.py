print("adakah")
print("========================")

umur = 20
if umur >= 20:
    print("hahaha tua")
else:
    print("masih muda brow")


nilai = 50
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("gagal coeg")

fruits = ["Kelapa", "Mangga", "Rambutan"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)


print("--------------")
for i in range(10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)
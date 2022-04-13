"""
Entiers consecutifs en decroissant
"""


b = int(input("Sasir un entier b: " ))
a = int(input("Sasir un entier a: "))
while a < b:
     a = int(input("Sasir un entier: "))
for i in range(a, b - 1, -1):
    print(i)

"""
Le Minimum de la liste saisie
"""



z = int(input("Saisir une taille pour la liste: "))
while z <= 1:
    z = int(input("Saisir une taille valide: "))

L = []

for i in range(z):
    nbr = int(input("Saisir un nombre: "))
    L.append(nbr)
print("Le nombre le plus petit est : ", min(L))

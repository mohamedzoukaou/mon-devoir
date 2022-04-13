"""
Somme des multiples de 10
"""



L =[10,455,750,12,40,9,18,400,31]
s = 0
for i in range(len(L)) :
    if L[i] % 10 == 0 :
        s += L[i]
print(f"La somme des multiples de 10 est: {s}" )

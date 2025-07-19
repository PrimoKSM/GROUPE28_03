nombre = int(input("Entrez un nombre  pour sa table de multiplication: "))

print(f"\nTable de multiplication de {nombre} :")
for i in range(1, 13):
    resultat = nombre*i
    print(f"{nombre} x {i} = {resultat}")

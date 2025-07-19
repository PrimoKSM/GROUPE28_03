entree = input("Entrez une liste de valeurs : ")
liste = entree.split()
uniques = []

for item in liste:
    if item not in uniques:
        uniques.append(item)

print(f"Liste sans doublons : {uniques}")

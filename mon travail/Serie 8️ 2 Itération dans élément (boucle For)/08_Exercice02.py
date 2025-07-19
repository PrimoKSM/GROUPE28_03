entree = input("Entrez des d'éléments : ")
liste= entree.split()

for i, elem in enumerate(liste):
    print(f"Indice {i} : {elem}")

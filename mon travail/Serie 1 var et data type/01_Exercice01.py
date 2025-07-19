prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

jours_vécus = age * 365
print("\n=== Profil ===")
print(f"Nom : {prenom}")
print(f"Âge : {age} ans ({jours_vécus} jours vécus environ )")
print(f"Ville : {ville}")
print(f"Métier : {metier}")




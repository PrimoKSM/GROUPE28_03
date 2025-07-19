heures = int(input("Nombres d'heures : "))
minutes = int(input("Nombres de minutes : "))
secondes = int(input("nombres de secondes : "))

total_secondes = heures * 3600 + minutes * 60 + secondes
print(f"Durée totale  : {total_secondes} secondes")

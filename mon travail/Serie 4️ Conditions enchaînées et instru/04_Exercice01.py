age = int(input("Âge : "))
situation = input("statut(étudiant, salarié, retraité) : ").lower()

if age < 18:
    tarif = 5
elif 18 <= age <= 25:
    if situation == "étudiant":
        tarif = 6
    elif situation == "salarié":
        tarif = 8
    else:
        tarif = 10
else:
    if situation == "retraité":
        tarif = 7
    else:
        tarif = 10

print(f"votre tarif est de : {tarif} €.")

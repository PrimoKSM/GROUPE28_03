etudiants = [("Alice", 16), ("Paul", 14), ("Sara", 15), ("David", 12)]

print("Étudiants ayant une note ≥ 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"{nom} : {note}")

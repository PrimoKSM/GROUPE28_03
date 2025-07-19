plat = input("Choisissez un type de plat (viande, poisson, végétarien) : ").lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant, à point, bien cuit) : ").lower()
    print(f"Vous avez choisi une viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron, beurre) : ").lower()
    print(f"Vous avez choisi un poisson avec une sauce {sauce}.")
elif plat == "végétarien":
    choix = input("Souhaitez-vous une salade ou des pâtes ? : ").lower()
    print(f"Vous avez choisi un plat végétarien avec {choix}.")
else:
    print("Choix invalide.")

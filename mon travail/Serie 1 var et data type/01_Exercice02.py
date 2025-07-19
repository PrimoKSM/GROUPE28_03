nom_produit = "Casque Bluetooth"
prix = 150.0
stock = 35
remise = 0.15

prix_final = prix * (1 - remise)

print("\n--- Fiche Produit ---")
print(f"produit : {nom_produit}")
print(f"Prix initial : {prix} €")
print(f"Remise : {remise} %")
print(f"Prix final : {prix_final:.2f} €")
print(f"Stock disponible : {stock}")

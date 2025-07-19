temp = float(input("Température en (°C): "))

if temp >= 35:
    print("Très chaud, restez hydraté.")
elif 25 <= temp <= 34:
    print("Chaud, faites attention au soleil.")
elif 15 <= temp <= 24:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")

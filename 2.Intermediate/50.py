"""
Printer une phrase tant que l'utilisateur le demande
"""
compteur = 0
turnOn = 'o'

while turnOn == 'o':
    print(f"Le compteur est maintenant a {compteur}")
    user = input("Voulez-vous continuer? o/n ")
    compteur += 1
    if user == turnOn:
        continue
    break
    
# 2e methode
i = 0
continuer = "o"

while continuer == "o":
    print(f"Le compteur est maintenant à {i}")
    continuer = input("Voulez-vous continuer ? o/n ")
    i += 1

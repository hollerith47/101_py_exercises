"""
Créer un programme pour surveiller un dossier
"""
import os
import time

dossier_recherche = "C:/Users/herma/Desktop"
dossier_a_chercher = "output"

delai_attente = input("Entrez un temps de rafraichissement : ")

# listdir du module os nous permet de list la liste de sous-dossier contenu dans un dossier
while dossier_a_chercher not in os.listdir(dossier_recherche):
    print("Dossier introuvable ...")
    time.sleep(int(delai_attente))
    
print("Trouvé !")

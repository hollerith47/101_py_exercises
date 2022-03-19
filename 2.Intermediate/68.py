"""
 Trouver un fichier à l'intérieur d'un dossier
 dans cet exercice nous allons trouver tout le fichier css nomme style.css contenu dans mon bureau
"""
import os
from glob import glob


dossier_recherche = "C:/Users/herma/Desktop"
fichier_a_trouver = "style.css"

# ici nous passons au module glob le dossier du recherche avec /** pour lui dire de faire le recherche recursive
fichiers = glob(dossier_recherche + "/**", recursive=True)
# on procede a une separation de la var fichiers en deux
fichiers_trouvee = [f for f in fichiers if os.path.split(f)[1] == fichier_a_trouver]
print(fichiers_trouvee)

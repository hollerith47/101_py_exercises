"""
Vérifier le nombre de fichiers et dossiers dans un dossier
et y ajouter si possible le temps d'execution
"""
from time import time
from glob import glob

current_time = time()
# dossier_recherche = "C:/Users/herma/Desktop"
# recherche de fichiers et dossiers dans tout l'ordinateur
dossier_recherche = "C:"

fichiers_et_dossiers_contenu = glob(f"{dossier_recherche}/**", recursive=True)
nombres_fichier_et_dossiers = len(fichiers_et_dossiers_contenu)
print(nombres_fichier_et_dossiers)
print(f"Temps d'exécution : {time()- current_time} s")

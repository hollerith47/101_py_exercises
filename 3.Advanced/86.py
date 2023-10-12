"""
Chercher un mot dans des fichiers
"""
import os
from glob import glob
from pprint import pprint

dossier = "/Users/herma/Documents"
mot = 'Python'
fichiers = glob(f"{dossier}/**/*.txt", recursive=True)

fichiers_trouves = []

for filename in fichiers:
    print(filename)
    with open(filename, 'r') as f:
        contenu_fichier = f.read()
        if mot in contenu_fichier:
            fichiers_trouves.append(filename)
    
    
pprint(fichiers_trouves)

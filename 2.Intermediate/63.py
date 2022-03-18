"""
 Écrire dans un fichier
"""
import os.path
from pathlib import Path

currentDirectory = Path.cwd()  # cwd = current working directory pour identifier le ou se trouve le script
file_created = Path.joinpath(currentDirectory, "fichier_63.txt")

# ecrire dans un fichier
# with open(file_created, 'w') as f:
#     f.write("Hello world !")
#     print(f)

# lire le fichier
with open(file_created, 'r') as f:
    content = f.readlines()
print(content)
# print(currentDirectory)

# ---------------------------------------------------------------
# dans cette autre methode on va utiliser le module os
cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, "fichier_63.txt")

with open(fichier, 'r') as f:
    contenu = f.readlines()

print(contenu)
print(currentDirectory)
print(cur_dir)
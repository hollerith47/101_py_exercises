"""
 Fixer erreur de variable dans un fichier
 ici nous allons lire le contenu du fichier variable.txt qui contient le string false
 l'objectif est de recuperer le contenu, le convertir en booleen et demander a notre script
 si le contenu de la variable est True ou False
 """
import os
import distutils.util


cur_dir = os.path.realpath(os.path.dirname(__file__))

# creation et ecriture dans le fichier
fichier = os.path.join(cur_dir, "variable_64.txt")
with open(fichier, 'w') as f:
    f.write("true")

# lecture du contenu du fichier
with open(fichier, "r") as f:
    variable = f.read()

# grace a cette ligne on parvient a recuperer le mot contenu dans variable et le convertir en booleen
vraie_variable = bool(distutils.util.strtobool(variable))
if vraie_variable:
    print("La variable est un boolean True")
else:
    print("La variable est un boolean False")
    
    
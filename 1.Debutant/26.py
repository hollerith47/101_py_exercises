"""
Dans cet exercice, nous allons importer une variable d'un autre dans notre
script principal.
le but de l'exercice est d'importer cette variable dans le fichier exercice.py
pour l'afficher grace a la fonction print.
"""

from constants import *

print(nom)

"""
import constants
print(constants.nom)
EXPLICATION

Rien de plus simple dans cet exercice ! Il suffisait d'importer le module constants et de faire un print de la variable
'nom' contenue à l'intérieur de ce module. Un exercice simple, mais qui nécessite de bien comprendre le fonctionnement
des modules et les possibilités qu'ils offrent.

POINTS IMPORTANTS À RETENIR
Pour importer une variable d'un module, il suffit d'importer le module dans lequel la variable est contenue.
"""
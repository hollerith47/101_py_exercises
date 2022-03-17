"""
Notions abordees: les modules, la boucle for.
le but de cet exercice est de generer 6 lancer de dés aléatoires, allant de 1 à 6
"""
from random import randint

for _ in range(6):
    print(randint(1, 6))

# 2e option-----------------------------
import random

for _ in range(6):
    nombre = random.choice(range(1, 7))
    print(nombre)

"""
Pour générer un nombre aléatoire de 1 à 6, nous utilisons donc la ligne de code suivante :

nombre = random.choice(range(1, 7))

Si vous ne voulez pas passer par une liste, vous pouvez également utiliser la fonction randint, comme ceci :

nombre = random.randint(1, 6)

La deuxième indication de l'exercice était de générer 6 lancer de dés.

Pour cela, on utilise une boucle for et encore une fois la fonction range, pour répéter l'opération 6 fois :

for _ in range(6):
    # Opération à répéter
Vous remarquerez que nous utilisons un nom de variable assez spécifique (un tiret du bas). En effet, ce nom de variable
est une convention en Python lorsque l'on génère une variable que l'on ne compte pas utiliser. Ici, on veut juste répéter
une opération un certain nombre de fois, mais nous ne faisons aucun usage de cette variable, nous utilisons donc un tiret
du bas pour signifier à quelqu'un qui pourrait lire notre script que cette variable n'est pas utilisée à l'intérieur de
la boucle.

POINTS IMPORTANTS À RETENIR
Pour récupérer un élément aléatoire dans une liste, on utilise la fonction choice du module random.
"""
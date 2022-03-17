"""
exercice tres simple sur le module
"""
import random

#nombre_aleatoire_error = randint(0, 5) #il manque random
nombre_aleatoire = random.randint(0, 5) #correction
print(nombre_aleatoire)


"""
EXPLICATION
Pour utiliser une fonction contenue à l'intérieur d'un module, il est impératif de préfixer cette fonction par le nom du module.

Dans cet exercice, on import le module comme suit :

import random

Pour utiliser la fonction randint, il faut donc faire :

random.randint(0, 5)

Si nous voulons utiliser directement la fonction randint, il est possible de le faire avec une syntaxe d'import
légèrement différente :

from random import randint

De cette façon, on importe directement la fonction randint et non pas tout le module random. La fonction randint est
donc directement accessible dans l'espace global de notre script :

randint(0, 5)

POINTS IMPORTANTS À RETENIR
Pour utiliser une fonction à l'intérieur d'un module, il ne faut pas oublier de préfixer la fonction par le nom du module.
Pour importer une fonction à l'intérieur d'un module directement dans l'espace global de notre script, on peut utiliser
la syntaxe from module import fonction .
"""
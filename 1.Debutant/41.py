"""
 Trouver l'erreur dans la fonction
 la fonction multiplicateur_mot retourne une erreur.
 Trouver cette erreur et modifiez la fonction pour qu'elle ne retourne plus
 d'erreur.
"""


# erreur
# def multiplicateur_mot(mult=5, mot):
# 	return mot * mult

def multiplicateur_mot(mot, mult=5):
    return mot * mult


mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)

"""
    EXPLICATION

L'ordre des paramètres par défaut dans une fonction a son importance ! En effet, si vous définissez une valeur par
défaut pour un paramètre qui se trouve en première position, vous avez l'obligation de définir une valeur par défaut
pour tous les paramètres qui suivent.

La façon rapide de régler l'erreur qui se trouvait dans ce script était donc soit de définir une valeur par défaut
pour les deux paramètres de la fonction, soit d'inverser l'ordre des paramètres, ce que nous avons fait dans la
solution proposé ci-dessus.

    POINTS IMPORTANTS À RETENIR

    L'ordre des paramètres dans une fonction a son importance ! Vous ne pouvez pas mettre un paramètre sans valeur
    par défaut après un paramètre qui en a une. """
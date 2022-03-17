"""
Trouver l'erreur dans la fonction
cette fois-ci le script ne retourne pas d'erreur mais n'affiche pas le resultat attendu

def addition(a, b):
    c = a + b

resultat = addition(5, 10)
print(resultat)
"""


def addition(a, b):
    c = a + b
    return c


resultat = addition(5, 10)
print(resultat)

"""
    EXPLICATION
Une fonction peut, dans certains cas, ne pas retourner de résultat (par exemple, une fonction qui exécute plusieurs print à la suite, pour afficher un message de bienvenue par exemple, n'a pas besoin de retourner de valeur spécifique).

Cependant, ici, la fonction sert à calculer la somme de deux valeurs. Il faut donc retourner d'une façon où d'une
autre  le résultat de cette addition.

Pour retourner une valeur dans une fonction, on utilise le mot clé return, comme ici :

    return c

Cela nous permet de récupérer la valeur de l'addition lors de l'appel de la fonction dans une variable :

    resultat = addition(5, 10)

    POINTS IMPORTANTS À RETENIR
    Pour retourner une valeur à l'intérieur d'une fonction, on utilise le mot clé return.
"""


"""
Vérifier si une phrase est un palindrome
Dans cet exercice nous allons verifier si un mot est un polindrome ou nom. Un
polindrome est un mot ou une phrase qui peut se lire de la meme facon dans le deux sens.

"""
mot = "Un roc cornu"
mot_new = mot.lower().replace(" ", "")
print(mot_new[::-1])
print(mot_new)

if mot_new == mot_new[::-1]:
    print(True)
else:
    print(False)
    
"""
    EXPLICATION

Un palindrome est un mot ou une phrase qui peut se lire de la même façon dans les deux sens
(exemple : "mon nom", "La malade pédala mal" ou comme l'exemple ici "Un roc cornu").

Pour vérifier si un mot ou une phrase est un palindrome, il faudra donc vérifier si la phrase d'origine est égale à la
phrase d'origine inversée.
Cette fois-ci, nous n'utiliserons pas la fonction reverse mais la syntaxe de slice : [::-1]
Avant cela, nous convertissons la phrase en minuscule pour ne pas que la casse influence le résultat et nous supprimons
les espaces avec la méthode replace :

    mot_lower = mot.lower().replace(" ", "")

Nous vérifions ensuite avec une structure conditionnelle si la chaîne de caractère en minuscule et sans espace est égal
à cette même chaîne de caractère inversée avec la syntaxe [::-1] :

    if mot_lower == mot_lower[::-1]:
        print(True)
    else:
        print(False)

En fonction de la structure conditionnelle nous affichons "True" ou "False".

    POINTS IMPORTANTS À RETENIR

    Pour enlever tous les espaces d'une chaîne de caractère, on peut utiliser la méthode replace.
    Pour inverser une chaîne de caractère, on peut utiliser la syntaxe [::-1]
"""

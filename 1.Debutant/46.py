"""
Récupérer seulement les éléments pairs d'une liste avec une compréhension de liste
Nous avons une liste qui contient 50 nombres
 le but de cet exercice est de recuperer dans une seconde liste, la liste nombres_pairs,
 uniquement les nombres pairs de la premiere liste comme dans l'exemple precedent
 mais ici en utilisant une comprehension de liste.
"""

nombres = range(50)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

"""
    EXPLICATION
Dans cet exercice, nous récupérons les nombres pairs de la liste, toujours avec l'opérateur modulo, mais cette fois-ci
en utilisant une compréhension de liste, ce qui permet de faire tenir le code en une seule ligne.
La syntaxe de la compréhension de liste est assez simple :
    [expression for expression in liste if condition]

La compréhension de liste nous permet donc d'exécuter une boucle for sur une seule ligne :
    [i for i in nombres]

La compréhension de liste retourne une nouvelle liste, que l'on peut stocker dans une variable :
    nouvelle_liste = [i for i in nombres]

Pour finaliser cet exercice, il ne reste plus qu'à ajouter la condition qui permet de vérifier si un nombre est pair ou
 non dans la compréhension de liste :
    nouvelle_liste = [i for i in nombres if i % 2 == 0]

    POINTS IMPORTANTS À RETENIR
    Pour exécuter une boucle for sur une seule ligne et ainsi trier les éléments d'une liste, on utilise une
    compréhension de liste.
"""

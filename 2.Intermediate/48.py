"""
Remplacer un élément dans une liste
"""
liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

liste = [i.replace(nom_a_chercher, nouveau_nom) for i in liste]
print(liste)

"""
    EXPLICATION

On continue dans cet exercice avec les compréhensions de liste que vous devez commencer à maîtriser.

Encore une fois, on commence par boucler à travers chaque élément de la liste grâce à la compréhension de liste :

    liste = [x for x in liste]

En l'état, la compréhension de liste ci-dessus ne change absolument rien à la liste. Il faut donc utiliser la fonction replace pour remplacer le nom à chercher par le nouveau nom :

    liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]

Ainsi, directement en bouclant sur la liste, on remplace toutes les occurrences de 'Julie' par 'Julien'.

    POINTS IMPORTANTS À RETENIR

    Pour remplacer un mot par un autre, on utilise la fonction replace.
"""
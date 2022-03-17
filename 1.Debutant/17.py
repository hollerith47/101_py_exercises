"""
recuperer les elements dans une liste
 afficher
 1. le premier element de la liste
 2. le dernier element de la liste
 3. le deux premiers elements de la liste
 4. le deux derniers elements de la liste
 avec la fonction print
"""

ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])
print(ma_liste[-1])
print(ma_liste[:2])
print(ma_liste[-2:])


"""
EXPLICATION
Pour récupérer le premier élément, nous l'avons-vu précédemment, on utilise les crochets et l'indice 0.

Pour récupérer le dernier élément, peu importe la taille de la liste, on utilise l'indice -1 !

Pour récupérer les deux premiers éléments de la liste, on utilise une syntaxe un peu spéciale, qui se nomme 'slicing'.

En effet, plutôt que de spécifier un seul indice entre les crochets, on peut spécifier un indice de départ et un indice de fin.

Ainsi, pour récupérer les deux premiers éléments, on peut utiliser la syntaxe suivante :

ma_liste[0:2]

Et puisque nous commençons depuis le début de la liste, on n'a même pas besoin d'indiquer le 0 et Python comprendra qu'on
 veut commencer depuis le début de la liste, jusqu'au deuxième élément inclus :

ma_liste[:2]

Pour récupérer les deux derniers éléments, peu importe la taille de la liste, on utilise là encore un indice négatif et
toujours le même principe de 'slicing' :

ma_liste[-2:]

Encore une fois, pas besoin d'indiquer un indice après les deux points, on peut tout simplement laisser le deuxième indice
vide, et le slice ira jusqu'à la fin de la liste.

POINTS IMPORTANTS À RETENIR
Pour récupérer plusieurs éléments à l'intérieur d'une liste, on utilise le slicing : ma_liste[début:fin]
Pour récupérer des éléments en partant de la fin, on peut utiliser des indices négatifs.
"""
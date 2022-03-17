"""
l'objectif de l'exercice est de recuperer un element sur deux dans la liste
le script doit donc afficher la liste suivante avec la fonction print:
[1, 3, 5, 7, 9]
"""

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_liste =[]

for i in range(len(ma_liste)):
    if i % 2 == 0:
        new_liste.append(ma_liste[i])

print(new_liste)

# -------methode simple ----------------
print(ma_liste[::2])

"""
EXPLICATION

Encore une fois, nous utilisons ici le 'slicing' pour récupérer uniquement un élément sur deux dans notre liste.

Nous pouvons indiquer en effet un troisième nombre entre les crochets et ce nombre indique le pas avec lequel nous
voulons récupérer les éléments de notre liste.

Là encore, pas besoin d'indiquer d'indice spécifique pour les deux premiers nombres : en n'indiquant aucun indice, le
slicing commencera automatiquement au début de la liste, ira jusqu'à la fin, en prenant seulement un élément sur deux :

ma_liste[::2]
La syntaxe complète du slicing est donc la suivante :

ma_liste[indice_de_depart:indice_de_fin:pas]

Si on veut récupérer les éléments de 4 à 25 avec un pas de 3 on fera donc :

>>> ma_liste = range(100)
>>> ma_liste[4:26:3]
[4, 7, 10, 13, 16, 19, 22, 25]
POINTS IMPORTANTS À RETENIR

Pour récupérer un élément sur deux, on utilise le slicing et on indique un pas de 2 à l'intérieur des crochets.
"""

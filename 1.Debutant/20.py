liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
new_liste = []

# //////incorrect--------------------------------
for i in range(len(liste_01)):
    if liste_01[i] == liste_02[i] :
        new_liste.append(liste_01[i])
# print(new_liste)
# -------------------------------------------------
print()
# ---------------------------------------------------------
new_liste1 =[]

for el in liste_01:
    if el not in liste_02:
        continue
    new_liste1.append(el)
# print(new_liste1)

# ------meilleur solution------------------------------------------------
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]

sliste_01 = set(liste_01)
sliste_02 = set(liste_02)
print(sliste_01)
print(sliste_02)

intersect = sliste_01.intersection(sliste_02)
print(list(intersect))

"""
EXPLICATION

Dans cet exercice, nous passons par les sets pour récupérer les éléments communs à deux liste.
Pour convertir une liste en set, rien de plus facile, on utilise la fonction set :

sliste_01 = set(liste_01)

Une fois que nos deux listes sont converties en set, nous pouvons utiliser des méthodes pour récupérer
l'intersection, la différence et plein d'autres opérations du même style :

intersect = sliste_01.intersection(sliste_02)

Il ne nous reste plus qu'à re-convertir notre set résultant en liste avec la fonction list :
resultat = list(intersect)

POINTS IMPORTANTS À RETENIR

1. Pour convertir une liste en set, on utilise la fonction set.
2. Pour récupérer les éléments communs à deux set, on utilise la méthode intersection.
"""

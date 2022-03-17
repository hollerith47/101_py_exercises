"""
 Enlever les doublons d'une liste
"""

nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

# methode simple avec set
set_nombres = set(nombres)
print(list(set_nombres))
print()
# methode sans set
nombres_sans_repetition = []
for i in nombres:
    if i not in nombres_sans_repetition:
        nombres_sans_repetition.append(i)

print(nombres_sans_repetition)

"""
    EXPLICATION

Dans cet exercice, il fallait trouver une façon d'enlever les doublons d'une liste sans passer par les set.
Pour se faire, nous commençons par créer une liste vide, que nous allons remplir petit à petit par les nombres de la
liste initiale.

À chaque itération de la boucle, nous vérifions avec une structure conditionnelle, que le nombre courant sur lequel on
boucle  n'est pas déjà présent dans la liste avec la syntaxe if i not in liste  :

    for i in nombres:
        if i not in nombres_sans_duplicats:
            nombres_sans_duplicats.append(i)

Si le nombre n'est pas déjà présent dans la liste vide que nous avons initialisé, nous l'ajoutons alors à cette liste.

De cette façon, si on tombe une seconde fois sur le même nombre, la structure conditionnelle ne sera pas vérifiée et le
nombre ne sera pas ajouté une deuxième fois dans la liste.

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si un élément est déjà présent ou non dans une liste, on utilise la syntaxe i in liste. Si le nombre
    est déjà dans la liste, cette syntaxe retournera True, si non, False.
"""


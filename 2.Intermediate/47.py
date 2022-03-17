nombre = 209812
somme = []
for i in str(nombre):
    chiffres = int(i)
    somme.append(chiffres)
    
print(sum(somme))

"""
    SOLUTION

    nombre = 209812
    somme = sum([int(i) for i in str(nombre)])
    print(somme)

    EXPLICATION

Ici, nous utilisons une compréhension de liste pour additionner chaque chiffre du nombre 209812.

Premièrement, pour pouvoir boucler à travers chaque chiffre du nombre, on convertit notre nombre entier en chaîne de caractère :

    str(nombre)

Ce qui nous permet ensuite, à l'aide d'une compréhension de liste, de boucler à travers chaque chiffre :

    [int(i) for i in str(nombre)]

Au passage, nous convertissons chaque chiffre en nombre avec la fonction int.
En effet, vu que nous avons converti notre nombre en chaîne de caractère, les éléments sur lesquels nous bouclons
avec  la boucle for sont des nombres en chaîne de caractère. Pour pouvoir les additionner ensemble il faut donc les  
convertir en integer.

Pour finir, on utilise la fonction sum, pour faire la somme de tous les nombres contenus dans la liste :

    somme = sum([int(i) for i in str(nombre)])

    POINTS IMPORTANTS À RETENIR

    Pour boucler sur chaque chiffre d'un nombre, on convertit le nombre en chaîne de caractère.
    Pour additionner ensemble tous les nombres contenus dans une liste, on utilise la fonction sum.
"""
"""
Convertir une chaîne de caractère en camelCase
"""
phrase = "Phrase en camel case"
phrase_split = phrase.split()
phrase_final = [phrase_split.pop(0).lower()]

for mot in phrase_split:
    phrase_final.append(mot.capitalize())
# print(phrase_final)

print(''.join(phrase_final))

"""
    EXPLICATION

Le but de cet exercice était de convertir une phrase au format camelCase (première lettre en minuscule, toutes les
lettres suivante de chaque mot en majuscule).

Tout d'abord, nous commençons par séparer la phrase sur les espaces pour récupérer une liste contenant chaque mot :

    phrase = "Phrase en camel case"
    phrase_splits = phrase.split()

Si vous vous souvenez bien, nous pouvons utiliser la fonction split sans argument pour séparer une chaîne de caractère
sur les espaces (on pourrait aussi faire split(" ") pour splitter explicitement sur les espaces mais du coup c'est un
peu rébarbatif et inutile).

Dans un mot en camelCase, le premier mot est en minuscule, il faut donc récupérer ce premier mot et le convertir en
minuscule :

    resultat = [phrase_splits.pop(0).lower()]

Ci-dessus, nous récupérons le premier élément de la liste avec la méthode pop. Cette méthode, récupère l'élément indiqué
par l'indice entre parenthèse et enlève cet élément de la liste. Cela nous assure que le premier mot ne sera plus dans
la liste "phrase_splits" après l'opération.

Nous convertissons ensuite ce premier élément en minuscule avec la méthode lower.

Pour terminer, nous mettons ce résultat dans une liste grâce aux crochets.

La variable "resultat" contient donc maintenant le premier mot de la variable "phrase" en minuscule.

Ensuite, nous utilisons une boucle for pour passer à travers chaque mot restant dans la liste et les ajouter à la liste
"resultat" avec la première lettre en majuscule grâce à la méthode capitalize :

    for mot in phrase_splits:
        resultat.append(mot.capitalize())

À ce stade, nous avons donc une liste qui contient le premier mot de la phrase en minuscule et tous les autres mots, commençant par une majuscule.

Il ne reste donc plus qu'à joindre tous ces éléments ensemble grâce à la fonction join :

    resultat_formate = "".join(resultat)

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément dans une liste par son indice et l'enlever de cette même liste, on utilise la méthode pop.
    Pour convertir une chaîne de caractère en minuscule, on utilise la méthode lower.
    Pour convertir une chaîne de caractère en mot commençant par une majuscule, on utilise la méthode capitalize.
    Pour joindre ensemble tous les éléments d'une liste ensemble par un caractère, on utilise la méthode join.
"""

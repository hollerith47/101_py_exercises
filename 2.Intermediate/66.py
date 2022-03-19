"""
Trouver les nombres divisibles par 7 mais qui ne sont pas des multiples de 3
Le but de cet exercice est de trouver tous le nombres de 0 a 1000 qui sont divisibles par 7
mais qui ne sont pas des multiples de 3.
par exemple, le nombre 14 est divisible par 7 mais il n'est pas multiple de 3
car 14/3 ne retourne pas un nombre entier
"""
nombres = []

for i in range(1, 1001):
    if (i % 7 == 0) and (i % 3 != 0):
        nombres.append(i)
    
print(nombres)

"""
    EXPLICATION

Encore un exercice pour vous faire pratiquer le modulo.

Dans cet exercice, on cherche les nombres divisibles par 7, donc dont le reste de la division par 7 donne 0.
Nous cherchons également à savoir si ces même nombres ne sont pas des multiples de 3 (donc dont le reste de la
division  n'est pas égal à 0).

Nous allons donc encore une fois utiliser l'opérateur modulo pour vérifier ces deux conditions.

Tout d'abord, nous créons une liste "resultat" qui va contenir tous les nombres qui confirment les deux conditions.

On par donc dans une boucle sur une liste de nombres allant de 0 à 1000 :

    for i in range(0, 1001):

Ensuite, on teste les deux conditions : on utilise l'opérateur 'and' pour vérifier que les deux conditions soient
vraies.
Si une seule des deux conditions n'est pas respectée, le nombre ne sera pas ajouté. Les deux conditions testées sont :

    (i % 7 == 0)
    (i % 3 != 0)

La première testant si le nombre est divisible par 7 et la deuxième testant si le nombre n'est pas multiple de 3.

Si ces deux conditions sont vérifiées, on ajoute le nombre dans la liste :

    resultat.append(i)

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si plusieurs conditions sont vraies, on utilise l'opérateur "and".
    Pour récupérer le reste d'une division, on utilise l'opérateur modulo (%).
"""

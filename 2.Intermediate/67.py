"""
Calculer la factorielle d'un nombre
Dans cet exercice, nous cherchons la factorielle d'un nombre, dans ce cas-ci le nombre5
la factorellle de 5 est egale a 120 (car 1x2x3x4x5 = 120).
"""
nombre = 5
resultat = 1
for i in range(1, nombre+1):
    resultat *=i

print(resultat)

"""
    SOLUTION

    nombre = 5
    
    if nombre == 0:
        resultat = 1
    else:
        resultat = 1
        for i in range(1, nombre + 1):
            resultat *= i
     
    print(resultat)

    EXPLICATION
La factorielle d'un nombre n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n.
(Wikipedia).

Ici, nous voulons calculer la factorielle du nombre 5. Je vous avais demandé dans cet exercice de gérer le cas où le
nombre est égal à 0 (auquel cas la factorielle est égal à 1).

C'est ce que nous faisons avec la première condition :

    if nombre == 0:
        resultat = 1

Une fois ce cas spécifique géré, on continue avec tous les autres cas.

La première chose à faire, est de créer une liste qui contient tous les nombres entiers positifs inférieurs ou égaux
au nombre contenu dans la variable "nombre". Il ne reste plus ensuite qu'à multiplier la variable "resultat" par chacun des nombres contenu dans cette liste :

    for i in range(1, nombre + 1):
        resultat *= i

Avec la syntaxe *=, on multiplie contenu dans la variable resultat par i. En gros, cela revient au même de faire :

    for i in range(1, nombre + 1):
        resultat = resultat * i

La syntaxe *= est plus légère à utiliser et donc nous la préférons souvent à la version plus longue. Notez que vous
pouvez effectuer ce genre d'opération avec n'importe quel opérateur mathématique. Ainsi, pour additionner ou
soustraire un nombre à une variable, on peut utiliser les syntaxe += et -=.

Ainsi, nous allons multiplier 1 par 2, puis le résultat de cette opération par 3, puis 4 etc, jusqu'à la valeur
contenue dans le nombre n, ce qui revient au même que l'opération utilisée pour calculer la factorielle de 5 :

1 x 2 x 3 x 4 x 5 = 120

    POINTS IMPORTANTS À RETENIR

    Pour rapidement multiplier une variable par un nombre, on peut utiliser la syntaxe *=

"""

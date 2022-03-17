"""
Afficher la table de multiplication d'un nombre
on continue avec la bouche for, cette fois-ci pour afficher la table de multiplication
d'un nombre.
"""
nombre = 7

for i in range(11):
    print(f"{i} x {nombre} = {i * nombre}")

"""
    XPLICATION

Ici, nous faisons tous les calculs nécessaires directement à l'intérieur de la méthode format.

Pour commencer, nous bouclons à travers une liste contenant les nombres de 0 à 10, grâce à la fonction range :

    for i in range(11):

Nous affichons ensuite dans la chaîne de caractère formattée, le nombre courant de la boucle, contenu dans la
variable i,  le nombre pour lequel nous affichons la table de multiplication, contenu dans la variable nombre,
puis la  multiplication de l'un par l'autre (i * nombre).

    POINTS IMPORTANTS À RETENIR

    Il est possible de faire des opérations mathématiques directement à l'intérieur de la méthode format,
    afin d'insérer le résultat de ces opérations à l'intérieur d'une chaîne de caractère.
"""
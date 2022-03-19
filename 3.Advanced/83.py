"""
 Recréer la méthode isdigit
"""


# ma methode
def isdigit(nombre):
    try:
        if int(nombre) is not None:
            return True
    except ValueError:
        return False


print(isdigit("1854274"))


# autre methode longue et complexe
def isdigit(variable):
    for i in variable:
        if i not in [str(n) for n in range(10)]:
            return False
    
    return True


"""
    EXPLICATION

Dans cet exercice, on continue avec la création de fonctions et méthodes disponibles de base dans Python.
Dans cet exercice, nous créons une fonction isdigit qui imite le comportement de la méthode isdigit, qui permet de
vérifier si une chaîne de caractère est composée uniquement de chiffres.

La première chose à faire était donc logiquement de créer une fonction isdigit qui accepte une variable en argument :

    def isdigit(variable):

Jusque là, rien de bien compliqué.

Ensuite, il faut que nous vérifions chaque caractère de la chaîne de caractère qui nous est passée en argument afin de
savoir si c'est un chiffre ou non.
Généralement pour vérifier si une chaîne de caractère est un nombre, on utilise la méthode isdigit. Ici, interdit de
l'utiliser, il va donc falloir faire autrement.

Comment vérifier si une chaîne de caractère correspond à un chiffre ?
Facile, il suffit de vérifier s'il est égal à 0, 1, 2, 3, 4, 5, 6, 7, 8, ou 9. Si c'est le cas, alors la chaîne de
caractère est bien un chiffre.

Il nous faut donc créer une liste qui contient tous les chiffres de 0 à 9, ce que nous faisons avec la compréhension de
liste suivante :

    [str(n) for n in range(10)]

Nous convertissons directement chaque chiffre "n" récupéré dans la boucle en chaîne de caractère avec la fonction str,
car dans notre boucle for, la variable i que nous récupérons est une chaîne de caractère.

La compréhension de liste ci-dessus nous retourne donc une liste de tous les chiffres de 0 à 9 en chaîne de caractère :

    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

Pour vérifier si la chaîne de caractère récupérée dans la variable "i" dans notre boucle for appartient ou non à cette
liste, on utilise une structure conditionnelle et la condition "in" :

    if i not in [str(n) for n in range(10)]:

Ici, nous utilisons "not in" car si la variable "i" n'est pas présente dans notre liste, alors cela veut dire que la
chaîne de caractère passée à notre fonction contient un caractère qui n'est pas égal à un chiffre.

Pas besoin d'aller plus loin donc et de passer en revue tous les caractères restants, nous pouvons arrêter la fonction
directement à ce stade et retourner False.

Si nous finissons la boucle for sans jamais avoir vérifié cette condition, cela signifie que nous n'avons rencontré
aucun caractère dans notre variable qui n'était pas un chiffre : notre variable ne contient donc que des chiffres et
nous pouvons retourner True.

    POINTS IMPORTANTS À RETENIR

    Pour créer rapidement et efficacement des listes, on peut utiliser des compréhensions de liste et la fonction range.
    Pour vérifier si une variable est présente ou non dans une liste, on utilise "in" dans une condition :
    if variable in liste. La condition retournera True si la variable est présente dans la liste et False dans le cas
    contraire.
"""

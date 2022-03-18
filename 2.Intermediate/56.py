"""
Formater un texte avec la méthode format
"""
texte = "Bonjour Udemy"
taille = len(texte)

debut_fin_horizontal = '-'
debut_fin_vertical = '|'
print(debut_fin_horizontal * taille)

for lettre in texte:
    print(f"{debut_fin_vertical}{lettre:^{taille -2}}{debut_fin_vertical}")

print(debut_fin_horizontal * taille)

"""
    EXPLICATION

Beaucoup de lignes de codes qui ne font pas forcément de sens à prime abord dans cet exercice, nous allons donc pas à
pas expliquer la logique derrière cette solution.

Tout d'abord, nous déclarons un certain nombre de variables : le texte à afficher, la longueur du texte (dans la
variable longueur) et les deux symboles que nous allons utiliser (symbole1 et symbole2).
Nous commençons ensuite par afficher le premier symbole, multiplié par la longueur de la chaîne de caractères :

    >>> print(symbole1 * longueur)
    -------------

Nous passons ensuite avec une boucle for à travers chaque lettre du mot :
    for lettre in texte:

Vient ensuite, la partie un peu plus complexe de l'exercice. Nous utilisons toute la puissance des f-string avec la
syntaxe suivante :

    print(f"{symbol2}{lettre:^{size-2}}{symbol2}")

Tout d'abord, nous définissons deux balises avec les accolades au début et à la fin de la chaîne de caractères pour
insérer la variable symbol2.
Cela nous permet d'afficher le 2e symbole au début et à la fin.
Puis, nous utilisons la syntaxe suivante :

    {lettre:^{size - 2}}

On indique vouloir insérer l'objet contenu dans la variable lettre (donc la lettre sur laquelle on boucle).

Ensuite, avec les deux points et l'accent circonflexe, on signifie que l'on veut ajouter un 'padding' avant et après
cette lettre : en gros, python va ajouter autant d'espaces que nécessaire avant et après la variable que l'on insère
dans l'accolade, afin que le nombre total de caractère soit égal au nombre passé.

Ce nombre, c'est size - 2, donc la longueur du texte, moins les 2 symboles que l'on place au début et à la fin de la
chaîne de caractères :

    >>> print(f"{symbol2}{lettre:^{size - 2}}{symbol2}")
    |     B     |

Ainsi, on s'assure que la longueur totale de la ligne, soit égale à la longueur de la première ligne qui elle ne
contient pas la lettre sur laquelle on boucle.
Puis on termine notre script par le même print que pour afficher la première ligne, afin de refermer notre boîte :

    print(symbole1 * longueur)

    POINTS IMPORTANTS À RETENIR
    Pour faire en sorte qu'une chaîne de caractères occupe un nombre précis de caractères, vous pouvez la 'padder' avec
    des espaces, en utilisant l'accent circonflexe à l'intérieur de votre f-string.
"""

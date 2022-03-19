"""
Vérifier si une phrase est un pangramme
"""
import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
alphabet = list(string.ascii_lowercase)
# print(alphabet)

for letter in phrase.lower():
    if letter in alphabet:
        alphabet.remove(letter)

# print(bool(not alphabet))
if not alphabet:
    print("La phrase est un pangramme")
else:
    print("La phrase n'est pas un pangramme")
    
"""
    EXPLICATION

On continue dans les mots bizarres avec cette fois-ci un exercice pour vérifier si une phrase est un pangramme.
Un pangramme est une phrase qui contient toutes les lettres de l'alphabet.

La phrase que nous allons vérifier est la suivante et est un pangramme :

    phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"

Là encore, nous commençons par convertir la phrase en minuscule avec la méthode lower.

Nous récupérons grâce au module string toutes les lettres de l'alphabet que nous mettons dans une liste avec la
fonction list :

    alphabet = list(string.ascii_lowercase)

La logique ensuite est de passer à travers chaque lettre de notre phrase avec une boucle for...

    for l in phrase_lower:

...pour vérifier si la lettre courante est contenue dans notre liste "alphabet"...

    if l in alphabet:

...et si c'est le cas, nous enlevons cette lettre de notre liste "alphabet" :

    alphabet.remove(l)

Il ne nous reste plus à la fin qu'à vérifier si notre liste alphabet est vide ou non. Si la liste est vide, c'est donc
que notre phrase contenait toutes les lettres de l'alphabet. Si il reste au moins une lettre dans la liste, alors la
phrase n'est pas vide est donc n'est pas un pangramme.

Pour vérifier si une liste est vide, pas besoin de s'embêter avec la fonction len : une liste vide est évaluée comme
False, on peut donc vérifier facilement avec une structure conditionnelle si la liste est vide ou non :

    if alphabet:
        print("La phrase n'est pas un Pangramme")
    else:
        print("La phrase est un Pangramme")

    POINTS IMPORTANTS À RETENIR

    Pour récupérer toutes les lettres de l'alphabet, on utilise le module string et la constante "ascii_lowercase".

    Pour enlever un élément d'une liste, on utilise la méthode remove.

    Une liste vide est évaluée comme False.


"""

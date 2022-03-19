"""
Compter le nombre d'occurrence d'un mot dans un texte
"""
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

lorem = lorem.replace('.', '').replace(',', '').lower()
lorem_en_liste = lorem.split()
mot = 'elit'
print(lorem_en_liste.count(mot))

"""
    EXPLICATION

Exercice assez simple dans lequel il fallait juste prendre quelques précautions.
Le but de l'exercice était de compter le nombre d'occurence du mot "elit" dans le texte contenu dans la variable
"lorem".

Peut-être avez-vous directement essayé d'utiliser la fonction count et cela ne fonctionnait pas.
Il fallait en effet quelque peut formater au préalable la chaîne de caractère.

Tout d'abord nous nous débarrassons de tous les signes de ponctuation, à savoir les virgules et les points, avec la
méthode replace :

    lorem = lorem.replace(",", "").replace(".", "")

Pour réaliser cette opération en une seule ligne, nous n'hésitons pas à chaîner les méthodes replace l'une à la suite
de l'autre.

Puisque notre script ne tiens pas compte de la casse, nous convertissons ensuite notre chaîne de caractère entièrement
en minuscules :

    lorem = lorem.lower()

Il ne nous reste plus qu'à séparer les mots les uns des autres avec la méthode split :

    lorem_split = lorem.split()

Vous remarquerez que nous ne passons aucun caractère à la méthode split : en effet, par défaut la méthode split va
séparer la chaîne de caractère sur les espaces si elle ne reçoit aucun argument.

Il ne nous reste pour finir plus qu'à utiliser la méthode count sur notre liste "lorem_split" pour compter le nombre
d'occurrence du mot "elit" dans notre liste de mots :

    print(lorem_split.count(mot))

    POINTS IMPORTANTS À RETENIR

    Pour remplacer un caractère par un autre, ou l'effacer, on utilise la fonction replace.
    Pour convertir une chaîne de caractère en minuscule, on utilise la fonction lower.
    Pour séparer une chaîne de caractère sur les espaces, on utilise la fonction split.
    Pour compter le nombre d'occurrence d'un élément dans une liste, on utilise la fonction count.
"""

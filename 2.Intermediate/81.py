"""
Compter le nombre de phrases dans un texte
"""
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(lorem.count("."))

"""
    EXPLICATION

Un problème en apparence complexe pour une solution très simple. Comment compter le nombre de phrases dans un texte ?
Aucunement besoin de boucle ou autre structure complexe pour se faire.
Il suffit de se demander ce qui définit une phrase : tout simplement un point.

Il nous suffit donc de compter le nombre de points dans le texte pour compter le nombre de phrase.
Nous utilisons donc la méthode 'count' sur notre chaîne de caractère pour compter le nombre de points :

    lorem.count(".")

    POINTS IMPORTANTS À RETENIR
    Pour compter le nombre de fois qu'un caractère apparaît dans une chaîne de caractère, on utilise la méthode 'count'.
"""

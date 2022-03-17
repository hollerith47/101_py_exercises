"""
Récupérer l'indice de l'itération dans une boucle
les boucles for, encore et toujours, avec cette fois-ci, un exercice dans lequel nous
allons recuperer a la fois l'indice et l'element sur lequel nous bouclons dans chaque
iteration de la boucle for.
liste = ["Pierre", "Paul", "Marie"]
Votre script doit donc retourner dans ce cas-ci:
    0 pierre
    1 Paul
    2 Marie
"""
liste = ["Pierre", "Paul", "Marie"]

# solution du debutant
for i in range(len(liste)):
    print(f'{i} {liste[i]}')

# meilleure solution
for i, nom in enumerate(liste):
    print(i, nom)


"""
    SOLUTION

    liste = ["Pierre", "Paul", "Marie"]
    for i, nom in enumerate(liste):
        print(i, nom)

    EXPLICATION

Pour récupérer un élément dans une liste ainsi que son indice dans une boucle for, une erreur souvent faite par les
débutants, est de passer par la fonction range et la fonction len, ce qui alourdit le code et le rend difficilement
lisible :

    for i in range(len(liste)):
        print(i, liste[i]))

Pour récupérer dans une boucle for à la fois l'élément sur lequel on boucle ainsi que son indice, on préfère utiliser la
fonction enumerate :

    for i, nom in enumerate(liste):
        print(i, nom)

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément et son indice dans une boucle for, on utilise la fonction enumerate.
"""

    
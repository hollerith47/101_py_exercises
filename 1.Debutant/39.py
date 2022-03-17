"""
Sortir d'une boucle infinie
Nous sommes en presence d'une boucle while infinie! En l'etat actuel, le
script ne s'arretera jamais et la phrase 'Exercice reussi !' ne s'affichera jamais
"""
i = 0

while i < 10:
    pass
    i += 1  # solution condition manquante

print("Exercice réussi !")

"""
    SOLUTION

    i = 0
    
    while i < 10:
        pass
        i += 1
     
    print("Exercice réussi !")

    EXPLICATION
Une erreur courante que font beaucoup de débutants est de créer une boucle infinie.

La boucle while, bien que très pratique, est également assez dangereuse à manipuler pour qui ne fait pas attention à la
condition de sortie.

C'était le cas dans cet exercice, dans lequel la variable i n'était jamais incrémentée et donc toujours plus petite
que 10.

Il fallait donc incrémenter la valeur de i pour pouvoir arriver à un moment dans le script où i soit plus grand que 10
et que la condition du while soit fausse.

Peu importe la boucle while que vous comptez faire, je vous conseille toujours de vous prévoir une porte de sortie de ce
genre : incrémentez une variable à chaque itération de la boucle et sortez de la boucle une fois que la variable atteint
un nombre trop élevé, afin d'éviter de faire planter votre script si votre condition initiale n'est jamais fausse.

    POINTS IMPORTANTS À RETENIR
    Pour incrémenter un nombre entier, on utilise la syntaxe variable += 1.
"""

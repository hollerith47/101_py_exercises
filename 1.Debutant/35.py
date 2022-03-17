"""
Dans cet exercice, nous voulons tronquer le nombre de decimales contenues apres
la virgule dans la variable nombre, par le nombre contenu dans la variables
decimales.
Votre script doit donc afficher: "nombre tronqué : 2938.489".
"""


nombre = 2938.48872
decimales = 3

print(f"Nombre tronqué: {nombre:.{decimales}f}")
print(f"Nombre tronqué: {nombre} ")

"""
    SOLUTION

    nombre = 2938.48872
    decimales = 3
    
    print(f"Nombre tronqué: {nombre:.{decimales}f}")
    
    # Avec la méthode format
    print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))

    EXPLICATION

Dans cet exercice, nous continuons d'explorer les possibilités des f-string qui cachent de nombreuses fonctionnalités
assez avancées.

En effet, il est possible d'utiliser la syntaxe suivante pour tronquer le nombre de décimales après la virgule d'un
nombre :

{nombre:.3f}

nombre correspond ici à la variable définit au début du script.

Nous avons ensuite deux points, un point et un nombre qui détermine le nombre de décimales après la virgule que l'on
souhaite conserver (ici 3) et pour finir la lettre f.

Je l'avoue, ce n'est pas la syntaxe la plus facile à retenir, mais c'est vraiment très efficace pour pouvoir rapidement
afficher un nombre tronqué dans une chaîne de caractères.

    SOLUTION ALTERNATIVE

Vous pouvez également utiliser la fonction round afin de tronquer le nombre de décimales :

    nombre = 2938.48872
    decimales = 3
    
    solution = round(nombre, decimales)
    
    print(f"Nombre tronqué: {solution}")

    POINTS IMPORTANTS À RETENIR
    On peut tronquer directement un nombre pour n'afficher qu'une certaine partie des décimales après la virgule grâce
    aux f-string et la syntaxe {nombre:.3f}.
"""

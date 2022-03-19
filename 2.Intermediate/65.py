"""
Trouvez tous les diviseurs d'un nombre
dans cet exercice, nous cherchons tous le diviseurs d'un nombre, dans ce cas-ci
le nombre 50
les diviseurs du nombre 50 correspondent a tous les nombres par lesquels on peut
diviser 50 sans qu'il n'y ait de reste a la division
"""
nombre = 50
diviseurs = []

for i in range(1, nombre+1):
    if nombre % i == 0:
        diviseurs.append(i)

print(diviseurs)

"""
    EXPLICATION

Le but de cet exercice était de trouver tous les diviseurs du nombre contenu dans la variable 'nombre'.

La première étape était donc de créer une liste de nombres qui contient tous les nombres de 1 au nombre contenu dans
la variable 'nombre' (ici, 50) :

    liste_nombres = list(range(1, nombre+1))

On crée ensuite une liste vide qui va nous permettre de stocker les nombres qui sont des diviseurs de 50.

On commence ensuite une boucle à travers notre liste de nombres. Grâce à l'opérateur modulo, on récupère le reste de
la  division.
Si le reste est égal à 0, alors le nombre courant, contenu dans la variable i, est un diviseur du nombre 50. Nous
l'ajoutons donc à notre liste 'diviseurs' :

    for i in liste_nombres:
        if nombre % i == 0:
            diviseurs.append(i)

Et voilà, un exercice assez simple en somme, mais qui faisait appel à l'opérateur modulo dont beaucoup de gens
oublient  souvent l'existence.
Je suis sur qu'une petite piqûre de rappel avec cet exercice ne vous a donc pas fait de mal ;)

    POINTS IMPORTANTS À RETENIR

    Pour récupérer le reste de la division d'un nombre par un autre, on utilise l'opérateur modulo (%).
"""

"""
 Récupérer seulement les éléments pairs d'une liste
 Nous avons une liste qui contient 50 nombres
 le but de cet exercice est de recuperer dans une seconde liste, la liste nombres_pairs,
 uniquement les nombres pairs de la premiere liste
"""
nombres = range(50)
nombres_pairs = []

for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)

print(nombres_pairs)

"""
    EXPLICATION

Pour résoudre cet exercice, il fallait faire appel à un opérateur mathématique quelque peu méconnu : l'opérateur modulo.
Cet opérateur est un peu l'alter égo de l'opérateur division, puisqu'il nous permet de récupérer le reste de la division
d'un nombre par un autre.

Par exemple, 10 % 2 retournera 0, car 10 / 2 est égal à 5 et la division ne laisse aucun reste.

Par contre, 11 % 2 retournera 1, car 11 / 2 est égal à 5 et il reste 1.

Le modulo est donc un opérateur mathématique très utilisé pour vérifier si un nombre est pair ou non.
En effet, un nombre divisible par 2 et ne laissant aucun reste, est pair.

On utilise donc le modulo dans cet exercice pour tester chaque élément de la liste dans une boucle for en vérifiant si
le modulo du nombre par 2 est égal ou non à 0 :

    for i in nombres:
        if i % 2 == 0:
            nombres_pairs.append(i)

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si un nombre est pair, on utilise l'opérateur mathématique modulo, en vérifiant si le modulo de notre
    nombre par 2 est égal ou non à 0.
"""

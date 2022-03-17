"""
Ajouter des éléments à un dictionnaire

"""

employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

n = 1
for element in liste:
    if not str(element).isdigit():
        employes[f"id-0{n}"] = element
        n += 1
    
print(employes)

# meilleur solution
i = 1

for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1
print(employes)

"""
    EXPLICATION

Pour cet exercice, nous avons du ruser un peu. Peut-être avez-vous commencé par utiliser la fonction enumerate pour
récupérer directement l'indice et l'élément sur lequel on boucle ? Le problème est qu'ici, certains éléments ne sont pas
valides et sont donc ignorés. Ainsi, pour garder un id d'employé continue, nous ne pouvons pas utiliser l'indice de
l'élément sur lequel on boucle.

C'est la raison d'être de la variable i que nous initialisons à 1 avant de passer dans la boucle et que nous
incrémentons chaque fois qu'un employé valide est détecté.

Pour détecter si un élément de la liste ne contient que des nombres, on utilise la fonction isdigit :

    if not str(element).isdigit():

Pour formatter la clé dans le dictionnaire, on utilise la fonction format :

    employes["id-{:02d}".format(i)] = element

La syntaxe :02d permet d'indiquer que nous souhaitons formater le nombre i pour qu'il contienne toujours 2 chiffres : 1
deviendra 01, 2 deviendra 02, 15 restera tel quel etc.

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si une chaîne de caractère ne contient que des nombres, on utilise la fonction isdigit.

    Pour formater un nombre pour qu'il contienne toujours 2 chiffres, on utilise la syntaxe 02d à l'intérieur
    d'accolades utilisées pour la fonction format.
"""

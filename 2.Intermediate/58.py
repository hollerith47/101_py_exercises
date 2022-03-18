"""
Calculer l'année de naissance à partir d'un âge donné
"""
from datetime import datetime

age = 25
mois_de_naissance = 5

yearNow = datetime.today().year
moisNow = datetime.today().month

annee_actuelle = datetime.today().year
mois_actuel = datetime.today().month

if mois_de_naissance > moisNow:
    result = yearNow - age - 1
else:
    result = yearNow - age
# les lignes 12-15 peuvent se resumer en une seule ligne
resultat = annee_actuelle - age - (1 if mois_de_naissance > mois_actuel else 0)
print(result)
print(resultat)

"""
    EXPLICATION

Dans cet exercice, nous utilisons la classe datetime du module datetime pour faire des calculs de date.
On commence tout d'abord par récupérer l'année actuelle avec :

    annee_actuelle = datetime.today().year

Puis le mois actuel de la même façon :

    mois_actuel = datetime.today().month

On fait ensuite une soustraction entre l'année actuelle et l'âge de la personne contenu dans la variable 'age'.
On fait une dernière petite vérification dans un opérateur ternaire pour vérifier si le mois de naissance de la
personne en question est plus grand que le mois actuel ou non. Si oui, on retire une année supplémentaire à l'année de naissance, si non, on ne retire rien de plus (else 0).

    POINTS IMPORTANTS À RETENIR

    Pour récupérer l'année actuelle, on utilise datetime.today().year
    Pour récupérer le mois actuel, on utilise datetime.today().month
"""
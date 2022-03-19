"""
Calculer le nombre de jours entre deux dates
Dans cet exercice, nous allons calculer le nombre de jours entre deux dates.
la date de depart que nous allons utiliser est le 2 juillet 2014 et la date de fin
le 11 juillet 2018.
le nombre de jours entre ces deux dates est 1470.
a vous de trouver le code qui permet de calculer automatiquement le nombre de jours entre ces
deux dates, grace au module datetime.
"""
from datetime import date

date_1 = date(2014, 7, 2)
date_2 = date(2018, 7, 11)

nombre_jours = abs(date_1 - date_2).days

print(nombre_jours)

# mes jours sur terre
my_birth = date(1996, 11, 17)
today = date.today()
nombre_jours_my_birth = abs(my_birth - today).days

print(f"Herman Makiese est né il y a de cela {nombre_jours_my_birth} jours")

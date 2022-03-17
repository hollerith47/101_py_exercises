"""

"""
mot = "Python"

# for i in range(mot): il manque la fonction len
for i in range(len(mot)):
	print(i)
	
"""
EXPLICATION

La fonction range a besoin d'un nombre pour créer une liste de nombres de la longueur du nombre passé en argument.
Ici dans le script, nous passions directement la variable mot - qui est une chaîne de caractère - à la fonction range,
ce qui nous retournait logiquement une erreur.

À la place, il fallait utiliser la fonction len pour calculer la longueur de la chaîne de caractère et ainsi passer ce
nombre à la fonction range pour pouvoir itérer sur la liste obtenue.

POINTS IMPORTANTS À RETENIR
Pour calculer la longueur d'une chaîne de caractère, on utilise la fonction len.
"""

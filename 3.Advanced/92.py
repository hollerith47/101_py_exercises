"""
Créer une fonction pour récupérer la valeur d'un dictionnaire
"""


def getValue(dictionnaire, *args):
    args = list(args)
    default = args.pop(-1)
    
    for arg in args:
        dictionnaire = dictionnaire.get(arg)
        if not dictionnaire:
            return default
    
    return dictionnaire


d = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
# a = getValue(d, "02", "identite", "nom", "valeur inconnue")
a = getValue(d, "01", "identite", "prenom", "valeur inconnue")
print(a)

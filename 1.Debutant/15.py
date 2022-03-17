"""
ici nous cherchons a compter le nombre de fois que la lettre o apparait dans la
phrase.
"""

lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
nombre = phrase.count(lettre_a_chercher)

print(nombre)

# autre solution
print(phrase.lower().count(lettre_a_chercher))

"""
EXPLICATION
Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.

Afin d'éviter toute confusion quant aux majuscules et minuscules, nous prenons le soin de convertir auparavant notre
chaîne de caractère en minuscule avec la fonction lower.

POINTS IMPORTANTS À RETENIR
Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.
Pour convertir une chaîne de caractère en minuscule, on utilise la fonction lower.
"""
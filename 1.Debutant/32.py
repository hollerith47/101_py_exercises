"""
formatage de chaine de caractere avec concatenation du prenom et nom
"""

prenom = "Pierre"
nom = "Dupont"

print("Bonjour je m'appelle {} {}".format(prenom, nom))

# 2e methode ----------------------------------------------
print(f"Bonjour je m'appelle {prenom} {nom}")

# Solution alternative avec la méthode format
print("Bonjour je m'appelle {prenom} {nom}".format(prenom=prenom, nom=nom))

"""
EXPLICATION
Il est possible de réussir cet exercice sans utiliser les f-string ou la fonction format, en concaténant des chaînes de
caractères avec l'opérateur +.

Il est cependant plus facile d'utiliser les f-string pour insérer des éléments à l'intérieur d'une chaîne de caractères.

Pour définir une chaîne de caractères comme une f-string, il suffit de précéder le premier guillemet de la lettre f :
f"Bonjour je m'appelle"

On peut ensuite insérer des variables à l'intérieur de la chaîne grâce aux accolades :
f"Bonjour je m'appelle {prenom} {nom}"

POINTS IMPORTANTS À RETENIR
Pour concaténer des chaînes de caractères, on peut utiliser une f-string, pour insérer directement à l'intérieur de la
chaîne des variables grâce aux accolades.
"""
"""
Créer une classe personnalisée pour une chaîne de caractère
"""


class SuperChaine(object):
    def __init__(self, mot):
        self.mot = mot
    
    def majuscule(self):
        return self.mot.upper()
    
    def minuscule(self):
        return self.mot.lower()
    
    def titre(self):
        return self.mot.capitalize()


chaine = SuperChaine("UdeMy")
print(chaine.majuscule())
print(chaine.minuscule())
print(chaine.titre())

"""
    EXPLICATION

Le but de cet exercice était de créer une classe personnalisée pour gérer les chaînes de caractère.
Nous devions ré-implémenter trois méthodes : upper, lower et capitalize.
Pour commencer, nous implémentons la méthode __init__, qui accepte un paramètre "texte" que nous récupérons par la suite
dans la variable texte :

    class SuperChaine(object):
        def __init__(self, texte):
            self.texte = texte

Cela nous permettra de modifier cette variable texte dans les méthodes que nous allons maintenant créer.
Nous créons donc 3 méthodes : majuscule (pour upper), minuscule (pour lower) et titre (pour capitalize).
Dans chaque méthode, nous retournons la variable texte en majuscule, en minuscule et avec une majuscule :

    def majuscule(self):
        return self.texte.upper()
     
    def minuscule(self):
        return self.texte.lower()
     
    def titre(self):
        return self.texte.capitalize()

Rien de bien compliqué ici, nous faisons juste ré-implémenter ces méthodes, avec un nom français, ce qui nous permet
donc d'utiliser ensuite notre classe de la façon suivante :

    chaine = SuperChaine("udemy")
    print(chaine.majuscule())
    print(chaine.minuscule())
    print(chaine.titre())

La seule chose à ne pas oublier dans toutes ces méthodes est de placer comme premier paramètre le mot self, qui
correspond à l'instance de la classe.

    POINTS IMPORTANTS À RETENIR

    Pour initialiser une classe, on utilise la méthode __init__.
    Une méthode est une fonction appartenant à une classe.
"""

"""
Créer une classe pour gérer des voitures
"""


class Voiture():
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur


super_voiture = Voiture("Lamborghini", 150000, "rouge")
print(super_voiture.marque)
print(super_voiture.prix)
print(super_voiture.couleur)

"""
    EXPLICATION

On passe avec ces exercices dans des sujets un peu plus complexes de Python avec les classes. Cet exercice était
cependant encore très simple pour qui maîtrise l'orienté objet.
Le but de cet exercice était de créer une classe qui contient trois attributs : la marque, le prix et la couleur de la
voiture.

Il suffisait donc de créer la méthode __init__, qui contient trois paramètres (sans compter "self") :

    class Voiture(object):
        def __init__(self, marque, prix, couleur):

Nous créons ensuite 3 variables (marque, prix et couleur), appartenant à la classe, à partir des arguments passés à la
fonction __init__ lors de l'instanciation de la classe :

    class Voiture(object):
        def __init__(self, marque, prix, couleur):
    	self.marque = marque
    	self.prix = prix
    	self.couleur = couleur

Nous pouvons donc ensuite créer une instance de notre classe en passant respectivement la marque, le prix et la couleur
de la voiture à la classe :

    super_voiture = Voiture("Lamborghini", 150000, "rouge")

    POINTS IMPORTANTS À RETENIR
    La méthode "magique" appelée lors de l'instanciation d'une classe est la méthode __init__
"""

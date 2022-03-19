"""
 Modifier la représentation d'une classe
"""


class Voiture(object):
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur
    
    def __repr__(self):
        return f"Votre voiture est une {self.marque.capitalize()} {self.couleur} et coûte {self.prix}$"


super_voiture = Voiture("lamborghini", 150000, "rouge")
print(super_voiture)

"""
    class Voiture(object):
        def __init__(self, marque, prix, couleur):
    	self.marque = marque
    	self.prix = prix
    	self.couleur = couleur
     
        def __repr__(self):
    	    return "Votre voiture est une {} {} et coûte {}$".format(self.marque.capitalize(), self.couleur, self.prix)
     
     
    super_voiture = Voiture("lamborghini", 150000, "rouge")
    print(super_voiture)

    EXPLICATION

Encore une fois un exercice assez simple pour qui maîtrise l'orienté objet, mais qui aborde tout de même des notions
moins connus du "grand public".

Ici, il fallait modifier la représentation de la classe Voiture, c'est à dire ce qui nous est retourné lorsque l'on
print une instance créé à partir de la classe Voiture.

Il fallait pour ce faire ré-implémenter la méthode spécial __repr__ :

    def __repr__(self):
        return "Votre voiture est une {} {} et coûte {}$".format(self.marque.capitalize(), self.couleur, self.prix)

Nous utilisons la méthode format ainsi que les attributs marque, couleur et prix de la classe pour afficher les
informations de l'instance de notre Voiture.

    POINTS IMPORTANTS À RETENIR
    Pour modifier la représentation d'une classe, on utilise la méthode spéciale __repr__.

"""

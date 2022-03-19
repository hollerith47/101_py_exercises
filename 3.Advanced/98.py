"""
Ajouter une propriété à la classe Voiture
"""


class Voiture(object):
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur
    
    @classmethod
    def lamborghini(cls):
        return cls("Lamborghini", 150000, "rouge")

    @classmethod
    def porsche(cls):
        return cls("Porsche", 200000, "noir")
    
    @property
    def prix_euros(self):
        prix_euros = self.prix * 1.5
        return round(prix_euros)


lamborghini = Voiture.lamborghini()
print(lamborghini.prix)
print(lamborghini.prix_euros)
print()
porsche = Voiture.porsche()
print(porsche.prix)
print(porsche.prix_euros)

"""
    EXPLICATION

Le but de cet exercice était de créer une propriété qui nous permette facilement d'accéder au prix de la voiture
converti en euro (par rapport à un prix de base en dollars).

Une propriété nous permet d'éviter de passer par des méthodes "getter" et "setter" (méthodes qui vont nous permettre de
modifier et récupérer la valeur d'un attribut).
Dans ce cas-ci, nous n'avons pas de propriété "setter", juste une propriété qui nous permet de récupérer un attribut
modifié de notre classe.

Pour définir une méthode comme une propriété, on utilise le décorateur @property :

    @property
    def prix_euros(self):

À l'intérieur de cette méthode, nous retournons tout simplement le prix original multiplié par 1.5 et arrondit avec la
fonction round pour faire la conversion en euros :

    prix_euros = self.prix * 1.5
    return round(prix_euros)

Cela nous permet donc d'accéder au prix en euros de la voiture de la façon suivante :

    print(lamborghini.prix_euros)

Vous remarquez donc que nous n'avons pas besoin d'utiliser les parenthèses après le nom de la méthode, contrairement à
une méthode classique du type :

    print(lamborghini.recuperer_prix_euros())

C'est un des avantages des propriétés, nous pouvons ainsi récupérer une valeur comme si c'était un attribut de notre
classe, alors qu'en arrière plan, nous faisons plusieurs opérations successives (multiplication et arrondit avec la
fonction int) pour convertir le prix de base en euros.

    POINTS IMPORTANTS À RETENIR

    Pour spécifier qu'une méthode doit être interprétée comme une propriété, on utilise le décorateur @property.

    Pour récupérer la valeur d'une propriété, on utilise tout simplement le nom de la méthode définie comme une
    propriété, sans les parenthèses.
    Pour arrondir un nombre, on utilise la fonction round.
"""

"""
Créer une classe qui hérite d'une autre
"""


class Voiture(object):
    def __init__(self):
        self.couleur = "noire"
        self.vitesse_max = 200
        self.prix = 25000
    
    def __repr__(self):
        return "Je suis une voiture normale"
    
    @property
    def prix_reduit(self):
        return self.prix * 0.75


class Lamborghini(Voiture):
    def __init__(self):
        super().__init__()
        self.vitesse_max = 300
        # self.prix = 100000
    
    def __repr__(self):
        return "Je suis une voiture de luxe"


ma_voiture = Lamborghini()
print(ma_voiture.couleur)
print(ma_voiture.vitesse_max)
print(ma_voiture)

"""
Créer une classe personnalisée pour une liste
"""


class CustomListe(list):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.valeurs = self.args
    
    def append(self, mot):
        if isinstance(mot, int):
            print("Vous ne pouvez pas ajouter de nombre a la liste")
            return False
        
        if isinstance(mot, list):
            self.valeurs.extend(mot)
            
        elif isinstance(mot, str):
            self.valeurs.append(mot)
            
        self.remove_duplicates()
    
    def remove_duplicates(self):
        self.valeurs = sorted(list(set(self.valeurs)))


ma_liste = CustomListe("Pierre", "Julien", "Marie")
ma_liste.append(5)
# ma_liste.append("Peter", "Julien", "Marie", 5)
ma_liste.append("Pierre")
ma_liste.append("Justin")
print(ma_liste.valeurs)

"""
    class CustomListe(list):
        def __init__(self, *args):
            self.valeurs = list(args)
     
        def append(self, value):
            if isinstance(value, int):
                print("Vous ne pouvez pas ajouter de nombre à la liste")
                return False
            if isinstance(value, list):
                self.valeurs.extend(value)
            elif isinstance(value, str):
                self.valeurs.append(value)
     
            self.remove_duplicates()
     
        def remove_duplicates(self):
            self.valeurs = sorted(list(set(self.valeurs)))
     
     
    ma_liste = CustomListe("Pierre", "Julien", "Marie")
    ma_liste.append(5)
    ma_liste.append("Pierre")
    print(ma_liste.valeurs)
"""

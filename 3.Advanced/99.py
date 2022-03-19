"""
Erreur d'héritage entre deux classes
"""


class Chien(object):
    def __init__(self, race):
        self.race = race
    
    @property
    def taille(self):
        return 100


class Chihuahua(Chien):
    def __init__(self, nom):
        super().__init__("Chihuahua")
        self.nom = nom


chien = Chihuahua("Lily")
print(chien.race)

"""
    EXPLICATION

Cet exercice touche à l'héritage et contenait une erreur que vous deviez identifier et résoudre.
Le problème du script de départ était que la classe Chihuahua n'appelait jamais le constructeur __init__ de la fonction
dont elle héritait.
Nous essayions d'afficher la race du chien alors qu'elle n'est pas définie dans la classe Chihuahua, et la classe
"Chien" dont Chihuahua hérite et qui contient l'attribut race dans sa méthode __init__ n'est jamais appelée.
Pour remédier à cela, nous utilisons la fonction "super" qui nous permet d'appeler la méthode __init__ de la classe
parent de Chihuahua :

    super().__init__("Chihuahua")

Vous remarquerez que nous profitons de l'appel à la méthode __init__ pour passer en argument la race du chien
("Chihuahua"), ce qui permettra donc d'afficher la bonne valeur lors du print de la race du chien à la dernière
ligne du script.

À la place de la fonction super, on peut explicitement utiliser le nom de la classe parente :

    Chien.__init__(self, "Chihuahua")

L'avantage d'utiliser la fonction super est que nous n'avons pas besoin de référer directement au nom de la classe
parent.
Ainsi, si nous décidons plus tard de renommer la classe "Chien" en "Chat", notre classe "Chihuahua" fonctionnera
toujours si on utilise super, mais nous retourneras une erreur si on utilise explicitement le nom de la classe "Chien".

Il est important de noter également que la syntaxe de la fonction super a été grandement allégée avec Python 3.

Si vous utilisez Python 2, vous devez passer deux arguments à la fonction super : la classe et l'instance de la classe :

    super(Chihuahua, self).__init__("Chihuahua")

La syntaxe est plus lourde et heureusement, avec Python 3, nous pouvons juste utiliser super() sans lui passer
d'arguments et cela fonctionne sans problème.

    POINTS IMPORTANTS À RETENIR
    Pour appeler une fonction d'une classe parente, on peut utiliser la fonction super.
"""

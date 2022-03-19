"""
Réimplémenter la méthode __add__

L'indice pour cet exercice est en fait dans le nom de l'exercice. Pour réussir à ajouter un espace lorsque l'on fait une
concaténation, il vous faudra ré-implémenter la méthode __add__ à l'intérieur de notre classe 'SuperStr'.

De plus, pour que cela fonctionne avec chaque concaténation et non pas seulement la première, il faut que l'objet que
vous retourniez dans la méthode __add__ soit une instance de SuperStr (c'est un peu le serpent qui se mord la queue,
mais vous verrez dans la prochaine partie avec la solution que c'est très puissant !).

Bon courage avec cet exercice qui paraît simple de prime abord mais qui j'imagine va vous donner un peu de fil à
retordre !
"""


class SuperStr(str):
    def __init__(self, chaine):
        self.chaine = chaine
    
    def __add__(self, mot):
        return SuperStr(f"{self.chaine} {mot}")


s = SuperStr("Bonjour")
print(s + "tout" + "le" + "monde")

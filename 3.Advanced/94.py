"""
Recréer la méthode split
"""


def separateur(mot, separator):
    liste = []
    mots = ''
    
    for letter in mot:
        if letter != separator:
            mots += letter
        
        else:
            liste.append(mots)
            mots = ''
    
    liste.append(mots)
    return liste


phrase = "bonjour-tout-le-monde"
print(separateur(phrase, "-"))

"""
def separateur(mot, sep):
    liste = []
    mot_courant = ""
 
    for lettre in mot:
	if lettre != sep:
	    mot_courant += lettre
	else:
	    liste.append(mot_courant)
	    mot_courant = ""
	    
    liste.append(mot_courant)
    return liste
    
    EXPLICATION

Dans cet exercice, il fallait recréer la méthode split, qui permet de séparer une chaîne de caractère en plusieurs
éléments.
Une méthode un peu plus complexe à recréer que celle que nous avons eu à refaire dans des exercices précédent.
Notre fonction "separateur" acceptera deux paramètres : la chaîne de caractère à séparer et l'élément sur lequel on
sépare cette chaîne de caractère :

    def separateur(mot, sep):

Nous initialisons ensuite deux variables vides :

    liste = []
    mot_courant = ""

Il nous faut ensuite passer à travers chaque caractère de la chaîne de caractère contenue dans la variable "mot" pour
vérifier si on est en présence du caractère séparateur ou non.

Nous avons donc une structure conditionnelle à l'intérieur de la boucle for, qui vérifie si la lettre courante est égale
ou non au séparateur. Si c'est le cas, nous ajoutons la lettre à la variable "mot_courant" :

    for lettre in mot:
        if lettre != sep:
        mot_courant += lettre

Dans le cas de la phrase "bonjour-tout-le-monde", nous allons donc ainsi ajouter les 7 premières lettres à notre
variable mot_courant.

Puis, dans le cas où nous sommes en présence du séparateur, nous allons dans la deuxième partie de la structure
conditionnelle, le "else", dans lequel nous ajoutons le mot_courant à notre variable "liste" et nous réinitialisons la
variable mot_courant à une chaîne de caractère vide :

    else:
        liste.append(mot_courant)
        mot_courant = ""

Une fois que nous sortons de la boucle for, il ne faut pas oublier d'ajouter le contenu de la variable "mot_courant"
dans notre liste.
En effet, on n'ajoute la chaîne de caractère "mot_courant" à notre liste uniquement quand on rencontre un séparateur.
À moins donc que notre chaîne de caractère ne finisse par un séparateur, si nous n'ajoutons pas une dernière fois la
variable "mot_courant" à notre liste, nous manquerons le dernier mot de notre phrase.

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si une variable est différente d'une autre, on utilise la syntaxe !=
    Pour vérifier si une variable est égale à une autre, on utilise la syntaxe ==
"""

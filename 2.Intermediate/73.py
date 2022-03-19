"""
 Créer un générateur de mot de passe
 Dans cet exercice, nous allons creer un generator de mot de passe random.
 a l'aide du module string et du module random.
 votre mot de passe doit contenir des lettres minuscules, majuscules, n'importe
 quel chiffre de 0 a 9 et n'importe quel caractere special
"""
import string
import random

taille = 8
mot_de_passe = []
lettres = string.ascii_letters + string.digits + string.punctuation
for _ in range(taille):
    mot_de_passe.append(random.choice(lettres))

print(''.join(mot_de_passe))

"""
    SOLUTION

    import string
    import random
    
    taille = 8
    
    symboles = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(symboles) for _ in range(taille))
    
    print(mot_de_passe)

    EXPLICATION

Le but de cet exercice était de générer un mot de passe aléatoire.

Le mot de passe devait être d'une longueur définie dans la variable "taille".

La première chose à faire était de récupérer toutes les lettres de l'alphabet, les nombres et tous les symboles.

Pour récupérer ces informations, nous utilisons le module string :

    >>> symboles = string.ascii_letters + string.digits + string.punctuation
    >>> symboles
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

On utilise ensuite le module random et la fonction choice comme vu dans un exercice précédent. Cette fonction va nous
permettre de sélectionner une lettre aléatoire parmi la chaîne de caractère "symboles" que nous avons déclaré plus haut.

Pour répéter l'opération autant de fois que nécessaire, on utilise une boucle et une compréhension de liste :

    random.choice(symboles) for _ in range(taille)

Pour terminer, nous joignons ensemble tous les éléments aléatoires récupérés grâce à la fonction join :

    mot_de_passe = ''.join(random.choice(symboles) for _ in range(taille))

    POINTS IMPORTANTS À RETENIR

    Pour récupérer toutes les lettres majuscules et minuscules de l'alphabet, on utilise la constante "ascii_letters"
    du module "string".
    Pour récupérer tous les nombres, on utilise la constante "digits" du module "string".
    Pour récupérer tous les symboles du clavier, on utilise la constante "punctuation" du module "string"
    Pour récupérer une lettre aléatoire dans une chaîne de caractère, on utilise la fonction "choice" du module "random".


"""

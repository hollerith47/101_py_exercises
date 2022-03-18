"""
Créer une fonction pour remonter dans une structure de dossiers
Le but de cet exercice est de creer une fonction, qui permet de remonter dans une structure
de dossier autant de fois qu'indiqué
"""
import os


def remonter_dossier(dossiers, couche=1):
    i = 0
    while i < couche:
        dossiers = os.path.dirname(dossiers)
        i += 1
    
    return dossiers


dossier = "/Users/Hmak47/Desktop/Dossier_01/Tutoriel/Udemy"
print(remonter_dossier(dossier, 3))

"""
    EXPLICATION

Le but de cet exercice était de créer une fonction pour remonter un nombre défini de fois dans une structure de dossier.

Pour récupérer le dossier parent d'un fichier ou d'un dossier, on utilise la fonction os.path.dirname du module os.

Pour commencer, nous créons une fonction qui accepte deux arguments : un dossier à traiter et le nombre de fois que
l'on  doit remonter dans la structure de dossier :

    def remonter_dossier(dossier, iterations=1):

Pour réaliser cette opération, nous allons utiliser une boucle while ! Dans ce cas-ci, où nous devons répéter un certain nombre de fois une opération, c'est une bonne façon de faire !

Nous commençons par initialiser une variable "i" à 0 :

    i = 0

Puis, tant que "i" est plus petit que la valeur contenue dans "iterations", nous utilisons la fonction dirname pour
récupérer le dossier parent de la variable "dossier". Nous stockons ce résultat dans la variable "dossier" elle-même
afin d'avoir un processus récursif :

    while i < iterations:
        dossier = os.path.dirname(dossier)

Puis, nous finissons en incrémentant la variable "i" de 1 :

    i += 1

Attention ! Cette partie est très importante, la plus importante de tout le script même ! Si vous oubliez
d'incrémenter la valeur de i, i sera toujours plus petit que "iterations" et vous rentrerez alors dans une boucle
infinie qui fera planter votre programme, voire votre ordinateur.

Une fois que la condition est fausse (c'est à dire quand i devient plus grand que iterations), nous sortons alors de
la boucle while et nous retournons la valeur finale contenue dans la variable "dossier".

    POINTS IMPORTANTS À RETENIR

    Pour récupérer le dossier parent d'un fichier ou d'un dossier, on utilise la fonction os.path.dirname
    du module os.path.
    Pour répéter une opération un nombre défini de fois, on peut utiliser une boucle while.
"""
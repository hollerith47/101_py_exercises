"""
Ajouter un séparateur de milliers à un nombre
"""


def ajoutSeparateur(nombres):
    nombres = str(nombres)[::-1]  # inverser l'ordre de mot [::-1]
    result = ''
    
    for i, chiffre in enumerate(nombres, 1):
        # chiffre_iversted = chiffre + ',' if i % 3 == 0 and i != len(nombres) else chiffre
        if i % 3 == 0 and i != len(nombres):
            chiffre_iversted = chiffre + ','
        else:
            chiffre_iversted = chiffre
        result += chiffre_iversted
    
    return result[::-1]


def ajout_separateur(nombres):
    nombres = str(nombres)[::-1]
    resultat = ""
    
    for i, chiffre in enumerate(nombres, 1):
        chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombres) else chiffre
        resultat += chiffre_formatte
    
    return resultat[::-1]


nombre = 52039480394023
print(ajout_separateur(nombre))

print(ajoutSeparateur(nombre))

"""
    EXPLICATION

Le but de cet exercice était de formater un nombre en ajoutant une virgule entre chaque millier.

Nous déclarons donc une fonction 'ajout_separateur' à laquelle nous passons un nombre qui doit être formaté.

Tout d'abord, nous commençons par convertir notre nombre en chaîne de caractère, afin de pouvoir boucler dessus, puis
nous inversons la chaîne de caractère avec la syntaxe [::-1].

Il est très important d'inverser le nombre, car si nous commençons depuis la gauche vers la droite, cela poserait
problème avec un nombre comme 1394023 par exemple :

    # On commence par la gauche, et on ajoute une virgule tous les 3 nombres :
    139,402,3

On se retrouve avec une virgule mal placée à la fin. Si en revanche on commence à ajouter une virgule tous les 3
chiffres par la droite, on aura bien :

    1,394,023

Nous déclarons ensuite une chaîne de caractère vide, dans laquelle nous allons ajouter un à un les chiffres ou virgules
nécessaires pour le nombre final.

On commence ensuite une boucle for, avec la fonction enumerate, qui nous permet de récupérer à la fois l'indice de
l'itération et le chiffre courant. On passe le nombre 1 en deuxième argument à la fonction enumerate pour avoir un
indice qui commence à 1 et non à 0.

On utilise ensuite l'opérateur modulo et un opérateur ternaire :

    chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombre) else chiffre

Cette condition indique que si le reste de la division de i par 3 est égal à 0, alors on ajoute le chiffre plus une
virgule, si non, on garde uniquement le chiffre. On ajoute une deuxième condition (and i != len(nombre)) pour vérifier
que i n'est pas égal à la longueur du nombre. En effet, pour les nombres ayant une longueur multiple de 3, sans cette
condition, on ajouterait une virgule devant le premier nombre (par exemple, avec 123456 on se retrouverait
avec ,123,456).

Ainsi, à la première itération, i sera égal à 1, donc i % 3 sera égal à 1 et on ajoutera donc uniquement le chiffre.
Pareil lors de la 2e itération, 2 % 3 sera égal à 1.

Lors de la 3e itération, i % 3 sera égal à 0, on ajoutera donc le chiffre plus une virgule, qui correspond au séparateur
des milliers.

On ajoute ensuite ce 'chiffre_formatte' à notre variable 'resultat' pour construire petit à petit le nombre final.

Pour terminer, on retourne le nombre de nouveau inversé, pour le remettre dans le bon sens puisque nous l'avions inversé
au début de la fonction :

    return resultat[::-1]

    POINTS IMPORTANTS À RETENIR
    Pour inverser une chaîne de caractère, on peut utiliser la syntaxe [::-1]
    On peut passer un deuxième argument à la fonction enumerate pour commencer à un indice autre que 0.
    L'opérateur modulo permet de réaliser une opération tous les x itérations (car n % n est égal à 0).
"""
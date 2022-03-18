"""
Créer une pyramide de symboles
"""
symbole = "$"
taille = 10
nombres = list(range(1, taille+1))

for i in nombres:
    espace = (taille - i)
    print(espace*" ", (symbole+" ")*i)

# 2e methode
for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole + " ") * i)


"""
    EXPLICATION

On continue avec un exercice d'affichage, grâce à la fonction print.
Le but de cet exercice était d'afficher une pyramide de dollars !
Nous commençons donc par définir le symbole utilisé et la taille de la pyramide dans deux variables, respectivement
'symbole' et 'taille'.

Nous entamons ensuite une boucle for qui boucle sur une liste de nombres de la taille de notre variable 'taille'
(on commence à 1 parce que notre première ligne contient un symbole. Si on commençait à 0 on aurait une première
ligne vide).

Nous déclarons ensuite à l'intérieur de la boucle une variable 'espaces' qui contient un caractère espace, multiplié par
la taille de la liste moins la valeur contenue dans l'itération actuelle de la boucle (la variable i).
À la première itération nous aurons donc une variable espaces qui contiendra 9 espaces (10 - 1), puis 8 (10 - 2), puis
7 (10 - 3) etc.

Cela permettra de décaler notre symbole pour que le premier dollars soit au milieu de la pyramide, puis chaque symbole
suivant se retrouvera de plus en plus proche de la marge.

Nous faisons donc ensuite un print de cette variable espaces, à laquelle nous ajoutons le symbole plus un espace,
multiplié par le nombre de l'itération actuel (la variable i).
Pourquoi ajouter un espace au symbole et multiplier le tout par i ? Parce que si on n'ajoute pas d'espace au symbole, on
se retrouve avec une pyramide un peu bizarre :

             $
            $$
           $$$
          $$$$
         $$$$$
        $$$$$$
       $$$$$$$
      $$$$$$$$
     $$$$$$$$$
    $$$$$$$$$$
    
Pour que chaque symbole soit bien aligné pour constituer une pyramide, il faut qu'il y ait un espace entre chaque
symbole $.

    POINTS IMPORTANTS À RETENIR
    Pour afficher plusieurs fois de suite un caractère, on peut tout simplement multiplier une chaîne de caractère
    par un nombre.
"""
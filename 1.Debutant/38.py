"""
dans cet exercice, nous allons trier trois nombres sans avoir recours a l'utilisation
de structures conditionnelles ni a la methode sort.
"""
a = 4
b = 6
c = 2

max_num = max(a, b, c)
min_num = min(a, b, c)
milieu_num = int((a + b + c)/3)

print(f"Les nombres dans l'ordre sont {min_num}, {milieu_num} et {max_num}.")

"""
    SOLUTION

    a = 4
    b = 6
    c = 2
    
    a1 = min(a, b, c)
    a3 = max(a, b, c)
    a2 = (a + b + c) - a1 - a3
    
    print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))

    EXPLICATION
Dans cet exercice, il fallait penser un peu plus à la solution car il était interdit d'utiliser les structures
conditionnelles.

Pour résoudre ce problème, nous commençons par trouver le nombre le plus petit et le nombre le plus grand entre les
trois variables a, b et c grâce aux fonctions min et max.

Cela nous donne donc la variable a1 et la variable a3 :

    a1 = min(a, b, c)
    a3 = max(a, b, c)

Puisque nous ne pouvons pas savoir d'avance quelles variables parmi a, b et c vont correspondre à la valeur la plus
petite et la valeur la plus grande, il nous faut faire un peu d'arithmétique pour trouver la valeur du milieu.

Pour se faire, nous additionnons les trois valeurs ensemble (a, b et c) puis nous soustrayons les deux variables
précédemment trouvées avec la fonction min et max :

    a2 = (a + b + c) - a1 - a3

    POINTS IMPORTANTS À RETENIR
    Pour trouver la valeur maximale ou minimale entre plusieurs variables, on utilise les fonctions min et max.
"""
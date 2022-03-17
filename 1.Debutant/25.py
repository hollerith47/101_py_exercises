liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

# resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))] erreur inclu
resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
print(resultat)

# print(sorted(list(set(liste))))

"""
EXPLICATION
Il est courant de faire ce genre d'erreurs dans des scripts qui contiennent beaucoup de parenthèses et crochets.

Une bonne façon de vérifier si vous n'avez pas oublié une parenthèse ou un crochet est de compter dans un sens le nombre
de parenthèse / crochet ouvrant, et ensuite de compter dans l'autre sens si vous avez bien le même nombre de
parenthèse / crochet fermant.

POINTS IMPORTANTS À RETENIR
Une seule chose : attention à la syntaxe !
"""

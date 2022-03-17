"""
dans cet exercice, nous allons melanger les lettres d'un mot grace au module
random. le mot melanger devra commencer par une majuscuke. dans cet exercice
nous allons melanger le mot 'Bonjour'
c'est script devra melanger les lettres de ce mot pour donner par example :
"ojnourb"
"""

import random

mot = "Bonjour"
mot = list(mot)
random.shuffle(mot)
melande_mot = ''.join(mot).capitalize()
print(mot)
print(melande_mot)

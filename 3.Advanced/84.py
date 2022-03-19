"""
Recréer la méthode join
"""


def join(*args):
    resultat_final = ''
    sep = args[0]
    elements = args[1:]
    
    for element in elements:
        resultat_final += element + sep
    
    return resultat_final[:-1]


j = join(":", "Bonjour", "tout", "le", "monde")
print(j)

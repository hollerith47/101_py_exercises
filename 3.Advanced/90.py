"""
 Recréer la méthode replace
"""


def replace(phrase, mot_a_remplacer, nouveau_mot):
    while mot_a_remplacer in phrase:
        indice_debut_mot = phrase.index(mot_a_remplacer)
        indice_fin_mot = indice_debut_mot + len(mot_a_remplacer)
        
        phrase = list(phrase)
        phrase[indice_debut_mot:indice_fin_mot] = list(nouveau_mot)
        phrase = ''.join(phrase)
    
    return phrase


phrase1 = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")
print(phrase1)

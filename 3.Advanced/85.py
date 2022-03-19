"""
Créer un dossier pour chaque lettre de l'alphabet
"""
import os
import string
from pathlib import Path

cur_dir = Path.cwd()
alphabet_dir = Path.joinpath(cur_dir, 'alphabet_85')
list_alphabet_letter = string.ascii_uppercase

for letter in list_alphabet_letter:
    letter_dir = Path.joinpath(alphabet_dir, letter)
    if not Path.is_dir(letter_dir):
        os.makedirs(letter_dir)
    # Path.mkdir(letter_dir, exist_ok=True)
# print(alphabet_dir)
# print(list_alphabet_letter)

"""
2e methode

    import os
    import string
     
    directory = os.path.dirname(__file__)
    alphabet_dir = os.path.join(directory, "alphabet")
    
    for lettre in string.ascii_uppercase:
        lettre_dir = os.path.join(alphabet_dir, lettre)
        if not os.path.isdir(lettre_dir):
            os.makedirs(lettre_dir)
"""

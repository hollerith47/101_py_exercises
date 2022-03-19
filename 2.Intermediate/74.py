"""
Vérifier si un mot de passe est valide
Dans cet exercice nous allons proceder a la verification du mot de passe generer precedemment
si, il est valide ou pas
condition:
1. contenir au moins 8 caracteres
2. contenir au moins une lettre majuscule
3. contenir au moins deux chiffres
"""
import string
import random

taille = random.randint(4, 12)

symboles = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = ''.join(random.choice(symboles) for _ in range(taille))


def validateurMotDePasse(mdp):
    if len(mdp) >= 8 and any(letter.isupper() for letter in mdp) and len([n for n in str(mdp) if n.isdigit()]) >= 2:
        return True
    return False


print(mot_de_passe)
succes = validateurMotDePasse(mot_de_passe)
print(succes)

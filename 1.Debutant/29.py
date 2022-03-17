import os

# chemin_variable_env = os.environ.get('HOME')  # le dossier principale du projet
# chemin_variable_env = os.environ.get('PYTHONPATH')  # LE CHEMIN DE PYTHON
chemin_variable_env = os.environ  # Afficher tout le variable d'environnement
print(chemin_variable_env)

"""
Dans cet exercice le script a pour objectif de trouver le variable d'environnement
dans un projet grace au module environ qui se charge de trouver la variable d'environnement.
"""
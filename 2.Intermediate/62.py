"""
Transformer un chemin relatif en absolu
le but dans cet exercice est d'enlever le .. dans le chemin et effectuer le changement
absolu dans le chemin du dossier donnee.
"""
import os


def normalizePath(path_directory):
    path_directory_parts = path_directory.split("/")
    # print(path_directory_parts)
    while ".." in path_directory_parts:
        index = path_directory_parts.index("..")
        # print(index)
        path_directory_parts.pop(index)
        path_directory_parts.pop(index - 1)
    
    # print(path_directory_parts)
    return os.sep.join(path_directory_parts)


chemin = "c:/Users/Herman/Desktop/output/../../Documents/Python"
print(normalizePath(chemin))

import os

fichier = "C:/Python36/python.exe"
extention_fichier = os.path.splitext(fichier)
extention_fichier = extention_fichier[1]
extention_fichier = extention_fichier.strip('.')
print(extention_fichier)

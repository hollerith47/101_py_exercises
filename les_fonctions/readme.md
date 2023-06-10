```python
score = 0
def poser_question(question, reponse):
    global score
    reponse_correcte = False
    choix_bonne_reponse = input(question)
    if choix_bonne_reponse == reponse:
        print("Bravo, vous avez trouvé la bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse, veuillez réessayer")
    print()
```
pour changer la valeur de la variable score dans une fonction
il faut utiliser le mot `global` comme sur la ligne 4
dans la fonction poser_question sinon il est impossible de 
changer la valeur de la variable score qui est une variable
globale.
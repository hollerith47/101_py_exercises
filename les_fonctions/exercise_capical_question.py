Question_1= """Question 1: Quelle est la capitale de la france?
    a. Paris
    b. Lyon
    c. Bordeaux
    d. Toulouse
votre reponse: """
bonne_reponse_1 = 'a'
Question_2 = """Question 2: Quelle est la capitale de l'italie?
    a. Rome
    b. Milan
    c. Florence
    d. Venice
votre reponse: """
bonne_reponse_2 = 'a'
Question_3 = """Question 3: Quelle est la capitale de l'allemagne?
    a. Paris
    b. Berlin
    c. Frankfurt
    d. Munich
votre reponse: """
bonne_reponse_3 = 'b'
Question_4 = """Question 4: Quelle est la capitale de l'estonie?
    a. Tallinn
    b. Kiev
    c. Kyiv
    d. Lviv
votre reponse: """
bonne_reponse_4 = 'a'
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
    

poser_question(Question_1, bonne_reponse_1)
poser_question(Question_2, bonne_reponse_2)
poser_question(Question_3, bonne_reponse_3)
poser_question(Question_4, bonne_reponse_4)
print("Score final : " + str(score))



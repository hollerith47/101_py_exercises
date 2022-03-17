chaine = "Pierre, Julien, Anne, Marie, Lucien"
# pour ordonner cette chaine de caractère on va procéder comme suit

chaine_en_liste = chaine.split(", ")
chaine_en_liste.sort()
chaine_ordonnee = ", ".join(chaine_en_liste)
print(chaine_ordonnee)

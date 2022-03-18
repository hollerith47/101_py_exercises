"""
Trier une liste d'employés
"""
import string

employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]
lettreAphabet = string.ascii_lowercase
miieu = int(len(lettreAphabet)/2)

alphabet_a_m = lettreAphabet[:miieu]
alphabet_n_z = lettreAphabet[miieu:]

employes_a_m = []
employes_n_z = []

for employe in employes :
    fistletter = employe[0].lower()
    if fistletter in alphabet_a_m :
        employes_a_m.append(employe)
    else:
        employes_n_z.append(employe)
        
" ".join(sorted(employes_a_m))
" ".join(sorted(employes_n_z))
print("Employés de A à M: ", " , ".join(sorted(employes_a_m)))
print("Employés de N à Z: ",  " , ".join(sorted(employes_n_z)))

# Solution avancée


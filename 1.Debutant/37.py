
age = int(input("Entrez l'age du chien: "))


# if age > 0:
#     if 0 < age <= 2:
#         age_chien = age * 10.5
#     else:
#         age_chien = 21 + (age - 2) * 4
#     print("L'age du chien est ", age_chien)
# else:
#     print("l'age doit etre positif")
#     exit()
if age < 0:
    print("l'age doit etre positif")
    exit()
elif age <=2:
    age_chien = age * 10.5
else:
    age_chien = 21 + (age - 2) * 4
    
print("L'age du chien est ", age_chien)

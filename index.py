from tinydb import TinyDB

db = TinyDB("Table_of_content.json", indent=4, encoding='utf-8')

with open("Table_of_content.txt", "r") as f:
    table = f.readlines()

"""
table_de_matiere = {}
i = 1
for ligne in table:
    contenu = ligne.replace('\n', '').split('. ')
    if len(contenu) == 2:
        table_de_matiere[f"{contenu[0]}"] = contenu[1]
    else:
        table_de_matiere[f"{i}"] = contenu[0]  # print(len(contenu))
    i += 1
# print(table_de_matiere)
db.insert(table_de_matiere)
print(len(db))
"""

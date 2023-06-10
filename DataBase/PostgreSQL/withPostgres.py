import psycopg2

# Paramètres de connexion à la base de données
host = "localhost"
database = "university"
user = "postgres"
password = "postgres"

# Connexion à la base de données
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Exemple d'exécution d'une requête SQL
cur.execute("SELECT * FROM student")

# Récupération des résultats
results = cur.fetchall()
for row in results:
    print(row)

# Fermeture du curseur et de la connexion à la base de données
cur.close()
conn.close()

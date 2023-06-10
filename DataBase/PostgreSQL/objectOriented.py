import psycopg2


class PostgreSQL:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        self.cur = self.conn.cursor()
    
    def execute_query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    # Création d'une instance de la classe PostgreSQL
    db = PostgreSQL(host="localhost", database="university", user="postgres", password="postgres")
    db_apiFlask = PostgreSQL(host="localhost", database="flask", user="postgres", password="postgres")
    # Exécution d'une requête SQL
    sql = """SELECT * FROM public.subject WHERE subj_id IN (
                SELECT subj_id
                FROM public.exam_marks
                WHERE student_id IN (12,32))"""
    sql2 = "SELECT LOWER (surname), UPPER(name) FROM public.student WHERE kurs = 3 AND stipend > 0"
    sql3 = """SELECT student_id,';', surname,';', name, stipend, kurs, city, DATE_PART('year', birthday) AS Birth,
    univ_id
	            FROM public.student"""
    news = "SELECT * FROM news"
    results = db_apiFlask.execute_query(news)
    user_list = [{'id': new[0], 'title': new[1], 'content': new[2], 'published_at': new[3]} for new in results]

    # Affichage des résultats dans la console
    print(user_list)
    # for row in results:
        # print(row)
    """
    for row in results:
        print("Surname : " + row[0] + " | name : " + row[1])
    """
    # Fermeture de la connexion à la base de données
    del db

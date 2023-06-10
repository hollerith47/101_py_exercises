from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import datetime
import bcrypt
import psycopg2
import random

app = Flask(__name__)
# signer les jetons JWT
app.config['JWT_SECRET_KEY'] = 'b"#ey\x0cFh\xe7@Sc \xa8=\xef\x1b\xd0\x860\xa3\xdf\xfa\x97\xe3'  # Clé secrète pour
jwt = JWTManager(app)
# Paramètres de connexion à la base de données
host = "localhost"
database = "flask"
user = "postgres"
password = "postgres"


# Fonction de connexion à la base de données
def get_db():
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    return conn


# index page
@app.route("/")
def index():
    return jsonify({"Message": "Hello world"})


# Endpoint pour enregistrer un nouvel utilisateur
@app.route('/api/register', methods=['POST'])
def register():
    # Récupération des données de la requête
    data = request.json
    username = data.get('username')
    password = data.get('password')
    userId = random.randint(10000, 99999)
    
    # Vérification que l'utilisateur n'existe pas déjà
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    if user:
        return jsonify({'error': 'Cet utilisateur existe déjà.'}), 400

    # Hash du mot de passe
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Création d'un nouvel utilisateur
    cur.execute("INSERT INTO users (user_id, username, password) VALUES (%s, %s, %s)", (userId, username, hashed_password))
    conn.commit()
    
    return jsonify({'message': 'Utilisateur enregistré avec succès.'}), 201


# Endpoint pour se connecter avec un nom d'utilisateur et un mot de passe
@app.route('/api/login', methods=['POST'])
def login():
    # Récupération des données de la requête
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Vérification que l'utilisateur existe et que le mot de passe est correct
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username))
    user = cur.fetchone()
    if not user:
        return jsonify({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}), 401

    # Vérification que le mot de passe est correct
    if not bcrypt.checkpw(password.encode('utf-8'), user[2]):
        return jsonify({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}), 401
    # Création d'un jeton JWT avec une durée de validité de 24 heures
    expires = datetime.timedelta(hours=24)
    access_token = create_access_token(identity=username, expires_delta=expires)
    # Retourne le jeton d'authentification
    return jsonify({'access_token': access_token}), 200


# Endpoint pour accéder à l'interface d'administration (avec authentification requise)
@app.route('/api/admin', methods=['GET'])
@jwt_required()  # Décoration de la fonction pour exiger un jeton JWT valide
def admin():
    # Récupération de tous les utilisateurs
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    # Retourne la liste de tous les utilisateurs
    user_list = [{'username': user[0], 'password': user[1]} for user in users]
    return jsonify(user_list), 200


if __name__ == '__main__':
    app.run(debug=True)

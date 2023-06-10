from flask import Flask, jsonify, request, url_for
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import datetime
import psycopg2
from flask_mail import Mail, Message
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
app.config['MAIL_SERVER'] = 'mail.htech-cloud.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'registration@htech-cloud.com'
app.config['MAIL_PASSWORD'] = 'ra}E?4f0Fl2~'
mail = Mail(app)

# Configuration de la base de données
app.config['DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flask'
conn = psycopg2.connect(app.config['DATABASE_URI'])

# Configuration de la clé secrète pour la gestion des tokens JWT
app.config['JWT_SECRET_KEY'] = 'b"#ey\x0cFh\xe7@Sc \xa8=\xef\x1b\xd0\x860\xa3\xdf\xfa\x97\xe3'
jwt = JWTManager(app)


# Fonction pour récupérer une connexion à la base de données
def get_db():
    return conn

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':"Server is running", 'response': "success"})

# Endpoint pour enregistrer un nouvel utilisateur
@app.route('/api/register', methods=['POST'])
def register():
    # Récupération des données de la requête
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    
    # Vérification que l'utilisateur n'existe pas déjà
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cur.fetchone()
    if user:
        return jsonify({'error': 'Cet email existe déjà.'}), 400
    
    # Hashage du mot de passe
    hashed_password = generate_password_hash(password, method='sha256')
    
    # Création d'un nouvel utilisateur
    cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, hashed_password, email))
    get_db().commit()
    # return jsonify({'message': "registration successful"})
    # Génération de l'URL de confirmation avec le nom d'utilisateur en tant que paramètre de requête
    confirmation_url = url_for('confirm', username=username, _external=True)
    # Envoi de l'e-mail de confirmation
    message = Message(subject='Confirmation d\'inscription', sender=app.config['MAIL_USERNAME'], recipients=[email])
    message.html = 'Bonjour, vous vous êtes inscrit sur notre site. Merci de cliquer sur ce lien pour confirmer votre ' \
                   'inscription : <a href="http://localhost:8000/api/confirm/{0}">Confirmer</a>. Votre nom ' \
                   'd\'utilisateur ' \
                   'est {1}'.format(username, username)
    mail.send(message)
    
    return jsonify({'message': 'Un e-mail de confirmation a été envoyé à {0}. Veuillez cliquer sur le lien dans '
                               'cet e-mail pour activer votre compte.'.format(email)}), 201


@app.route('/api/confirm/<username>', methods=['GET'])
def confirm(username):
    # Vérification que l'utilisateur existe
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    if not user:
        return jsonify({'error': 'Utilisateur non trouvé.'}), 404
    
    # Activation du compte
    cur.execute("UPDATE users SET confirmed=true WHERE username=%s", (username,))
    get_db().commit()
    
    return jsonify({'message': 'Votre compte a été activé avec succès.'}), 200


# Endpoint pour se connecter avec un nom d'utilisateur et un mot de passe
@app.route('/api/login', methods=['POST'])
def login():
    # Récupération des données de la requête
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Récupération de l'utilisateur depuis la base de données
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    if not user:
        return jsonify({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}), 401
    
    # Vérification du mot de passe hashé
    if not check_password_hash(user[2], password):
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
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    
    # Retourne la liste de tous les utilisateurs
    user_list = [{'id': u[0], 'username': u[1], 'email': u[3]} for u in users]
    return jsonify({'users': user_list}), 200


@app.route('/api/news', methods=['GET'])
def getNews():
    # Récupération des données de la requête
    cur = get_db().cursor()
    cur.execute("SELECT * FROM news")
    news = cur.fetchall()
    
    # Retourne la liste de tous les utilisateurs
    news_list = [{'_id': new[0], 'title': new[1], 'content': new[2], 'published_at': new[3].strftime('%d-%m-%Y')} for
                 new in news]
    return jsonify({'news': news_list}), 200


@app.route('/api/news', methods=['POST'])
def postNews():
    # Récupération des données de la requête
    data = request.json
    title = data.get('title')
    content = data.get('content')
    now = datetime.datetime.now()
    
    cur = get_db().cursor()
    # Création du news
    cur.execute("INSERT INTO news (title, content, date) VALUES (%s, %s, %s)", (title, content, now))
    get_db().commit()
    
    return jsonify({'message': 'Post publier avec success'})


if __name__ == '__main__':
    app.run(debug=True, port=8000)

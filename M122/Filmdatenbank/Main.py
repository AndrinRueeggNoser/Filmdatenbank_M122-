import json
import logging
from flask import Flask, render_template, request
import psycopg2
from flask_mail import Mail, Message
import os
import zipfile

app = Flask(__name__)


logging.basicConfig(filename='programm.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


with open('config.json') as f:
    config = json.load(f)


dbname = config['database']['dbname']
user = config['database']['user']
password = config['database']['password']
host = config['database']['host']
port = config['server']['port']


app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'andrin.rueegg@noseryoung.com'
app.config['MAIL_PASSWORD'] = 'Kingbro88unddiniMum'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cur = conn.cursor()
except Exception as e:
    app.logger.error("Failed to connect to the database: %s", e)

query = """
INSERT INTO movies (name, release_date, length_minutes, rating, category)
VALUES (%s, %s, %s, %s, %s);
"""

check_query = """
SELECT * FROM movies WHERE name = %s AND release_date = %s;
"""

movie_data = [
    ("Spiderman: No Way Home", "2021-12-17", 148, "8.2", "Action Adventure Fantasy"),
    ("The Matrix Resurrections", "2021-12-22", 148, "5.8", "Action Sci-Fi"),
    ("Spider-Man: Across the Spider-Verse", "2022-06-02", 140, "8.6", "Action Animation"),
    ("Iron Man", "2008-04-30", 126, "7.9", "Action"),
    ("Emily Erdbeer", "2012-12-13", 30, "5.5", "Animation"),
    ("Murder Mystery", "2019-06-14", 97, "6.0", "Detective Stories"),
    ("SpongeBob Schwammkopf", "1999-05-01", 23, "8.2", "Comedy Slapstick"),
    ("One Piece Film: Red", "2022-08-06", 100, "8.4", "Action Adventure Animation"),
    ("The Dark Knight", "2008-07-18", 152, "9.0", "Action Crime Drama"),
    ("Inception", "2010-07-16", 148, "8.8", "Action Adventure Sci-Fi"),
    ("Interstellar", "2014-11-07", 169, "8.6", "Adventure Drama Sci-Fi"),
    ("The Godfather", "1972-03-24", 175, "9.2", "Crime Drama"),
    ("Pulp Fiction", "1994-10-14", 154, "8.9", "Crime Drama"),
    ("Fight Club", "1999-10-15", 139, "8.8", "Drama"),
    ("Forrest Gump", "1994-07-06", 142, "8.8", "Drama Romance"),
    ("The Shawshank Redemption", "1994-09-22", 142, "9.3", "Drama"),
    ("The Lord of the Rings: The Return of the King", "2003-12-17", 201, "8.9", "Action Adventure Drama"),
    ("Star Wars: Episode V - The Empire Strikes Back", "1980-06-20", 124, "8.7", "Action Adventure Fantasy")
]

for movie in movie_data:
    cur.execute(check_query, (movie[0], movie[1]))
    if cur.fetchone() is None:
        try:
            cur.execute(query, movie)
            app.logger.info("Inserted movie: %s", movie[0])
        except Exception as e:
            app.logger.error("Failed to insert movie: %s, error: %s", movie[0], e)

conn.commit()

@app.route('/')
def home():
    try:
        cur.execute("SELECT * FROM movies;")
        movies = cur.fetchall()
        return render_template('index.html', movies=movies)
    except Exception as e:
        app.logger.error("Failed to fetch movies: %s", e)

@app.route('/send-mail', methods=['POST'])
def send_mail():
    try:

        zipf = zipfile.ZipFile('Table.zip', 'w', zipfile.ZIP_DEFLATED)
        zipf.write('index.html')
        zipf.close()


        msg = Message('Hello', sender='andrin.rueegg@noseryoung.com', recipients=['andrinrueegg@icloud.com'])
        msg.body = "Here is the table you requested."


        with app.open_resource('Table.zip') as fp:
            msg.attach('Table.zip', 'application/zip', fp.read())


        mail.send(msg)

        return 'Mail sent!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    try:
        app.run(debug=True, port=port)
    except Exception as e:
        app.logger.error("Failed to run the application: %s", e)

cur.close()
conn.close()
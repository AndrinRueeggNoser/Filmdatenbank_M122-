from flask import Flask, render_template
import psycopg2
app = Flask(__name__)

dbname = "moviedb"
user = "ania"
password = "123"
host = "192.168.36.138"
port = "5432"

try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
except psycopg2.OperationalError as e:
    print(f"Unable to connect to the database: {e}")
    exit(1)

cur = conn.cursor()

query = """
INSERT INTO movies (name, release_date, category, length_minutes, rating)
VALUES (%s, %s, %s, %s, %s);
"""

check_query = """
SELECT * FROM movies WHERE name = %s AND release_date = %s;
"""

movie_data = [
    ("Spiderman: No Way Home", "2021-12-17", "Action Adventure Fantasy", 148, "8.2"),
    ("The Matrix Resurrections", "2021-12-22", "Action Sci-Fi", 148, "5.8"),
    ("Spider-Man: Across the Spider-Verse", "2022-06-02", "Action Animation", 140, "8.6"),
    ("Iron Man", "2008-04-30", "Action", 126, "7.9", ),
    ("Emily Erdbeer", "2012-12-13", "Animation", 30, "5.5"),
    ("Murder Mystery", "2019-06-14", "Detective Stories", 97, "6.0"),
]

for movie in movie_data:
    cur.execute(check_query, (movie[0], movie[1]))
    if cur.fetchone() is None:
        cur.execute(query, movie)

conn.commit()

@app.route('/')
def home():
    cur.execute("SELECT * FROM movies;")
    movies = cur.fetchall()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True, port=5432)

cur.close()
conn.close()
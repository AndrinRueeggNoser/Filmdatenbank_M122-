from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

dbname = "moviedb"
user = "utopia1"
password = "060507"
host = "localhost"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()

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
        cur.execute(query, movie)

conn.commit()

@app.route('/')
def home():
    cur.execute("SELECT * FROM movies;")
    movies = cur.fetchall()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

cur.close()
conn.close()
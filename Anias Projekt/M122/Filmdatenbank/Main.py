import psycopg2

dbname = "moviedb"
user = "ania"
password = "123"
host = "localhost"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

cur = conn.cursor()

create_query = """
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    release_date DATE,
    length_minutes INT,
    rating DECIMAL(3, 1),
    category VARCHAR(50)
);
"""

select_query = """
SELECT * FROM movies WHERE name = %s AND release_date = %s;
"""

insert_query = """
INSERT INTO movies (name, release_date, length_minutes, rating, category)
VALUES (%s, %s, %s, %s, %s);
"""

movie_data = [
    ("Spiderman: No Way Home", "2021-12-17", 148, 8.2, "Action Adventure Fantasy"),
    ("The Matrix Resurrections", "2021-12-22", 148, 5.8, "Action Sci-Fi"),
]

for movie in movie_data:
    cur.execute(select_query, (movie[0], movie[1]))
    if cur.fetchone() is not None:
        continue
    cur.execute(insert_query, movie)
conn.commit()

cur.close()
conn.close()

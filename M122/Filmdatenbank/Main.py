import psycopg2

dbname = "moviedb"
user = "utopia1"
password = "060507"
host = "localhost"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

cur = conn.cursor()

select_query = """
SELECT * FROM movies WHERE name = %s AND release_date = %s;
"""

insert_query = """
INSERT INTO movies (id, name, release_date, length_minutes, rating, category)
VALUES (%s, %s, %s, %s, %s, %s);
"""

def get_next_available_id():
    cur.execute("SELECT id FROM movies WHERE id BETWEEN 1 AND 10;")
    ids = {i[0] for i in cur.fetchall()}
    all_ids = set(range(1, 11))
    available_ids = all_ids - ids
    return min(available_ids) if available_ids else None

movie_data = [
    ("Spiderman: No Way Home", "2021-12-17", 148, "8.2", "Action Adventure Fantasy"),
    ("The Matrix Resurrections", "2021-12-22", 148, "5.8", "Action Sci-Fi"),
]

for movie in movie_data:
    cur.execute(select_query, (movie[0], movie[1]))
    if cur.fetchone() is not None:
        continue
    next_id = get_next_available_id()
    if next_id is None:
        continue
    cur.execute(insert_query, (next_id, *movie))
conn.commit()

cur.close()
conn.close()
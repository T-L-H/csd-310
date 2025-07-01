import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

secrets = dotenv_values(".env")
print(secrets)
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}


def displayFilms(cursor, title):
    query = """
        SELECT film_name AS 'Film Name', 
               film_director AS 'Director', 
               genre_name AS 'Genre Name ID', 
               studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()
    print("\n-- " + title + " --")
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre Name ID: {film[2]}")
        print(f"Studio Name: {film[3]}\n")  # extra newline for spacing like sample

try:
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()




    displayFilms(cursor, "DISPLAYING FILMS")
    insert_query = """
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
    VALUES ('Star Wars', 'George Lucas', 2, 1, '1977', 121);
"""
    cursor.execute(insert_query)
    db.commit()
    displayFilms(cursor, "DISPLAYING FILMS AFTER INSERT")
    update_query = """
        UPDATE film
        SET genre_id = 1 
        WHERE film_name = 'Alien';
    """
    cursor.execute(update_query)
    db.commit()
    displayFilms(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")
    delete_query = """
        DELETE FROM film
        WHERE film_name = 'Gladiator';
    """
    cursor.execute(delete_query)
    db.commit()
    displayFilms(cursor, "DISPLAYING FILMS AFTER DELETE")

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    try:
        db.close()
    except NameError:
        pass
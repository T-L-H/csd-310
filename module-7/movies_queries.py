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

try:
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio")
    studioData = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studioData:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


    cursor.execute("SELECT * FROM genre")
    GenreData = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in GenreData:
        print("Studio ID: {}\nStudio Name: {}\n".format(genre[0], genre[1]))

    
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    shortFilm = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in shortFilm:
       print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directorFilm= cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in directorFilm:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))




   
        


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
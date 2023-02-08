import psycopg2
from config import host, user, password, db_name, port

connection = None

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    connection.autocommit = True

    # the cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version {cursor.fetchone()}")

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            nickname varchar(50) NOT NULL);"""
        )
        print(f"[INFO] Table created successfully")

    # insert data into the table
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users(first_name, nickname) VALUES
            ('Andrei', 'python_learner1');
            INSERT INTO users(first_name, nickname) VALUES
            ('Valentina', 'python_learner2');"""
        )
        print(f"[INFO] Data was successfully inserted")

    # get data from the table
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT nickname FROM users WHERE first_name = 'Valentina';"
        )
        print(f"Data selected: {cursor.fetchone()}")
        cursor.execute(
            "SELECT * FROM users;"
        )
        print(f"Data selected: {cursor.fetchall()}")

    # delete the table
    with connection.cursor() as cursor:
        cursor.execute(
            "DROP TABLE users;"
        )
        print(f"[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL:", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

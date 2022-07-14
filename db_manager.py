import sqlite3
from sqlite3 import Error
from os import path


# Creates a connection to the sql server
def create_connection():
    db = path.dirname(path.abspath(__file__))
    db = path.join(db, 'db')
    db = path.join(db, 'recomenusql.db')
    connection = None
    try:
        connection = sqlite3.connect(db)
        return connection
    except Error as er:
        print(er)
    return connection


# Creates the tables used by recoMenu
def create_tables(connection):

    users_table_sql = """CREATE TABLE IF NOT EXISTS users (
                            id integer PRIMARY KEY,
                            recommender text
                        );"""
    recipes_table_sql = """CREATE TABLE IF NOT EXISTS recipes (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            recipe text,
                            keywords json,
                            owner_id integer NOT NULL
                            FOREIGN KEY (owner_id) REFERENCES users (id)
                        );"""
    recipe_books_table_sql = """CREATE TABLE IF NOT EXISTS recipe_books (
                                user_id integer NOT NULL,
                                recipe_id integer NOT NULL,
                                rating integer,
                                FOREIGN KEY (user_id) REFERENCES users (id)
                                FOREIGN KEY (recipe_id) REFERENCES recipes (id)
                            );"""
    keywords_table_sql = """CREATE TABLE IF NOT EXISTS keywords (
                            keyword text NOT NULL,
                            recipe_ids json NOT NULL
                        );"""

    execute_sql_command(connection, users_table_sql)
    execute_sql_command(connection, recipes_table_sql)
    execute_sql_command(connection, recipe_books_table_sql)
    execute_sql_command(connection, keywords_table_sql)


# Helper function to execute a sql command given a connection and command string
def execute_sql_command(connection, sql_command):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_command)
    except Error as er:
        print(er)

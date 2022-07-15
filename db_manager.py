import sqlite3
from sqlite3 import Error
from os import path


# Add a user to the users table
def add_user(connection, user, recommender):
    sql = """INSERT INTO users(id,recommender)
                 VALUES(?,?)"""
    user_data = (user, recommender)
    curs = connection.cursor()
    curs.execute(sql, user_data)
    connection.commit()


# Add a recipe to the recipe table
def add_recipe(connection, name, recipe, keywords, owner):
    sql = """INSERT INTO recipes(name,recipe,keywords,owner_id)
                     VALUES(?,?,?,?)"""
    # TODO: Figure out how to JSON-ize the keywords
    recipe_data = (name, recipe, keywords, owner)
    curs = connection.cursor()
    curs.execute(sql, recipe_data)
    connection.commit()


# Add a recipe to a user's recipe book
def add_recipe_to_recipe_book(connection, user, recipe_name, rating):
    pass


# Add a new keyword or add a recipe to an existing keyword
def add_keyword(connection, keyword, recipe_id):
    pass


# Delete a recipe from the recipes table
def delete_recipe(connection, name):
    pass


# Remove a recipe from a user's recipe book
def remove_recipe_from_recipe_book(connection, user, name):
    pass


def modify_recipe(connection, name, recipe, keywords):
    pass


# Get a recipe from the database
def get_recipe(connection, name):
    pass


# Get a user's rating for a particular recipe
def get_rating(connection, user, recipe_name):
    pass


# Get all recipe names
def get_recipe_names(connection):
    pass


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


# Creates a connection to the test sql server
def create_testing_connection():
    db = path.dirname(path.abspath(__file__))
    db = path.join(db, 'db')
    db = path.join(db, 'recomenutestsql.db')
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

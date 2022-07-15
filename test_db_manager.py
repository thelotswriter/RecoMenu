import unittest
import db_manager


class TestDBManager(unittest.TestCase):

    def __init__(self):
        self.connection = db_manager.create_testing_connection()
        db_manager.create_tables(self.connection)

    def test_add_user(self):
        self.fail()

    def test_add_recipe(self):
        self.fail()

    def test_add_recipe_to_recipe_book(self):
        self.fail()

    def test_add_keyword(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()

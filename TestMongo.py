import unittest

from Mongo import Mongo


class TestMongo(unittest.TestCase):
    def test_create_Mongo(self):
        m = Mongo()
        self.assertIsNotNone(m)

    def test_create_database(self):
        m = Mongo()
        self.assertIsNotNone(m.create_database("test"))

    def test_get_databases(self):
        m = Mongo()
        for db in m.get_databases():
            print(db)

    def test_set_database(self):
        m = Mongo()
        print(m.set_database("test"))

    def test_delete_database(self):
        m = Mongo()
        m.delete_database("test")

    def test_create_collection(self):
        m = Mongo()
        self.assertRaises(ValueError, m.create_collection, "test")
        m.set_database("test")
        self.assertIsNotNone(m.create_collection("test"))

    def test_set_collection(self):
        m = Mongo()
        self.assertRaises(ValueError, m.create_collection, "test")
        m.set_database("test")
        self.assertIsNotNone(m.create_collection("test"))


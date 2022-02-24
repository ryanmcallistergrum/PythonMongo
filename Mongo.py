import string
import pymongo as pm
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class Mongo:
    CONNECTION_STRING: string = "mongodb://localhost:27017/"
    client: MongoClient = None
    current_database: Database = None
    current_collection: Collection = None

    def __init__(self):
        self.client = pm.MongoClient(self.CONNECTION_STRING)

    def create_database(self, dbname) -> Database:
        return self.set_database(dbname)

    def get_databases(self) -> list[Database]:
        result: list[Database] = list[Database]()
        for db in self.client.list_databases():
            if db['name'] not in ['admin', 'config', 'local']:
                result.append(db)
        return result

    def get_database(self, dbname) -> Database:
        return self.set_database(dbname)

    def set_database(self, dbname) -> Database:
        self.current_database = self.client.get_database(dbname)
        return self.current_database

    def delete_database(self, dbname) -> None:
        self.client.drop_database(dbname)

    def create_collection(self, coll_name) -> Collection:
        return self.set_collection(coll_name)

    def get_collections(self) -> list[Collection]:
        if self.current_database is None:
            raise TypeError("No database is currently selected! Please first select a database and try again!")
        colls: list[Collection] = list[Collection]()
        for coll in self.current_database.list_collections():
            colls.append(self.current_database.get_collection(coll))
        return colls

    def get_collection(self, coll_name) -> Collection:
        if self.current_database is None:
            raise TypeError("No database is currently selected! Please first select a database and try again!")
        return self.current_database.get_collection(coll_name)

    def set_collection(self, coll_name) -> Collection:
        if self.current_database is None:
            raise TypeError("Database is not set! Please first select a database and try again!")
        self.current_collection = self.current_database.get_collection(coll_name)
        return self.current_collection

    def delete_collection(self, coll_name) -> None:
        if self.current_database is None:
            raise TypeError("Database is not set! Please first select a database and try again!")
        self.current_database.drop_collection(coll_name)

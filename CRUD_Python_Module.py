from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        USER = "aacuser"
        PASS = "aacuser123"   # your actual password
        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        self.client = MongoClient(
    "mongodb://%s:%s@%s:%d/%s?authSource=admin" % (USER, PASS, HOST, PORT, DB)
)

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # C in CRUD
    def create(self, data):
        """
        Insert a document into the animals collection.

        Args:
            data (dict): key/value pairs for MongoDB document

        Returns:
            bool: True if successful insert, else False
        """
        if data is None or not isinstance(data, dict):
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except PyMongoError as e:
            print(f"Insert failed: {e}")
            return False

    # R in CRUD
    def read(self, query):
        """
        Query documents from the animals collection using find().

        Args:
            query (dict): MongoDB query dictionary

        Returns:
            list: list of matching documents, or empty list
        """
        if query is None or not isinstance(query, dict):
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read failed: {e}")
            return []

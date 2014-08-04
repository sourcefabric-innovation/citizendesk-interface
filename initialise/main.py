from collections import namedtuple

from pymongo import MongoClient

Init = namedtuple('Init', ['collection', 'data'])

client = MongoClient()
database = client['citizendesk']

def init_collection(init):
    collection = database[init.collection]
    collection.drop()
    for document in init.data: collection.insert(document)

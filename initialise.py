from collections import namedtuple

from pymongo import MongoClient

Init = namedtuple('Init', ['collection', 'data'])
users = Init('users', [{
        'username': 'Doug',
        'password': 'no',
}, {
        'username': 'Francesco',
        'password': 'no',
}, {
        'username': 'Martin',
        'password': 'no',
}, {
        'username': 'Darko',
        'password': 'no',
}])
coverages = Init('coverages', [{
        'title': 'default coverage'
}]

client = MongoClient()
database = client['citizendesk']
for init in users, coverages:
    collection = database[init.collection]
    collection.drop()
    for document in init.data:
        collection.insert(document)

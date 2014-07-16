from pymongo import MongoClient

client = MongoClient()
database = client['citizendesk']
collection = database['users']

collection.drop()

users = [{
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
}]

for user in users: collection.insert(user)

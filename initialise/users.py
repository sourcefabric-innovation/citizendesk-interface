from uuid import uuid4

from main import Init, init_collection

documents = [{
        'username': 'Doug',
}, {
        'username': 'Francesco',
}, {
        'username': 'Martin',
}, {
        'username': 'Darko',
}, {
        'username': 'Erik',
}, {
        'username': 'Aderito',
}, {
        'username': 'User1',
}, {
        'username': 'User2',
}, {
        'username': 'User3',
}, {
        'username': 'User4',
}, {
        'username': 'User5',
}]

# like in https://github.com/superdesk/Live-Blog/blob/63c713a90b8e464aff62a032cb5d85f6b1220d1d/plugins/livedesk-sync/livedesk/core/impl/chained_sync.py#L303
for document in documents:
    document['password'] = 'no'
    document['uuid']     = str(uuid4().hex)

init_users = Init('users', documents)

if __name__ == "__main__": init_collection(init_users)

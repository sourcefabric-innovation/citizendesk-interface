from uuid import uuid4

from main import Init, init_collection

documents = [{
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
}, {
        'username': 'Erik',
        'password': 'no',
}, {
        'username': 'Aderito',
        'password': 'no',
}]

# like in https://github.com/superdesk/Live-Blog/blob/63c713a90b8e464aff62a032cb5d85f6b1220d1d/plugins/livedesk-sync/livedesk/core/impl/chained_sync.py#L303
for document in documents: document['uuid'] = str(uuid4().hex)

init_users = Init('users', documents)

if __name__ == "__main__": init_collection(init_users)

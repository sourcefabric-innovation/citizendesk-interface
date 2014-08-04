from main import Init, init_collection

init_users = Init('users', [{
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
}])

if __name__ == "__main__": init_collection(init_users)

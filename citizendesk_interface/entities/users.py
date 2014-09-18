
from apps.users.users import UsersModel, ensure_hashed_password

users = {
    'schema': UsersModel.schema,
    'datasource': UsersModel.datasource,
    'extra_response_fields': UsersModel.extra_response_fields,
}


def on_insert_users(docs):
    for doc in docs:
        ensure_hashed_password(doc)

def init(app):
    app.on_insert_users += on_insert_reports

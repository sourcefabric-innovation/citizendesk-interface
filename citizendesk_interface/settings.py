from .entities.reports import entity as reports

settings = {
    'MONGO_DBNAME': 'citizendesk',

    'DOMAIN': {
        'reports': reports,
    }
}

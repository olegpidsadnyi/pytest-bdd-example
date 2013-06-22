from flask import current_app


def recreate_database():
    db = current_app.extensions['sqlalchemy'].db
    print 'Recreating database: %s' % db.engine.url.database
    db.drop_all()
    db.create_all()

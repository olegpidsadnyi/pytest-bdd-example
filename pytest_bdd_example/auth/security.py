from flask.ext.security import SQLAlchemyUserDatastore
from .models import db, User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

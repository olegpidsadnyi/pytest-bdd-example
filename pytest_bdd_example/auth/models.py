from flaskext.sqlalchemy import SQLAlchemy
from flaskext.auth.models.sa import get_user_class

from __package__ import bp


db = SQLAlchemy(bp)

UserBase = get_user_class(db.Model)


class User(UserBase):
    # Extend the user model
    pass

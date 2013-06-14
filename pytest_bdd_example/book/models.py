from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()

association_table = db.Table('association', Base.metadata,
    db.Column('left_id', db.Integer, db.ForeignKey('left.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('right.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    sur_name = db.Column(db.String(30))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50))
    description = db.Column(db.Text)

    authors = db.relationship("Author", secondary=association_table, backref="books", order_by="Author.id")

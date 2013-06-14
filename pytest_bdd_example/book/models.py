from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    sur_name = db.Column(db.String(30))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50))
    description = db.Column(db.Text)

    authors = db.relationship(
        Author,
        secondary=lambda: author_books,
        backref='books',
        order_by=Author.id,
    )


author_books = db.Table(
    'author_books',
    db.Column('author_id', db.Integer, db.ForeignKey(Author.id)),
    db.Column('book_id', db.Integer, db.ForeignKey(Book.id)),
)

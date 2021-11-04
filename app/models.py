from app import db

from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

user_book = db.Table('user_book',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text)
    password_hash = db.Column(db.String(128))
    books_read_per_year = db.Column(db.Integer)
    books = db.relationship('Book', secondary = user_book)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    critics_rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    books = db.relationship('Book', backref='genre')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Set up configuration settings for connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# The secret key here is used for demonstration purposes - DO NOT USE IN PRODUCTION
app.config['SECRET_KEY'] = 'this-is-a-secret' 

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from app.book import bp as book_bp
app.register_blueprint(book_bp, url_prefix='/book')

from app.genre import bp as genre_bp
app.register_blueprint(genre_bp, url_prefix='/genre')

from app.chart import bp as chart_bp
app.register_blueprint(chart_bp, url_prefix='/chart')

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, prefix='/auth')

from app import routes
from app.models import Book, Genre, User

@app.cli.command('init-db')
def init_db():

    # Recreate the database for the app
    db.drop_all()
    db.create_all()

    # Create some records for the different genres
    fantasy = Genre(
        name = 'Fantasy'
    )
    db.session.add(fantasy)

    programming = Genre(
        name = 'Programming'
    )
    db.session.add(programming)

    research = Genre(
        name = 'Research'
    )
    db.session.add(research)

    # Create some records for the different books in the database
    hobbit = Book(
        title = 'The Hobbit',
        author = 'J.R.R Tolkien',
        critics_rating = 8,
        genre = fantasy
    )

    dune = Book(
        title = 'Dune',
        author = 'Frank Herbert',
        critics_rating = 9,
        genre = fantasy
    )

    dark_materials = Book(
        title = 'His Dark Materials',
        author = 'Phillip Pullman',
        critics_rating = 7,
        genre = fantasy
    )

    python = Book(
        title = 'Automate the Boring Stuff with Python',
        author = 'Al Sweigart',
        critics_rating = 8,
        genre = programming
    )

    statistics = Book(
        title = 'Think Stats',
        author = 'Allen B. Downey',
        critics_rating = 7,
        genre = programming 
    )

    research_skills = Book(
        title = 'Research Skills for Teachers',
        author = 'Beverley Moriarty',
        critics_rating = 8,
        genre = research
    )

    # Create some records for the different users

    dan = User(
        username = 'dan',
        password = 'dan',
        books_read_per_year = 12
    )
    dan.books.extend([hobbit, python, statistics, research_skills])
    db.session.add(dan)

    jill = User(
        username = 'jill',
        password = 'jill',
        books_read_per_year = 30,
    )
    jill.books.extend([dune, research_skills])
    db.session.add(jill)

    dom = User(
        username = 'dom',
        password = 'dom',
        books_read_per_year = 52
    )
    dom.books.extend([hobbit, dune, dark_materials, python, statistics, research_skills])
    db.session.add(dom)

    db.session.commit()

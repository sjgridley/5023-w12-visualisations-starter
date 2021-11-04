from flask import Blueprint

bp = Blueprint('book', __name__, template_folder='templates')

from app.book import routes
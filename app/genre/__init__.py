from flask import Blueprint

bp = Blueprint('genre', __name__, template_folder='templates')

from app.genre import routes
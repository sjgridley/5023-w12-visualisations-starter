from flask import redirect, url_for
from flask_login import login_required

from app import app

@app.route('/')
@login_required
def index():
    return redirect(url_for('book.book_list'))




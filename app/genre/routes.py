from flask import render_template, url_for, redirect
from flask_login import login_required

from app import db
from app.models import Genre
from app.genre import bp
from .forms import AddGenreForm, EditGenreForm

@bp.route('/')
@login_required
def genre_list():
    ''' A route for a list of all the genres in the collection. '''
    genres = Genre.query.all()
    return render_template('genre_list.html', title = 'Genres', genres = genres)

@bp.route('/add', methods = ['GET', 'POST'])
@login_required
def genre_add():
    ''' A route for showing a form and processing form for adding a new genre. '''
    form = AddGenreForm()

    # When the form has been processed with no errors, save the new genre to database
    if form.validate_on_submit():
        genre = Genre()
        form.populate_obj(obj=genre)
        db.session.add(genre)
        db.session.commit()
        # Once the new genre has been saved, return back to the view of all genres
        return redirect(url_for('genre.genre_list'))
    return render_template('genre_add.html', form = form, title = 'Add genre')

@bp.route('/<int:id>')
@login_required
def genre_details(id):
    ''' A route to display details for a specific genre, for the given id. '''
    genre = Genre.query.get_or_404(id)
    return render_template('genre_details.html', title = 'Genre details', genre = genre)

@bp.route('/<int:id>/delete')
@login_required
def genre_delete(id):
    ''' A route that deletes a genre for the given id. '''

    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()

    # Once the genre record has been deleted, return back to the list of the genres
    return redirect(url_for('genre.genre_list'))

@bp.route('/<int:id>/edit', methods = ['GET', 'POST'])
@login_required
def genre_edit(id):
    ''' A route for displaying and processing a form, when editing a genre. '''
   
    genre = Genre.query.get_or_404(id)
    form = EditGenreForm(obj=genre)

    # When the form has been completed correctly, the changes to the genre are saved
    if form.validate_on_submit():
        form.populate_obj(obj=genre)
        db.session.commit()
        # Once the changes have been saved in database, show the view of the details for the genre
        return redirect(url_for('genre.genre_details', id = genre.id))
    
    # When the request is a GET or there are errors in the form, return the view with the form
    return render_template('genre_edit.html', title = 'Edit genre', form = form, genre = genre)
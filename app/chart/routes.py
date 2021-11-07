import json

from flask import render_template
from flask_login import login_required
import pandas as pd
import plotly.express as px
import plotly

from app import db
from app.chart import bp
from app.models import Book

@bp.route('/')
@login_required
def chart_list():
    return render_template('chart_list.html', title = 'List of Charts')

@bp.route('/book_ratings')
@login_required
def book_ratings_chart():
    # Retrieve all the books in the collection
    book_query = Book.query
    df = pd.read_sql(book_query.statement, book_query.session.bind)

    # Draw the chart and dump it into JSON format
    chart = px.bar(df, x='title', y='critics_rating')
    chart_JSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder, indent=4)

    # Returns the template, including the JSON data for the chart
    return render_template('chart_page.html', title = 'Critic ratings for books', chart_JSON = chart_JSON)
    
@bp.route('/user_books')
@login_required
def user_books_chart():
    # Run query to get count of books owned per user and load into DataFrame
    query = (
        "SELECT username, count(*) as books_owned "
        "FROM user_book ub "
        "JOIN user u on ub.user_id = u.id "
        "GROUP BY username"
    )
    df = pd.read_sql(query, db.session.bind)

    # Draw the chart and dump it into JSON format
    chart = px.bar(df, x ='username', y='books_owned')
    chart_JSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder, indent=4)

    # Returns the template, including the JSON data for the chart
    return render_template('chart_page.html', title = 'Books owned per user', chart_JSON = chart_JSON)

# TODO: Add a route for a bar chart that compares books read per year by user
@bp.route('/books_read')
@login_required
def books_read_chart():
    # Run query to get count of books owned per user and load into DataFrame
    query = (
        "SELECT username, books_read_per_year "
        "FROM user u"
    )
    df = pd.read_sql(query, db.session.bind)

    # Draw the chart and dump it into JSON format
    chart = px.bar(df, x ='username', y='books_read_per_year')
    chart_JSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder, indent=4)

    # Returns the template, including the JSON data for the chart
    return render_template('chart_page.html', title = 'Books read per year per user', chart_JSON = chart_JSON)


# TODO: Add a route for a bar chart that compares number of books per genre
@bp.route('/genre_books')
@login_required
def genre_books_chart():
    
    query = (
        "SELECT name, count(*) as number_of_books "
        "FROM genre g "
        "JOIN book b on b.genre_id = g.id "
    )
    df = pd.read_sql(query, db.session.bind)

    # Draw the chart and dump it into JSON format
    chart = px.bar(df, x ='name', y='number_of_books')
    chart_JSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder, indent=4)

    # Returns the template, including the JSON data for the chart
    return render_template('chart_page.html', title = 'Books in each Genre', chart_JSON = chart_JSON)
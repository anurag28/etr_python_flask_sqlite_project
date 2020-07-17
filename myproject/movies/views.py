from flask import url_for, redirect, render_template, request, Blueprint
from myproject import db
from myproject.models import Movie, User, Post
from myproject.movies.forms import AddMovieForm, SearchMovieForm
from flask_login import current_user
from sqlalchemy import join
from sqlalchemy.sql import select

movie = Blueprint('movie', __name__)


@movie.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        new_movie = Movie(name=form.name.data, cast=form.cast.data,
                          genre=form.genre.data, rating=form.rating.data,
                          review=form.comment.data)
        db.session.add(new_movie)
        db.session.commit()
        db.session.flush()
        movie_id = new_movie.id
        user_id = current_user.id
        new_post = Post(user_id=user_id, movie_id=movie_id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('movie.show', movie_id=movie_id))

    return render_template('add_movie.html', form=form)


@movie.route('/show', methods=['GET', 'POST'])
def show():
    p = Post.query.filter_by(user_id=current_user.id).first()
    mo = Movie.query.filter_by(id=p.movie_id).first()
    r = db.session.query(Movie.name, Post.date, Movie.cast, Movie.rating, Post.user_id).join(Post, Movie.id == Post.movie_id).all()
    return render_template('show.html', m=p, mm=mo, R=r)


@movie.route('/search_movies', methods=['GET','POST'])
def search_movies():
    form = SearchMovieForm()

    if form.validate_on_submit():
        if form.name.data:
            # movie_data = db.session.query(Movie.name, Post.date, Movie.cast, Movie.rating, Post.user_id).join(Post, Movie.id == Post.movie_id).filter_by(Movie.name == form.name.data).all()
            return redirect(url_for('movie.search_results', form.name.data))

    return render_template('search_movie.html', form=form)


@movie.route('/<name>/search_results')
def search_results(name):
    movie_details = db.session.query(Movie.name, Post.date, Movie.cast, Movie.rating, Post.user_id).join(Post,Movie.id == Post.movie_id).all()
    render_template('search_results.html', movie_details=movie_details)
